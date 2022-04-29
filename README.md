![](readme-assets/udacity-logo.png?raw=true)

# Udacity-Data-Science
nanodegree project repository

* Software Engineering
* Data Engineering
* Experimental Design & Recommendations
* Capstone

## Table of Contents
1. [Project Description](#project_desc)
2. [CRISP-DM For Job Satisfaction Prediction](#CRISP-DM)
3. [File Structure](#fileStructure)
4. [Requirements](#requirements)
5. [Acknowledgements](#ack)

### 1. Project Description <a name="project_desc"></a>
In this repository, we use [Stack Overflow Annual Developer Survey data](https://insights.stackoverflow.com/survey)
to do some exploratory analyses of data jobs (Data Scientist, Data Analyst, Data Engineer).
Analyses include facts on salary, job satisfaction, change of the data jobs (2019 v.s. 2020).
Machine learning modelling has also been used to predict job satisfaction.

A medium post about the analyses results can be found [here](https://lcxustc.medium.com/salary-satisfaction-trend-of-data-jobs-f47bdf72afa3).

### 2. CRISP-DM For Job Satisfaction Prediction <a name="CRISP-DM"></a>
In particular, for the job satisfaction prediction, the procedure of [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) for data mining has been applied.
#### - Business Problem
We are interested in understanding job satisfaction for data jobs, and try to identify some important factors. This
 may be useful, as example, for a Career Advice & Coach Company to better plan career development for their
  customers, such as job seekers to switch to the data field or data professionals to make the next step in their
   career path.

#### - Data Understanding
The Stack Overflow Survey Data is a questionnaire designed for people with general developer background. It
 covers questions about personal background such as age, gender, education level, and job-related questions such as
  salary, work hours, job types, job satisfaction, etc. We focus on responders who have a data-related jobs and use the
   responses to job satisfaction as the entry point to understand what contribute to job satisfaction. Exploratory
    data analysis has been applied to get some preliminary insight into job satisfaction. Then modelling technique is applied.

#### - Data Preparation
To prepare the raw survey data for modelling purpose, we need to first extract responses that are associated with data-related jobs. Standard data preparation procedure has been applied, mainly including:

* select the subset of data of interest and transform raw data properly;
* feature selection;
* missing data imputation;
* categorical data encoding.
