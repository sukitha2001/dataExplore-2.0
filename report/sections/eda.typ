#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Exploratory Data Analysis

== Visual Analysis

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

#let stroke_smoking_plot = figure(
  image(
    "../exports/stroke-event_vs_smoking-habit_stacked_bar.svg",
    width: 100%
  ),
  caption: [Stroke Event vs Smoking Habit],
) 

#let stroke_glucose_level_plot = figure(
  image(
    "../exports/glucose-level_vs_stroke-event_boxplot.svg",
    width: 100%
  ),
  caption: [Stroke Event vs Glucose Level],
) 

#let stroke_risk_score_plot = figure(
  image(
    "../exports/risk-score_vs_stroke-event_boxplot.svg",
    width: 100%
  ),
  caption: [Stroke Event vs Risk Score],
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

#grid(
  columns: (1fr, 1fr),
  rows: (auto, auto),
  gutter: 3pt,
  stroke_glucose_level_plot,
  stroke_risk_score_plot,
)

The 2 boxplots show that the glucose level and risk score are higher in the group with stroke events. This is expected as these are risk factors for stroke.

#figure(
  image(
    "../exports/corr.svg",
    width: 50%
  ),
  caption: [Correlation Heatmap],
) <fig:correlation-heatmap>

The heatmap shows the correlation between the numerical variables. We can see that there is a strong correlation between has_heart_disease, has_hypertension, high_glucose, risk_score and glucose_level suggesting that there is no multicollinearity and that there no hidden interactions between the variables.

#pagebreak()

== Statistical Tests

To confirm whether the observed differences are statistically significant, we performed a series of chi-squared tests for independance. The results are summarized below:

#figure(
  image(
    "../exports/chi_summary.png",
    width: 100%
  ),
  caption: [Chi-squared Test Summary],
) <fig:chi-squared-summary>
  
So now we can conclude that there is no statistically significant relationship between the stroke event and the variables residence, gender. The rest seem to have a relationship with the stroke event. Since these are possible to be non-linear relationships we won't be able to find them just using visualizations.

