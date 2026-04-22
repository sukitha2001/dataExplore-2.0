import pandas as pd
import numpy as np
from scipy import stats
import os

num_cols = ["age", "glucose_level", "bmi_value", "risk_score"]
cat_cols = ["gender", "age_group", "has_hypertension", "has_heart_disease", "marital_status", "employment_type", "residence", "high_glucose", "bmi_category", "smoking_habit", "lifestyle_risk"]

target = "stroke_event"
df = pd.read_csv("../data/recoded_train.csv")

print("=" * 60)
print("PARAMETRIC TESTS: Chi-Square & ANOVA")
print("=" * 60)

print("\n### CHI-SQUARE TEST (Categorical vs Target) ###")
chi_results = []
for col in cat_cols:
    ct = pd.crosstab(df[col], df[target])
    chi2, p, dof, expected = stats.chi2_contingency(ct)
    chi_results.append({"Variable": col, "Chi2": chi2.round(2), "p-value": p.round(2), "DOF": dof})

chi_df = pd.DataFrame(chi_results).sort_values("p-value")
print(chi_df.to_string(index=False))

print("\n### ANOVA (Numerical vs Target) ###")
anova_results = []
for col in num_cols:
    group0 = df[df[target] == 0][col]
    group1 = df[df[target] == 1][col]
    f_stat, p = stats.f_oneway(group0, group1)
    anova_results.append({"Variable": col, "F-stat": f_stat.round(2), "p-value": p.round(2)})

anova_df = pd.DataFrame(anova_results).sort_values("p-value")
print(anova_df.to_string(index=False))

print("\n" + "=" * 60)
print("NON-PARAMETRIC TESTS: Fisher's Exact & Kruskal-Wallis")
print("=" * 60)

print("\n### FISHER'S EXACT TEST (Categorical vs Target) ###")
fish_results = []
for col in cat_cols:
    ct = pd.crosstab(df[col], df[target])
    oddsr, p = stats.fisher_exact(ct)
    fish_results.append({"Variable": col, "Odds Ratio": oddsr.round(2), "p-value": p.round(2)})

fish_df = pd.DataFrame(fish_results).sort_values("p-value")
print(fish_df.to_string(index=False))

print("\n### KRUSKAL-WALLIS TEST (Numerical vs Target) ###")
kw_results = []
for col in num_cols:
    group0 = df[df[target] == 0][col]
    group1 = df[df[target] == 1][col]
    h_stat, p = stats.kruskal(group0, group1)
    kw_results.append({"Variable": col, "H-stat": h_stat.round(2), "p-value": p.round(2)})

kw_df = pd.DataFrame(kw_results).sort_values("p-value")
print(kw_df.to_string(index=False))

sig_level = 0.05
print("\n" + "=" * 60)
print(f"SIGNIFICANT VARIABLES (p < {sig_level})")
print("=" * 60)

print("\nCategorical (Chi-square):")
sig_cat = chi_df[chi_df["p-value"] < sig_level]["Variable"].tolist()
print(f"  {sig_cat if sig_cat else 'None'}")

print("\nNumerical (ANOVA):")
sig_num = anova_df[anova_df["p-value"] < sig_level]["Variable"].tolist()
print(f"  {sig_num if sig_num else 'None'}")

# os.makedirs("../exports/results", exist_ok=True)
# chi_df.to_csv("../exports/results/chi_square_test.csv", index=False)
# anova_df.to_csv("../exports/results/anova_test.csv", index=False)
# fish_df.to_csv("../exports/results/fisher_exact_test.csv", index=False)
# kw_df.to_csv("../exports/results/kruskal_wallis_test.csv", index=False)

# print("\nResults saved to ../exports/results/")