# Customer Churn Prediction Project


### Table of Contents  
1. [Project Motivation](#project-motivation)
2. [Requirements](#requirements)
3. [Libraries used](#libraries)
4. [File Descriptions](#file-descriptions)
5. [Project Steps](#project-steps)
6. [Project Results-Post](#project-results-post)
7. [Authors](#authors)
8. [Acknowledgements](#acknowledgements)



## Project Motivation <a name="project-motivation"></a>

Sparkify is a digital music service similar to Spotify or Pandora. Many users stream the songs from the
service every day either using the free tier that place advertisements between the songs or using the premium
subscription model, where they stream music with no advertisements but paying a monthly fee rate. Users can upgrade,
downgrade or cancel their service at any time, so it is important that the users love the service.

Every time the user interacts with the service while they are playing songs, logging out, liking in a song or
downgrading the service, it generates data. The purpose of this project is to use this data generated to predict
which users are at risk to churn deleting their accounts since this can potentially save the company considerable
money in revenues.


## Requirements <a name="requirements"></a>
The following libraries are needed to run the notebook:
* numpy
* pandas
* matplotlib
* seaborn
* pyspark


## File Descriptions <a name="file-descriptions"></a>

## Jupyter Notebook
Here will be done the analysis and develop of the machine learning models to predict the churn
of the users in the service

* `Sparkify.ipynb`: exploratory data analysis, data preprocessing, and pilot development of machine learning model on local machine using data subset from [Udacity]().
* `mini_sparkify_event_data.json`: subset of user activity data. (not uploaded due to data quota limit)


## Data
Data that will be used for the analysis and training of the model:

* (mini_sparkify_event_data.json.zip): dataset with the data collected in
the service

## Summary of Results

Accuracy and F1 score obtained for five different models are displayed in the following
table:


| Model name | Accuracy | f1score | Training time (min:sec)|
| :---: | :---: | :---: | :---: |
| Logistic Regression | 0.914286 | 0.902108 | 0 days 00:20:00.105321
| Random Forest | 0.742857 | 0.733348 | 0 days 00:16:11.130489
| Decision Tree | 0.800000 | 0.805938 | 0 days 00:18:24.188392
| Gradient Boosted Trees | 0.800000 | 0.805938 | 0 days 00:29:02.641496
| LinearSVC | 0.828571 | 0.750893 | 0 days 00:17:43.810483

<br />

A comparison of these results can be seen in the following pictures:

![Accuracy](https://github.com/pedflotor/Sparkify-Churn-Prediction/blob/master/images/Accuracy.png)
![f1score](https://github.com/pedflotor/Sparkify-Churn-Prediction/blob/master/images/f1score.png)

<br />

The best fitting model was a Logistic Regresion Classificatio model with accuracy
of 0.91 and F1 score of 0.90. Important features were user tenure (registration_min),
friend, and average songs per session.

From them, the higher the value of these features are, most likely the user will
stay in the service and will not churn.

<br />

Future improvements may include a larger dataset and use increased parameters
in Grid Search to tune the models.


## Project Blog Post on Medium
* https://medium.com/@ajnacht/customer-churn-prediction-5aad7d80afde


## Acknowledgements
+ https://spark.apache.org/docs/latest/ml-classification-regression.html
+ https://spark.apache.org/docs/latest/ml-tuning.html
