#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Data Analysis

== Descriptive Statistics

=== Numerical Variables

#figure(
  table(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto),
    table.header(
      [*Variable*], [*Mean*], [*Std Dev*], [*Min*], [*25%*], [*50%*], [*75%*], [*Max*]
    ),
    [age], [54.73], [22.41], [0.08], [35], [55], [74], [82],
    [glucose_level], [127.85], [33.68], [60], [100], [118], [150], [300],
    [bmi_value], [27.66], [6.11], [10], [23], [27], [31], [55],
    [risk_score], [0.30], [0.53], [0], [0], [0], [1], [2],
  ),
  caption: [Summary Statistics for Numerical Variables],
) <tab:numerical-summary>

Age shows mean of approximately 55 years with considerable variation (SD = 22.41). Glucose levels average 127.85 mg/dL with right-skewed distribution. BMI values average 27.66, placing patients in overweight category. Risk score is predominantly low (median = 0).

=== Categorical Variables

#figure(
  table(
    columns: (auto, auto, auto, auto),
    table.header(
      [*Variable*], [*Category*], [*Count*], [*Percentage*]
    ),
    [gender], [F], [5,627], [57.9%],
    [], [M], [4,095], [42.1%],
    [age_group], [senior], [4,747], [48.8%],
    [], [middle], [3,418], [35.2%],
    [], [young], [1,557], [16.0%],
    [has_hypertension], [No], [7,945], [81.7%],
    [], [Yes], [1,777], [18.3%],
    [has_heart_disease], [No], [8,597], [88.4%],
    [], [Yes], [1,125], [11.6%],
    [marital_status], [Married], [7,413], [76.2%],
    [], [Not Married], [2,309], [23.8%],
    [employment_type], [Working], [7,693], [79.1%],
    [], [Government], [1,278], [13.1%],
    [], [Other], [751], [7.7%],
    [residence], [Urban], [5,107], [52.5%],
    [], [Rural], [4,615], [47.5%],
    [high_glucose], [No], [7,126], [73.3%],
    [], [Yes], [2,596], [26.7%],
    [bmi_category], [Obese], [4,654], [47.9%],
    [], [Overweight], [2,820], [29.0%],
    [], [Normal], [1,893], [19.5%],
    [], [Underweight], [355], [3.7%],
    [smoking_habit], [Non-smoker], [3,560], [36.6%],
    [], [Unknown], [2,395], [24.6%],
    [], [Ex-smoker], [2,179], [22.4%],
    [], [Current smoker], [1,588], [16.3%],
    [lifestyle_risk], [Low], [6,736], [69.3%],
    [], [Medium], [2,179], [22.4%],
    [], [High], [807], [8.3%],
  ),
  caption: [Distribution of Categorical Variables],
) <tab:categorical-distribution>

Majority are female (57.9%), seniors (48.8%), married (76.2%), working (79.1%). Nearly half are obese (47.9%), 18% have hypertension, 12% have heart disease.

== Visual Analysis

=== Numerical Variables vs Stroke Event

Box plots reveal:
- Age: Stroke patients show higher median age
- Glucose Level: Higher median in stroke group
- BMI: Similar distributions between groups
- Risk Score: Higher values in stroke group

=== Categorical Variables vs Stroke Event

Stacked bar charts show:
- Age Group: Senior patients have dramatically higher stroke rates
- Hypertension: Higher stroke rates in hypertensive patients
- Heart Disease: Elevated stroke rates in patients with heart disease
- High Glucose: Increased stroke occurrence with elevated glucose
- BMI Category: Higher BMI shows elevated stroke rates
- Lifestyle Risk: Higher risk correlates with higher stroke rates

== Statistical Testing Results

=== Parametric Tests

#figure(
  table(
    columns: (auto, auto, auto, auto, auto),
    table.header(
      [*Variable*], [*Chi-Square*], [*DOF*], [*p-value*], [*Significance*]
    ),
    [age_group], [2786.98], [2], [0.000], [Significant],
    [marital_status], [745.95], [1], [0.000], [Significant],
    [high_glucose], [681.79], [1], [0.000], [Significant],
    [employment_type], [638.10], [2], [0.000], [Significant],
    [has_hypertension], [572.75], [1], [0.000], [Significant],
    [bmi_category], [537.46], [3], [0.000], [Significant],
    [has_heart_disease], [445.87], [1], [0.000], [Significant],
    [smoking_habit], [294.24], [3], [0.000], [Significant],
    [lifestyle_risk], [205.37], [2], [0.000], [Significant],
    [residence], [13.97], [1], [0.000], [Significant],
    [gender], [2.70], [1], [0.100], [NS],
  ),
  caption: [Chi-Square Test Results],
) <tab:chi-square-results>

Chi-Square: 10/11 categorical variables significant (p < 0.05), only gender not significant.

#figure(
  table(
    columns: (auto, auto, auto, auto),
    table.header(
      [*Variable*], [*F-Statistic*], [*p-value*], [*Significance*]
    ),
    [age], [4906.30], [0.000], [Significant],
    [risk_score], [1025.01], [0.000], [Significant],
    [glucose_level], [682.70], [0.000], [Significant],
    [bmi_value], [NaN], [NaN], [-],
  ),
  caption: [ANOVA Results],
) <tab:anova-results>

ANOVA: Age, risk_score, glucose_level significant (p < 0.001).

=== Non-Parametric Tests

#figure(
  table(
    columns: (auto, auto, auto, auto),
    table.header(
      [*Variable*], [*Odds Ratio*], [*p-value*], [*Significance*]
    ),
    [marital_status], [4.06], [0.000], [Significant],
    [high_glucose], [3.54], [0.000], [Significant],
    [has_hypertension], [3.92], [0.000], [Significant],
    [has_heart_disease], [4.57], [0.000], [Significant],
    [residence], [1.16], [0.000], [Significant],
    [gender], [1.07], [0.100], [NS],
  ),
  caption: [Fisher's Exact Test Results],
) <tab:fisher-results>

Fisher's Exact: Confirms Chi-Square findings. Heart disease shows highest OR (4.57).

#figure(
  table(
    columns: (auto, auto, auto, auto),
    table.header(
      [*Variable*], [*H-Statistic*], [*p-value*], [*Significance*]
    ),
    [age], [3284.18], [0.000], [Significant],
    [risk_score], [978.61], [0.000], [Significant],
    [glucose_level], [366.46], [0.000], [Significant],
  ),
  caption: [Kruskal-Wallis Results],
) <tab:kw-results>

Kruskal-Wallis: Confirms ANOVA results.

== Summary of Significant Variables

10 categorical and 3 numerical variables show significant associations with stroke events across both parametric and non-parametric tests.
