# Text Mining and Search project

<center>Fabrizio Cominetti, 882737</center>
<center>Ruben Agazzi, 844736</center>
<br />

<center><img src="https://www.scienze.unimib.it/sites/sc02/files/scientifica_logo.png"></center>
<br />

Tasks to be accomplished:
- Text pre-processing (mandatory, task dependent)
- Text representation (choose suitable representation (s) and explain the rationale behind this choice)

Core tasks (please select two at your choice):
- Text classification;
- Text clustering.

Dataset:
- IMBD reviews

Evaluation:
- Provide suitable evaluation metrics, depending on the considered task.

---

## About

In this project, user reviews from the IMDB platform were analyzed through the use of text mining techniques. After carrying out an initial phase of text processing and text representation, the project continued with the classification of the reviews, through some text classification techniques - such as Support Vector Machines (SVM), Multilayer Perceptron (MLP), and Logistic Regression. Next, a text clustering phase was carried out through the use of two algorithms: DBSCAN and k-means.

## Repository Overview

```
├── README.md
├── data
├── figures
├── notebooks
├── report
├── slideshow
└── requirements.txt
```

## Installation & Usage

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](/data/raw/) within this repo, make sure to un-zip the raw data folder.
3. Data processing/transformation and all scripts are being kept [here](/notebooks/)
4. Run the notebook (see requirements.txt to install the necessary packages)