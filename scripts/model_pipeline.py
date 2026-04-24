"""
Model Comparison Pipeline with Cross-Validation
================================================
A comprehensive pipeline for comparing multiple classification models.
Copy and paste this into a Jupyter notebook.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import (
    cross_val_score, StratifiedKFold, GridSearchCV
)
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier, GradientBoostingClassifier,
    AdaBoostClassifier, BaggingClassifier
)
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report,
    balanced_accuracy_score
)
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Try importing XGBoost and CatBoost
try:
    from xgboost import XGBClassifier
except ImportError:
    XGBClassifier = None

try:
    from catboost import CatBoostClassifier
except ImportError:
    CatBoostClassifier = None

import styling

# =============================================================================
# 1. Configuration
# =============================================================================

# Target variable
TARGET = 'stroke_event'

# Features to exclude
EXCLUDE = ['patient_id', TARGET, 'Unnamed: 0']

# Numerical features
NUMERICAL_COLS = ['age', 'glucose_level', 'bmi_value', 'risk_score']

# Categorical features
CATEGORICAL_COLS = [
    'gender', 'age_group', 'has_hypertension', 'has_heart_disease',
    'marital_status', 'employment_type', 'residence', 'high_glucose',
    'bmi_category', 'smoking_habit', 'lifestyle_risk', 'cluster'
]

# Cross-validation settings
CV_FOLDS = 5
CV_STRATIFIED = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=42)

# =============================================================================
# 2. Model Definitions (Easy to Edit)
# =============================================================================

def get_models_balanced():
    """
    Returns dictionary of models WITH class balancing.
    Edit this function to add/remove/modify models.
    """
    models = {
        # --- Logistic Regression ---
        'Logistic Regression (Balanced)': LogisticRegression(
            class_weight='balanced',
            max_iter=1000,
            random_state=42
        ),
        
        # --- SVM ---
        'SVM (Balanced)': SVC(
            class_weight='balanced',
            probability=True,
            random_state=42
        ),
        
        # --- Decision Tree ---
        'Decision Tree (Balanced)': DecisionTreeClassifier(
            class_weight='balanced',
            random_state=42
        ),
        
        # --- Random Forest ---
        'Random Forest (Balanced)': RandomForestClassifier(
            class_weight='balanced',
            n_estimators=100,
            random_state=42
        ),
        
        # --- Gradient Boosting ---
        'Gradient Boosting': GradientBoostingClassifier(
            n_estimators=100,
            random_state=42
        ),
        
        # --- XGBoost ---
        # 'XGBoost (Balanced)': XGBClassifier(
        #     scale_pos_weight='balanced',
        #     n_estimators=100,
        #     use_label_encoder=False,
        #     eval_metric='logloss',
        #     random_state=42
        # ) if XGBClassifier else None,
        
        # --- CatBoost ---
        'CatBoost (Balanced)': CatBoostClassifier(
            auto_class_weights='Balanced',
            verbose=0,
            random_state=42
        ) if CatBoostClassifier else None,
    }
    
    # Remove None values (if library not installed)
    return {k: v for k, v in models.items() if v is not None}


def get_models_unbalanced():
    """
    Returns dictionary of models WITHOUT class balancing.
    Edit this function to add/remove/modify models.
    """
    models = {
        # --- Logistic Regression ---
        'Logistic Regression': LogisticRegression(
            max_iter=1000,
            random_state=42
        ),
        
        # --- SVM ---
        'SVM (RBF)': SVC(
            probability=True,
            random_state=42
        ),
        
        # --- Decision Tree ---
        'Decision Tree': DecisionTreeClassifier(
            random_state=42
        ),
        
        # --- Random Forest ---
        'Random Forest': RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),
        
        # --- Gradient Boosting ---
        'Gradient Boosting': GradientBoostingClassifier(
            n_estimators=100,
            random_state=42
        ),
        
        # --- XGBoost ---
        # 'XGBoost': XGBClassifier(
        #     n_estimators=100,
        #     use_label_encoder=False,
        #     eval_metric='logloss',
        #     random_state=42
        # ) if XGBClassifier else None,
        
        # --- CatBoost ---
        'CatBoost': CatBoostClassifier(
            verbose=0,
            random_state=42
        ) if CatBoostClassifier else None,
    }
    
    return {k: v for k, v in models.items() if v is not None}


# =============================================================================
# 3. Load and Prepare Data
# =============================================================================

print("Loading data...")
df = pd.read_csv('../data/train_with_clusters.csv')
print(f"Dataset shape: {df.shape}")

# Separate features and target
X = df.drop(columns=[col for col in EXCLUDE if col in df.columns])
y = df[TARGET]

# Encode categorical variables
le_dict = {}
for col in CATEGORICAL_COLS:
    if col in X.columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        le_dict[col] = le

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

print(f"Features shape: {X_scaled.shape}")
print(f"Target distribution:\n{y.value_counts()}")

# =============================================================================
# 4. Cross-Validation Function
# =============================================================================

def evaluate_model_cv(model, X, y, cv, model_name, scoring='f1'):
    """
    Evaluate a model using cross-validation.
    """
    try:
        scores = cross_val_score(model, X, y, cv=cv, scoring=scoring, n_jobs=-1)
        return {
            'model_name': model_name,
            'mean_score': scores.mean(),
            'std_score': scores.std(),
            'scores': scores
        }
    except Exception as e:
        print(f"Error evaluating {model_name}: {e}")
        return None


def run_cv_comparison(models, X, y, cv, scoring='f1'):
    """
    Run cross-validation for all models.
    Returns a DataFrame with results.
    """
    results = []
    
    for name, model in models.items():
        print(f"Evaluating: {name}...")
        result = evaluate_model_cv(model, X, y, cv, name, scoring)
        
        if result:
            results.append(result)
            print(f"  {name}: {result['mean_score']:.4f} (+/- {result['std_score']:.4f})")
    
    return pd.DataFrame(results)


# =============================================================================
# 5. Run Comparison
# =============================================================================

print("\n" + "="*70)
print("CROSS-VALIDATION RESULTS (Balanced Models)")
print("="*70)

balanced_models = get_models_balanced()
results_balanced = run_cv_comparison(balanced_models, X_scaled, y, CV_STRATIFIED, 'f1')

print("\n" + "="*70)
print("CROSS-VALIDATION RESULTS (Unbalanced Models)")
print("="*70)

unbalanced_models = get_models_unbalanced()
results_unbalanced = run_cv_comparison(unbalanced_models, X_scaled, y, CV_STRATIFIED, 'f1')

# =============================================================================
# 6. Combine and Display Results
# =============================================================================

results_combined = pd.concat([results_balanced, results_unbalanced], ignore_index=True)
results_combined = results_combined.sort_values('mean_score', ascending=False).reset_index(drop=True)

print("\n" + "="*70)
print("COMBINED RANKING (by F1 Score)")
print("="*70)
print(results_combined[['model_name', 'mean_score', 'std_score']].to_string(index=False))

# =============================================================================
# 7. Visualization
# =============================================================================

# Bar plot comparison
fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#2ecc71' if 'Balanced' in name else '#3498db' for name in results_combined['model_name']]

bars = ax.barh(
    results_combined['model_name'],
    results_combined['mean_score'],
    xerr=results_combined['std_score'],
    color=colors,
    capsize=5,
    alpha=0.8
)

ax.set_xlabel('F1 Score', fontsize=12)
ax.set_ylabel('Model', fontsize=12)
ax.set_title('Model Comparison (Cross-Validation F1 Score)', fontsize=14)
ax.invert_yaxis()

# Add value labels
for i, (score, std) in enumerate(zip(results_combined['mean_score'], results_combined['std_score'])):
    ax.text(score + std + 0.01, i, f'{score:.3f}', va='center', fontsize=10)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2ecc71', label='Balanced'),
    Patch(facecolor='#3498db', label='Unbalanced')
]
ax.legend(handles=legend_elements, loc='lower right')

styling.style_ax(ax, minor_grid=False)
plt.tight_layout()
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 8. Multi-Metric Comparison
# =============================================================================

def get_detailed_metrics(models, X, y, cv):
    """
    Get detailed metrics for all models.
    """
    from sklearn.model_selection import cross_val_predict
    
    metrics_data = []
    
    for name, model in models.items():
        print(f"Detailed metrics: {name}...")
        
        # Get predictions via cross-validation
        y_pred = cross_val_predict(model, X, y, cv=cv)
        
        metrics_data.append({
            'Model': name,
            'Accuracy': accuracy_score(y, y_pred),
            'Balanced Accuracy': balanced_accuracy_score(y, y_pred),
            'Precision': precision_score(y, y_pred),
            'Recall': recall_score(y, y_pred),
            'F1 Score': f1_score(y, y_pred),
            'ROC AUC': roc_auc_score(y, y_pred),
        })
    
    return pd.DataFrame(metrics_data)


print("\n" + "="*70)
print("DETAILED METRICS (All Models)")
print("="*70)

all_models = {**balanced_models, **unbalanced_models}
detailed_metrics = get_detailed_metrics(all_models, X_scaled, y, CV_STRATIFIED)
detailed_metrics = detailed_metrics.sort_values('F1 Score', ascending=False)

print(detailed_metrics.to_string(index=False))

# Save results
detailed_metrics.to_csv('model_comparison_metrics.csv', index=False)
print("\nResults saved to 'model_comparison_metrics.csv'")

# =============================================================================
# 9. Top Model Training and Evaluation
# =============================================================================

print("\n" + "="*70)
print("TOP 3 MODELS - TRAIN/TEST SPLIT EVALUATION")
print("="*70)

test_df = pd.read_csv('../data/test_with_clusters.csv')
# Separate features and target
X_test = test_df.drop('stroke_event')
y_test = test_df['stroke_event']

# Apply same preprocessing
for col in NUMERICAL_COLS:
    if col in X_test.columns:
        X_test[col] = scaler.transform(X_test[[col]])

for col in CATEGORICAL_COLS:
    if col in X_test.columns:
        X_test[col] = le_dict[col].transform(X_test[col].astype(str))

top_models = results_combined.head(3)['model_name'].tolist()

for rank, model_name in enumerate(top_models, 1):
    print(f"\n{'='*60}")
    print(f"Rank {rank}: {model_name}")
    print(f"{'='*60}")
    
    model = all_models[model_name]
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
    
    print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Balanced Accuracy: {balanced_accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")
    if y_pred_proba is not None:
        print(f"ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    print(f"\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# =============================================================================
# 10. Summary
# =============================================================================

print("\n" + "="*70)
print("SUMMARY")
print("="*70)

best_model = results_combined.iloc[0]['model_name']
best_score = results_combined.iloc[0]['mean_score']

print(f"\nBest Model: {best_model}")
print(f"Best F1 Score (CV): {best_score:.4f}")
print(f"\nNumber of models compared: {len(results_combined)}")
print(f"Cross-validation folds: {CV_FOLDS}")

# print("\n" + "="*70)
# print("HOW TO EDIT THIS SCRIPT")
# print("="*70)
# print("""
# 1. To add a new model:
#    - Add to get_models_balanced() or get_models_unbalanced()
#    - Example:
#      'New Model': NewModelClassifier(params, class_weight='balanced', ...)

# 2. To change scoring metric:
#    - Edit the 'scoring' parameter in run_cv_comparison()
#    - Options: 'accuracy', 'f1', 'precision', 'recall', 'roc_auc'

# 3. To tune hyperparameters:
#    - Add GridSearchCV or RandomizedSearchCV for specific models
#    - Example provided below
# """)

# =============================================================================
# EXAMPLE: Hyperparameter Tuning (uncomment to use)
# =============================================================================

"""
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf_tuned = RandomizedSearchCV(
    RandomForestClassifier(class_weight='balanced', random_state=42),
    param_distributions=param_dist,
    n_iter=20,
    cv=CV_STRATIFIED,
    scoring='f1',
    random_state=42,
    n_jobs=-1
)

rf_tuned.fit(X_scaled, y)
print(f"Best RF params: {rf_tuned.best_params_}")
print(f"Best RF F1: {rf_tuned.best_score_:.4f}")
"""