import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import styling

num_cols = ["age", "glucose_level", "bmi_value", "risk_score"]
cat_cols = ["gender", "age_group", "has_hypertension", "has_heart_disease", "marital_status", "employment_type", "residence", "high_glucose", "bmi_category", "smoking_habit", "lifestyle_risk"]
ordinal_cats = ["age_group", "bmi_category", "lifestyle_risk"]
nominal_cats = [col for col in cat_cols if col not in ordinal_cats]

target = "stroke_event"
df = pd.read_csv("../data/recoded_train.csv")

os.makedirs("../report/exports", exist_ok=True)

for col in num_cols:
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.boxplot(data=df, x=target, y=col, hue=target, ax=ax)
    # ax.set_title(f"{col} vs {target}")
    ax.set_xlabel(target)
    ax.set_ylabel(col)
    plt.tight_layout()
    styling.style_ax(ax)
    # styling.style_legend(ax)
    styling.save_figure(fig, save_path="../report/exports", filename=f"{col.replace('_', '-').lower()}_vs_{target.replace('_', '-').lower()}_boxplot")
    plt.close()

for col in cat_cols:
    fig, ax = plt.subplots(figsize=(10, 10))
    ct = pd.crosstab(df[target], df[col], normalize="index") * 100
    ct.plot(kind="bar",stacked=True, ax=ax)
    # ax.set_title(f"{col} vs {target}")
    ax.set_ylabel("Percentage")
    ax.set_xlabel(target)
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    styling.style_ax(ax)
    styling.style_legend(ax)
    styling.save_figure(fig, save_path="../report/exports", filename=f"{target.replace('_', '-').lower()}_vs_{col.replace('_', '-').lower()}_stacked_bar")
    plt.close()

print("Plots saved to ../report/exports")