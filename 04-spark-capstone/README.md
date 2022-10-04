# Customer Churn Prediction Project

Sparkify is a digital music service similar to Spotify or Pandora. Many users stream the songs from the
service every day either using the free tier that place advertisements between the songs or using the premium
subscription model, where they stream music with no advertisements but paying a monthly fee rate. Users can upgrade,
downgrade or cancel their service at any time, so it is important that the users love the service.

Every time the user interacts with the service while they are playing songs, logging out, liking in a song or
downgrading the service, it generates data. The purpose of this project is to use this data generated to predict
which users are at risk to churn deleting their accounts since this can potentially save the company considerable
money in revenues.


### Table of Contents  
1. [Project Motivation](#project-motivation)
2. [Requirements](#requirements)
3. [Libraries used](#libraries)
4. [File Descriptions](#file-descriptions)
4. [Project Steps](#project-steps)
5. [Authors](#authors)
6. [Acknowledgements](#acknowledgements)


1. <a href = "#Requirements" > Requirements </a>
2. <a href = "#Jupyter-Notebook"> Jupyter Notebook </a>
3. <a href = "#Data" > Data </a>
4. <a href = "#Summary-of-Results" > Summary of Results </a>
5. <a href = "#Article-of-the-Project" > Article of the Project </a>
6. <a href = "#Acknowledgements" > Acknowledgements </a>

## Project Motivation <a name="project-motivation"></a>

## Requirements <a name="requirements"></a>
The following libraries are needed to run the notebook:
+ numpy
+ pandas
+ time
+ datetime
+ matplotlib
+ seaborn
+ pyspark


## File Descriptions <a name="file-descriptions"></a>

## Jupyter Notebook
Here will be done the analysis and develop of the machine learning models to predict the churn
of the users in the service

- `Sparkify.ipynb`: exploratory data analysis, data preprocessing, and pilot development of machine learning model on local machine using data subset from [Udacity]().
- `mini_sparkify_event_data.json`: subset of user activity data. (not uploaded due to data quota limit)


## Data
This is the data that will be used for the analysis and training of the model:

+ [(```mini_sparkify_event_data.json.zip```)](mini_sparkify_event_data.json.zip): dataset with the data collected in
the service

## Summary of Results

After training 5 different models, the accuracy and f1 score obtained for each one is displayed in the following
table:

| Model name | Accuracy | f1score | Training time (min:sec)|
| :---: | :---: | :---: | :---: |
| Random Forest | 0.800000 | 0.736508 | 04:34.036536|
| Logistic Regression | 0.885714 | 0.860829 | 04:08.942884 |
| Decision Tree | 0.800000 | 0.805938 | 04:47.750021 |
| Gradient Boosted Trees | 0.685714 | 0.717108 | 04:24.014526|
| LinearSVC | 0.828571 | 0.750893 | 04:04.784299 |

<br />

A comparison of these results can be seen in the following pictures:

![Accuracy](https://github.com/pedflotor/Sparkify-Churn-Prediction/blob/master/images/Accuracy.png)
![f1score](https://github.com/pedflotor/Sparkify-Churn-Prediction/blob/master/images/f1score.png)

<br />

The model with the best result is *Logistic Regresion* with an accuracy of 0.885 and a f1 score of 0.861. The features
that have more impact are registration_min, errors, friend, played_time_session, avg_songs_session and thumbs_down as
the picture below depicts.

![coeff](https://github.com/pedflotor/Sparkify-Churn-Prediction/blob/master/images/coeff.png)

From them, the higher the value of these features are, most likely the user will stay in the service and will not churn.

<br />

In order to improve the model in the future it would be good to try with a bigger dataset where the models have more
data to learn from and use more parameters in Grid Search to tune the models


## Article of the Project
+ https://petanth91.medium.com/churn-prediction-in-sparkify-a-digital-music-service-26aa8640bffb?sk=94e1836865a2fcc1cae7c37ab9495aa4

## Acknowledgements
+ https://spark.apache.org/docs/latest/ml-classification-regression.html
+ https://spark.apache.org/docs/latest/ml-tuning.html  
+ https://www.displayr.com/how-to-interpret-logistic-regression-coefficients/
+ https://www.udacity.com/course/learn-spark-at-udacity--ud2002
