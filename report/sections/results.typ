#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Advance Data Analysis

== Feature Selection and Engineering

The encoded dataset contained 19 variables including the variables we derived from the original dataset such as bmi_was_missing. To reduce multicollinearity redundant variables were dropped from the model.

- High_glucose - Derived from glucose_level
- Bmi_category - Derived from bmi_value
- Age_group -Derived from age
- Lifestyle_risk
- Bmi_was_missing - Derived from bmi_value

The class imbalance ratio was calculated and used as scale_pos_weight for XGBoost and for Logistic Regression and Random Forest balanced class weights were used.

== Model Training and Hyperparameter Tuning

Data were scaled using standard scalar and hyperparameters tuning were done by RandomizedSearchCV with 5 fold stratified K-Fold crossvalidation.

== Threshold optimisation using F2 score

The default threshold is 0.5 for all three models, since our target variable is highly imbalanced and we are fitting this data to stroke patient data, False negatives can be costly for the patient. Therefore we have used an F2 score which penalizes false negatives and rewards true positives. In layman terms this means higher the F2 score better the model.

$ "F2 score" = 5 * ("precision" * "recall") / (4 * "precision" + "recall") $

#pagebreak()

== Evaluation Metrics

#figure(
  image("../exports/model-comparison.png", width: 100%),
  caption: [Model Comparison]
)

Across all three models when we switch to the F2-optimal threshold, recall has been reduced while precision is slightly improved. This is crucial because a low precision score leads to an increase in false positives, even if higher recall results in more true positives. Such an outcome might discourage stakeholders from adopting the model, as the financial burden associated with false positives could be significant. From our evaluation metrics we can conclude that Logistic Regression with F2-optimal threshold and XGBoost with F2-optimal threshold are the better suited models since they have good recall and moderate precision giving high true positive and comparatively low false positives. Which indicates those two are financially feasible compared to other models.