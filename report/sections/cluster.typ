#import "@preview/classy-tudelft-thesis:0.1.0": *
#import "@preview/physica:0.9.6": *
#import "@preview/unify:0.7.1": num, numrange, qty, qtyrange
#import "@preview/zero:0.5.0"


= Cluster Analysis

Since the dataset contained both numeric and categorical type variables, a Principle Component Analysis would be inaccurate. Therefore, we performed a  Factor Analysis for Mixed Data. 


#figure(
  image(
    "../exports/famd.png",
    width: 100%
  ),
  caption: [FAMD Loadings],
) <fig:famd-loadings>

By Looking at the loadings we can derive the following factors:

#figure(
  table(
    columns: (auto, 1fr),
    table.header(
      [*Factor*], [*Variables*]
    ),
    [Experience], [
      - age,
      - age_group,
      - employment_type,
    ],
    [Risk Factor], [
      - smoking_habit,
      - lifestyle_risk
    ],
    align: (start, start),
  ),
  caption: [FAMD Factors],
) <tab:famd-factors>

Next by using the K-Means algorithm we were able to identify 4 distinct clusters in the dataset. Averaging with a Silhouette Score of 0.56.

#let silhouette_plot = figure(
  image(
    "../exports/silhouette.svg",
    width: 100%
  ),
  caption: [Silhouette Score Plot],
) 

#let cluster_plot = figure(
  image(
    "../exports/clusters.svg",
    width: 100%
  ),
  caption: [Cluster Analysis],
) 
  

#grid(
  columns: (1fr, 1fr),
  rows: (auto, auto),
  gutter: 3pt,
  silhouette_plot,
  cluster_plot,
)
  