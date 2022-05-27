![](readme-assets/sof-2020-dev-survey.png?raw=true)

# 2020 Stack Overflow Developer Survey

## Table of Contents
0. [Installation](#install)
1. [Motivation & Project Description](#project_desc)
2. [File Descriptions](#file_desc)
3. [Licensing, Author, & Acknowledgements](#acknowl)


## 0. Installation <a id='install'></a>

Principle project code is contained in the Jupyter notebook 'stackoverflow'. The project was written in Python 3.9.7 and requires the following packages:
* Pandas, NumPy, sklearn, matplotlib, seaborn


## 1. Motivation & Project Description <a name="project_desc"></a>

In this repository, we use [Stack Overflow Annual Developer Survey data](https://insights.stackoverflow.com/survey)
to explore and contrast data and developer roles. Exploratory analyses includes information regarding compensation, job satisfaction, educational background, etc. Next, job satisfaction is explored for data roles and developer roles, and how satisfied
each group is in their jobs. Finally, two machine learning models, logistic regression and random forest classifiers, are used to identify
features that predict job satisfaction.

#### The Cross Industry Standard Process for Data Mining (CRISP-DM) for Job Satisfaction Prediction <a name="CRISP-DM"></a>
In particular, for the job satisfaction prediction, the procedure of [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) for data mining is adhered to.

#### - Business Problem  
We are interested in understanding job satisfaction of those working in data roles, and try to identify some important factors. This information is useful for students and other early career or career switching professionals interested in
entering what has recently become a much in demand skill set. This would be useful for career advisors in universities and career coaching professionals to update and improve their advising information set.

#### - Data Understanding  
The Stack Overflow Developer's Survey focuses on technology workers with a general developer background but includes related fields including data. The survey covers questions about personal background such as age, gender, education level, and job-related questions such as salary, work hours, job types, job satisfaction, etc. This project focuses on responders who identify as developers and those with data-related roles. Responses to job satisfaction questions are used to understand factors that contribute to job satisfaction. Exploratory data analysis is used to gain initial insight into each role as well as job satisfaction. Then modeling techniques are applied.

* Q1. Can we distinguish between data roles and developer roles?  
* Q2. How satisfied are data and developer roles with their jobs?
* Q3. Can predictors of job satisfaction be modeled through machine learning?

#### - Data Preparation  
To prepare the raw survey data for modeling, developer and data role response information is identified and extracted. Standard data preparation procedure have been used, including:

* select a subset of features interest
* missing data management
* appropriate feature preprocessing
* categorical data encoding

#### - Modeling  
Data is split into training and test set and trained using a logistic regression model and a random forest model. Linear modelling in a classification context consists of regression followed by a transformation to return a categorical output and thereby producing a decision boundary. A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.


## 2. File Descriptions  <a name="file_desc"></a>
In addition to project code contained in the notebook 'stackoverflow', support functions are found under the 'helper_functions' folder.


## 3. Licensing, Author, & Acknowledgements <a name="acknowl"></a>

This project was written by Andrew Nachtigal

Stack Overflow data was used in this project. Analysis or conclusions are the
work of the author.

The MIT license gives users express permission to reuse code for any purpose.

A medium post about the analyses results can be found [here](https://medium.com/@ajnacht/sof-2020-three-takeaways-abeb675c4454).
