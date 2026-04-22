#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Exploratory Data Analysis

== Variable distributions

#figure(
  image(
    "../exports/stroke-dist.svg",
    width: 50%
  ),
  caption: [Stroke Distribution],
) <fig:stroke-distribution>

This above count plot shows the significant imbalance in the target variable `stroke_event`. Which will be needed to address during the model training phase.


#let stroke_heart_disease_plot = figure(
  image(
    "../exports/stroke-event_vs_has-heart-disease_stacked_bar.svg",
    width: 100%
  ),
  caption: [Stroke Event vs Has Heart Disease],
) 

#let stroke_hypertension_plot = figure(
  image(
    "../exports/stroke-event_vs_has-hypertension_stacked_bar.svg",
    width: 100%
  ),
  caption: [Stroke Event vs Has Hypertension],
)

#let stroke_high_glucose_plot = figure(
  image(
    "../exports/stroke-event_vs_high-glucose_stacked_bar.svg",
    width: 100%
  ),
  caption: [Stroke Event vs High Glucose],
) 

#let stroke_risk_plot = figure(
  image(
    "../exports/stroke-event_vs_lifestyle-risk_stacked_bar.svg",
    width: 100%
  ),
  caption: [Stroke Event vs Lifestyle Risk],
) 




#grid(
  columns: (1fr, 1fr),
  rows: (auto, auto),
  gutter: 3pt,
  stroke_heart_disease_plot,
  stroke_hypertension_plot,
)

It can be seen that the proportions of the stroke events are significantly higher in the group with heart disease and hypertension.
This should be investigated using statistical tests to confirm that this is not some inherent bias due to the imbalance in the dataset.

#grid(
  columns: (1fr, 1fr),
  rows: (auto, auto),
  gutter: 3pt,
  stroke_high_glucose_plot,
  stroke_risk_plot,
)

The plots suggest that there is some relationship between the stroke event and high_glucose, lifestyle_risk, has_heart_disease, has_hypertension.


== Analytical Approach

The analysis follows a structured framework:

1. Exploratory Data Analysis (EDA): Examination of variable distributions
2. Visual Analysis: Boxplots and bar charts
3. Statistical Testing: Parametric and non-parametric tests

== Variable Classification

#figure(
  table(
    columns: (auto, auto),
    table.header(
      [*Category*], [*Variables*]
    ),
    [Numerical], [age, glucose_level, bmi_value, risk_score],
    [Categorical], [gender, age_group, has_hypertension, has_heart_disease, marital_status, employment_type, residence, high_glucose, bmi_category, smoking_habit, lifestyle_risk],
    [Ordinal], [age_group, bmi_category, lifestyle_risk],
    [Nominal], [gender, has_hypertension, has_heart_disease, marital_status, employment_type, residence, high_glucose, smoking_habit],
  ),
  caption: [Variable Classification],
) <tab:variable-classification>

== Statistical Methods

*Parametric Tests:*
- Chi-Square Test: Assesses association between categorical variables and stroke events
- ANOVA: Compares means of numerical variables across stroke event groups

*Non-Parametric Tests:*
- Fisher's Exact Test: Alternative to Chi-Square for categorical associations
- Kruskal-Wallis Test: Non-parametric alternative to ANOVA

Significance threshold: alpha = 0.05

== Visualization Style

Visualizations were generated using Matplotlib and Seaborn with custom publication-quality style including consistent font family, grid lines, and clean aesthetics.
