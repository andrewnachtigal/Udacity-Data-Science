![](readme-assets/sof-2020-dev-survey.png?raw=true)

# 2020 Stack Overflow Developer Survey

## Table of Contents
1. [Project Description](#project_desc)
2. [CRISP-DM For Job Satisfaction Prediction](#CRISP-DM)
3. [File Structure](#fileStructure)
4. [Requirements](#requirements)
5. [Acknowledgements](#ack)

### 1. Project Description <a name="project_desc"></a>
In this repository, we use [Stack Overflow Annual Developer Survey data](https://insights.stackoverflow.com/survey)
to explore and contrast data and developer roles. Exploratory analyses includes information regarding compensation, job satisfaction, educational background, etc.

Machine learning modeling is used to predict job satisfaction.

A medium post about the analyses results can be found [here](https://lcxustc.medium.com/salary-satisfaction-trend-of-data-jobs-f47bdf72afa3).

### 2. The Cross Industry Standard Process for Data Mining (CRISP-DM) for Job Satisfaction Prediction <a name="CRISP-DM"></a>
In particular, for the job satisfaction prediction, the procedure of [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) for data mining is adhered to.

CRISP-DM steps revolve around data:

1. Business Understanding - What does the business need?
2. Data Understanding – What data is available and what is needed? Is the data clean?
3. Data Preparation - How should the data be organized for modeling?
4. Modeling - What modeling techniques should be applied?
5. Evaluate and iterate - Which model best meets the business objectives?
6. Model deployment - How do stakeholders access the results?


#### - Business Problem
We are interested in understanding job satisfaction of those working in data roles, and try to identify some important factors. This information is useful for students and other early career or career switching professionals interested in
entering what has recently become a much in demand skill set. This would be useful for career advisors in universities and career coaching professionals to update and improve their advising information set.


#### - Data Understanding
The Stack Overflow Developer's Survey



\is a questionnaire designed for people with general developer background. It
 covers questions about personal background such as age, gender, education level, and job-related questions such as
  salary, work hours, job types, job satisfaction, etc. We focus on responders who have a data-related jobs and use the
   responses to job satisfaction as the entry point to understand what contribute to job satisfaction. Exploratory
    data analysis has been applied to get some preliminary insight into job satisfaction. Then modelling technique is applied.

#### - Data Preparation
To prepare the raw survey data for modeling, we need to first extract information from respondents employed in data related roles. Standard data preparation procedure has been applied, mainly including:

* select the subset of data of interest and transform raw data properly
* feature selection
* missing data imputation
* categorical data encoding.

There are 10,372 data instances and 38 features after data preparation (54 feature columns after one-hot encoding).

#### - Modelling
There are five possible responses to job satisfaction, so it is a multi-classification problem. Data has been split
into training and test set. An untuned Gaussian Naive Bayes has been tried as a baseline model. And then grid search with cross-validation technique is applied to tune XGBoost model. Average ROC-AUC score has been used as the main metric for hyperparameter tuning and model performance evaluation, while other metrics such as Log-Loss, Accuracy, average Precision (macro), average Recall (macro) and Confusion Matrix have been used together to give a comprehensive evaluation of the model performance.

#### - Evaluation
A set of metrics have been used to evaluate the model performance. Although there exist the overfitting issue to
some extent, the model performance is considered acceptable and the model has a reasonable predictive power. We also applied some explainability technique (e..g, [SHAP](https://github.com/slundberg/shap)) to get more insight of the modelling result, such as key drivers (e.g., Salary, OnboardExperience, Age, YearsCode, CompanySize) and dependence relationship w.r.t. predicting job satisfaction.

#### - Deployment
This project doesn't cover the deployment part, but with the trained model, one can productionize it, such as
integrating it into an App, and score new data instance.

### 3. Acknowledgements <a name="ack"></a>
Stack Overflow data was used in this project. Analysis or conclusions are the
work of the author.
