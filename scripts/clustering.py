"""
Stroke Risk Clustering Analysis
==========================
This script performs clustering analysis on healthcare data using FAMD + KMeans.
Copy and paste this into a Jupyter notebook.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

import prince  # FAMD library
import styling

# =============================================================================
# 1. Load Data
# =============================================================================

# Load train and test data
train_df = pd.read_csv('../data/train.csv')  # Using healthcare_data.csv as train
test_df = pd.read_csv('../data/test.csv')  # Using clustered data as test

print(f"Train shape: {train_df.shape}")
print(f"Test shape: {test_df.shape}")

# Define columns
categorical_cols = [
    'gender', 'employment_type', 'residence', 'age_group', 
    'bmi_category', 'smoking_habit', 'lifestyle_risk'
]

numeric_cols = [
    'age', 'has_hypertension', 'has_heart_disease', 'marital_status',
    'glucose_level', 'bmi_value', 'risk_score', 'high_glucose'
]

# =============================================================================
# 2. Preprocessing Function
# =============================================================================

def preprocess_data(df, num_imputer=None, cat_imputer=None, scaler=None, fit=True):
    """
    Preprocess data for clustering.
    Returns processed dataframe and fitted transformers (if fit=True).
    """
    df_processed = df.copy()
    
    # Handle numeric columns
    if fit:
        num_imputer = SimpleImputer(strategy='median')
        df_processed[numeric_cols] = num_imputer.fit_transform(df_processed[numeric_cols])
    else:
        df_processed[numeric_cols] = num_imputer.transform(df_processed[numeric_cols])
    
    # Handle categorical columns
    if fit:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df_processed[categorical_cols] = cat_imputer.fit_transform(df_processed[categorical_cols])
    else:
        df_processed[categorical_cols] = cat_imputer.transform(df_processed[categorical_cols])
    
    # Convert categorical to string
    for col in categorical_cols:
        df_processed[col] = df_processed[col].astype(str)
    
    # Scale numeric columns
    if fit:
        scaler = StandardScaler()
        df_processed[numeric_cols] = scaler.fit_transform(df_processed[numeric_cols])
    else:
        df_processed[numeric_cols] = scaler.transform(df_processed[numeric_cols])
    
    return df_processed, num_imputer, cat_imputer, scaler

# =============================================================================
# 3. Preprocess Training Data
# =============================================================================

train_processed, num_imputer, cat_imputer, scaler = preprocess_data(train_df, fit=True)
print("\nPreprocessing complete!")

# =============================================================================
# 4. FAMD (Factor Analysis of Mixed Data)
# =============================================================================

famd = prince.FAMD(
    n_components=10,
    random_state=42
)

# Fit FAMD on training data ONLY
X_train_famd = famd.fit_transform(train_processed[numeric_cols + categorical_cols])

print(f"FAMD fitted on training data ({len(X_train_famd.columns)} components)")

# =============================================================================
# 5. Find Optimal K
# =============================================================================

K_range = range(2, 11)
silhouette_scores = []

print("\nK | Silhouette Score")
print("-" * 30)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_train_famd)
    
    score = silhouette_score(X_train_famd, labels)
    silhouette_scores.append(score)
    
    print(f"{k} | {score:.4f}")

optimal_k = K_range[np.argmax(silhouette_scores)]
print(f"\nOptimal K: {optimal_k}")

# =============================================================================
# 6. Fit Final KMeans on Training Data
# =============================================================================

kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
train_cluster_labels = kmeans_final.fit_predict(X_train_famd)

train_df['cluster'] = train_cluster_labels

print(f"\nTrain cluster distribution:")
print(train_df['cluster'].value_counts().sort_index())

# =============================================================================
# 7. Cluster Summary (Training Data)
# =============================================================================

cluster_summary = train_df.groupby('cluster').agg({
    **{col: 'mean' for col in numeric_cols},
    **{col: lambda x: x.mode()[0] if len(x.mode()) > 0 else x.iloc[0] for col in categorical_cols}
})

print("\nCluster Summary (Training Data):")
print(cluster_summary)

# =============================================================================
# 8. Visualizations
# =============================================================================

# Silhouette Plot
fig, ax = plt.subplots(figsize=(10, 6))

sample_silhouette_values = silhouette_samples(X_train_famd, train_cluster_labels)
avg_score = silhouette_score(X_train_famd, train_cluster_labels)

y_lower = 10

for i in range(optimal_k):
    cluster_silhouette_vals = sample_silhouette_values[train_cluster_labels == i]
    cluster_silhouette_vals.sort()
    
    size_cluster = cluster_silhouette_vals.shape[0]
    y_upper = y_lower + size_cluster
    
    ax.fill_betweenx(
        np.arange(y_lower, y_upper),
        0,
        cluster_silhouette_vals
    )
    
    ax.text(-0.05, y_lower + 0.5 * size_cluster, str(i))
    y_lower = y_upper + 10

ax.axvline(x=avg_score, color="red", linestyle="--", label=f"Avg: {avg_score:.3f}")
ax.set_title(f"Silhouette Plot (K={optimal_k})", fontsize=14)
ax.set_xlabel("Silhouette Coefficient", fontsize=12)
ax.set_ylabel("Cluster", fontsize=12)
ax.legend()
styling.style_ax(ax, minor_grid=False)

plt.tight_layout()
plt.savefig('silhouette_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# Cluster Visualization (FAMD components)
fig, ax = plt.subplots(figsize=(10, 8))

scatter = ax.scatter(
    X_train_famd.iloc[:, 0], 
    X_train_famd.iloc[:, 1], 
    c=train_cluster_labels,
    cmap='viridis',
    alpha=0.5,
    s=20
)

ax.set_xlabel("FAMD Component 1", fontsize=12)
ax.set_ylabel("FAMD Component 2", fontsize=12)
ax.set_title("Cluster Visualization (FAMD + KMeans)", fontsize=14)
plt.colorbar(scatter, label="Cluster")
styling.style_ax(ax)

plt.tight_layout()
plt.savefig('cluster_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

# Cluster sizes
fig, ax = plt.subplots(figsize=(8, 6))

cluster_sizes = train_df['cluster'].value_counts().sort_index()
bars = ax.bar(cluster_sizes.index, cluster_sizes.values, color=plt.cm.viridis(np.linspace(0, 1, optimal_k)))

ax.set_xlabel('Cluster', fontsize=12)
ax.set_ylabel('Number of Patients', fontsize=12)
ax.set_title('Cluster Sizes (Training Data)', fontsize=14)
ax.set_xticks(range(optimal_k))

for i, v in enumerate(cluster_sizes.values):
    ax.text(i, v + 50, str(v), ha='center', fontsize=10)

styling.style_ax(ax, minor_grid=False)

plt.tight_layout()
plt.savefig('cluster_sizes.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 9. Apply to Test Data (NO RETRAINING)
# =============================================================================

print("\n" + "="*60)
print("APPLYING TO TEST DATA (No Retraining)")
print("="*60)

# Preprocess test data using fitted transformers
test_processed, _, _, _ = preprocess_data(test_df, num_imputer, cat_imputer, scaler, fit=False)

# Transform test data using fitted FAMD (NOT refit!)
X_test_famd = famd.transform(test_processed[numeric_cols + categorical_cols])

print(f"Test data transformed using fitted FAMD")

# Predict clusters using fitted KMeans (NOT refit!)
test_cluster_labels = kmeans_final.predict(X_test_famd)

test_df['cluster'] = test_cluster_labels

print(f"\nTest cluster distribution:")
print(test_df['cluster'].value_counts().sort_index())

# Verify cluster consistency
print(f"\nCluster centers used (from training):")
print(kmeans_final.cluster_centers_[:5])  # Show first 5 dimensions

# =============================================================================
# 10. Save Results
# =============================================================================

train_df.to_csv('../data/train_with_clusters.csv', index=False)
test_df.to_csv('../data/test_with_clusters.csv', index=False)

print("\n" + "="*60)
print("CLUSTERING ANALYSIS COMPLETE")
print("="*60)
print(f"Number of clusters: {optimal_k}")
print(f"Silhouette Score (train): {avg_score:.4f}")
print(f"\nTraining data saved: train_with_clusters.csv")
print(f"Test data saved: test_with_clusters.csv")