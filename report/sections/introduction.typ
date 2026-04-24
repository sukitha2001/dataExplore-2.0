#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Introduction

== Background

Early identification of individuals at high risk for stroke enables timely intervention. Traditional risk assessment methods rely on clinical expertise and manual scoring systems, which may be subjective and limited in predictive capacity. 

This analysis tries to identify key risk factors associated with stroke events and develop a predictive model to predict the likelihood of a stroke. The dataset comprises 9,722 patient records with 18 variables.

== Methodology

The process began with a Data Cleaning phase. Here, the raw data was audited for duplicates that could skew results and missing values, particularly common in medical fields like BMI or smoking history, which were either removed or filled using statistical imputation. We also screened for anomalies or outliers, such as impossible physiological readings, to ensure the model wouldn't learn from "noisy" or incorrect data.

Once the data was cleaned, we moved into the Cluster Analysis to identify the different clusters of patients in the dataset. Following that, we moved into Exploratory Data Analysis (EDA). This involved visualizing distributions to understand the demographics of the patient population and using correlation matrices to see how variables like age, heart disease, and glucose levels interact. A key takeaway from this phase is often identifying class imbalance, as stroke events are typically much rarer than non-events in a general population, a factor that heavily influences how a model is trained.

To move beyond visual trends and into scientific certainty, we performed Statistical Testing. By applying methods such as Chi-Square tests for categorical variables and T-tests for continuous data, we were able to calculate p-values to determine if a correlation was statistically significant. This step filtered out the "noise," ensuring that only true clinical risk factors those with a mathematically proven link to stroke events were prioritized for the final model.

Finally, we synthesized these insights into a Predictive Model, transforming historical data into a forecasting tool. By selecting an appropriate algorithm, such as Logistic Regression for its interpretability or a Random Forest for its ability to handle complex patterns, we trained the system to assign a probability score to new patients. The success of this model likely hinged on optimization metrics like sensitivity or AUC-ROC, ensuring the tool is sensitive enough to catch high-risk cases without an overwhelming number of false alarms.


== Dataset Description

The healthcare dataset contains patient information could be categorized into four main groups:

#figure(
  table(
    columns: (auto, 1fr),
    table.header(
      [*Category*], [*Variables*]
    ),
    [Demographic], [
      - age,
      - age_group,
      - gender,
      - marital_status,
      - employment_type,
      - residence
    ],
    [Clinical], [
      - has_hypertension,
      - has_heart_disease,
      - glucose_level,
      - high_glucose,
      - bmi_value,
      - bmi_category,
      - smoking_habit,
      - lifestyle_risk
    ],
    [Derived], [
      - risk_score
    ],
    align: (start, start),
  ),
  caption: [Information Types],
) <tab:info-types>

The dataset contains variables of different types, continuous and categorical. And the categorical variables can be divided as nominal and ordinal.

#figure(
  table(
    columns: (auto, 1fr),
    table.header(
      [*Category*], [*Variables*]
    ),
    [Numerical], [
      - age,
      - glucose_level,
      - bmi_value,
      - risk_score
    ],
    [Ordinal], [
      - age_group,
      - bmi_category,
      - lifestyle_risk
    ],
    [Nominal], [
      - gender,
      - has_hypertension,
      - has_heart_disease,
      - marital_status,
      - employment_type,
      - residence,
      - high_glucose,
      - smoking_habit
    ],
    align: (start, start),
  ),
  caption: [Variable Classification],
) <tab:variable-classification>


== Dataset Cleaning

The dataset contained a lot of missing values and duplicates. Initially, we had to drop the duplicate rows which was around 4612 rows leaveing us with 5110 rows. 

Next we looked for missing values in the dataset. We found that there were 201 missing values in the `bmi_value` column. Since just dropping these missing values as well would reduce our dataset significantly, we chose to impute it. To maintian a testset that was representative of the original dataset and to prevent data leakage, we performed stratified sampling to split the dataset into training and testing sets prior to any calculations pertaining to the imputation of missing values. 

Looking at the distribution of the `bmi_value` column, we found that it was almost normally distributed. 

#figure(
  image(
    "../exports/bmi-hist.svg",
    width: 50%
  ),
  caption: [BMI Distribution],
) <tab:bmi-distribution>

Therefore, we chose to impute the missing values with the mean of the `bmi_value`. On top of that we noticed that there were no missing values in the `bmi_category` column and that each `bmi_category` was approximately normally distributed. Therefore imputing the missing values with the mean `bmi_value` of each `bmi_category` was a valid approach.



#figure(
  image(
    "../exports/bmi-kde.svg",
    width: 50%
  ),
  caption: [BMI KDE plot seperated by categories],
) <tab:bmi-distribution>


