#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Discussion, Conclusion and Future Work

== Discussion

The advanced analysis refined the modeling pipeline by incorporating feature selection, engineered variables, and cost-sensitive learning strategies tailored to the healthcare context. By removing redundant features such as high_glucose, bmi_category, and age_group, the study reduced multicollinearity and ensured that the models relied on the most informative and non-duplicative predictors. This step improved both model stability and interpretability.

Class imbalance remained a central challenge, and it was addressed using class weighting and scale adjustments rather than relying solely on resampling. This approach preserved the original data distribution while still making the models more sensitive to minority (stroke) cases.

A key improvement in this phase was the shift from default classification thresholds to threshold optimization using the F2 score. Unlike traditional metrics, the F2 score places greater emphasis on recall, reflecting the real-world cost of missing stroke cases. However, the results revealed an important trade-off: optimizing for F2 slightly reduced recall while improving precision. This indicates that while the models became more conservative in predicting stroke cases (reducing false positives), they still maintained a strong ability to identify true positives.

When comparing models, Logistic Regression and XGBoost with F2-optimized thresholds emerged as the most balanced options. They achieved a practical compromise between recall and precision, ensuring that stroke cases are detected at a reasonable rate without overwhelming the system with false alarms. In contrast, other models either over-predicted negatives or introduced too many false positives, making them less viable in a cost-sensitive healthcare setting.

== Conclusion

This enhanced analysis demonstrates that careful feature engineering, appropriate handling of class imbalance, and threshold optimization are critical for building effective predictive models in healthcare. Simply maximizing accuracy or recall is insufficient; instead, models must balance clinical relevance with operational feasibility.

The use of the F2 score aligned the modeling objective with the real-world priority of minimizing false negatives while still controlling false positives. Among the evaluated models, Logistic Regression and XGBoost (with optimized thresholds) provided the best overall performance, offering both strong detection capability and acceptable precision.

These findings highlight that relatively simpler models, when properly tuned and aligned with domain-specific objectives, can outperform more complex alternatives in practical applications.

== Future Work

Several improvements can further strengthen this work:

- Advanced Resampling Techniques: Incorporating methods such as SMOTE or hybrid sampling could be compared with class weighting to assess potential gains.
- Cost-Sensitive Learning: Explicitly defining and integrating misclassification costs into model training could better reflect real-world financial and clinical impacts.
- Model Interpretability: Applying explainability techniques (e.g., SHAP values) would help clinicians understand and trust model predictions.
- Threshold Customization by Use Case: Different thresholds could be set depending on clinical scenarios (e.g., screening vs. diagnosis) to optimize decision-making.
- External Validation: Testing the models on independent or real hospital datasets would improve confidence in generalizability.
- Integration into Clinical Systems: Future work could explore deployment within decision support tools, enabling real-time stroke risk assessment.


By addressing these areas, the predictive framework can be made more accurate, interpretable, and applicable in real-world healthcare scenarios.