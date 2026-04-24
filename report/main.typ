/* Imports: */
// Note: these imports need to repeated for every file used in the document.

// Main import of the template
// This import contains the wrap-it and equate packages by default.
#import "@preview/classy-tudelft-thesis:0.1.0": *
#set text(font: "Times New Roman")


// Main styling, containg the majority of typesetting including document layout, fonts, heading styling, figure styling, outline styling, etc. Some parts of the styling are customizable.
#show: base.with(
  // These first two parameters are only used for the pdf metadata.
  title: "Predicting Stroke Risk Using Patient Health and Lifestyle Data",
  name: "",
  // What is displayed at the top-right of the page. The top-left of the page displays the current chapter.
  rightheader: "Ctrl Freaks",
//   // Main and math fonts
  // main-font: "New York",
//   // math-font: "New York",
//   // Colors used for internal references (figures, equations, sections) and citations
//   ref-color: olive,
//   cite-color: blue,
//   // Language, used for correct hyphenation patterns and default word for outline title, etc.
//   language: "en",
//   region: "GB",
)


/* Title page */

// #maketitlepage(
//   // These first arguments are self-explanatory
//   title: [Predicting Stroke Risk],
//   subtitle: [Using Patient Health and Lifestyle Data],
//   name : "",
//   defense-date: none,
//   // These following arguments appear in a small table below the main title, subtitle, author
//   student-number: none,
//   project-duration: none,
//   daily-supervisor: none,
//   // The thesis committee should be an array of contents, consisting of all the committee members and their affiliations
//   thesis-committee: none,
//   cover-description: none,
//   publicity-statement: none,
// )

/* Remaining contents of front matter */

// #heading(numbering: none, [Preface])

// // Your preface here
// // #lorem(250)



#heading(numbering: none, [Contributions])

#table(
  columns: (auto, 1fr),
  table.header(
    [*Member*], [*Contributions*]
  ),
  [Vidura Gunawardana], [
    - EDA Plotting
    - Plot Styling
    - Statistical Testing
    - Cluster Analysis
    - Report Writing
  ],
  [Sukitha Rathnayake], [
    - Data Preprocessing
    - Feature Engineering
    - Model Training
    - Model Evaluation
  ],
  [Prabhavi Hemachandra], [
    - Model Training
    - Model Evaluation
    - Report Writing
  ],
  align: (start, start),
)

// Your Abstract here
// #lorem(250)


#outline()
#outline(title: "Figures", target: figure.where(kind: image))
#outline(title: "Tables", target: figure.where(kind: table))


// After the front matter is complete, we switch page numbering from roman to arabic numbering, and restart counting. The next chapter created afterwards starts on page 1.

#show: switch-page-numbering

// #include "./sections/0default-template.typ" // Comment out this line when you start writing
#include "./sections/introduction.typ"
#include "./sections/cluster.typ"
#include "./sections/eda.typ"
#include "./sections/results.typ"
#include "./sections/conclusion.typ"


// #bibliography(
//   "references.bib",
//   title: [References],
//   style: "american-physics-society",
// )


// #show: appendix

// #include "./sections/6appendix.typ"
