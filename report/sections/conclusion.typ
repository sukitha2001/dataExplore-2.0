#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"

= Discussion, Conclusion and Future Work

== Discussion

=== Key Findings

1. Age is the strongest predictor (Chi Square = 2786.98, F = 4906.30), consistent with known epidemiology where stroke risk doubles each decade after age 55.

2. Cardiovascular comorbidities show strong associations:
   - Hypertension: OR = 3.92 (approximately 4x higher odds)
   - Heart disease: OR = 4.57 (highest odds ratio)
   - High glucose: OR = 3.54

3. Lifestyle factors (smoking, lifestyle risk score) show significant associations with stroke events.

4. Gender shows no significant association, suggesting stroke risk may be more influenced by other factors.

=== Interpretation

The consistency between parametric and non-parametric tests strengthens validity. Effect sizes provide clinically meaningful insights:
- Heart disease: 4.57x odds
- Hypertension: 3.92x odds
- High glucose: 3.54x odds

The marital status association (OR = 4.06) is likely confounded by age and requires careful interpretation.

=== Clinical Implications

1. Targeted screening: Prioritize patients with hypertension, heart disease, elevated glucose, and advanced age
2. Preventive interventions: Focus on modifiable risk factors
3. Resource allocation: Direct prevention efforts toward high-risk populations

=== Limitations

1. Balanced dataset may affect generalizability to real-world populations
2. BMI value shows NaN results indicating data quality issues
3. Cross-sectional design limits causal inference
4. Missing important variables: alcohol consumption, physical activity, family history

== Conclusion

This comprehensive analysis has identified key variables associated with stroke events. Stroke risk is multifactorial, with age, cardiovascular comorbidities, metabolic indicators, and lifestyle factors as primary predictors.

The identification of 10 significant categorical and 3 significant numerical predictors provides a foundation for developing predictive models. Strong statistical significance (p < 0.001) suggests these factors should be central to any stroke risk prediction framework.

From a public health perspective, this analysis reinforces:
- Regular blood pressure monitoring and hypertension management
- Glucose level screening and diabetes prevention
- Lifestyle modification programs
- Targeted screening for older adults

== Future Work

1. Predictive model development using machine learning algorithms
2. Validation in independent datasets
3. Investigation of interaction effects between risk factors
4. Improvement of data quality
5. Collection of additional risk factors
6. Development of risk stratification protocols
