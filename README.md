# Predictive model for cross selling motor vehicle Insurance

**Author:** DSPT05 - Group 9

## Project Overview

ICEA LION Group includes a Life Insurance company, a General Insurance company, an Asset Management company, and a Trust company. The Life company has provided life insurance to its
customers.  They need help in building a model to predict whether the life insurance policyholders (customers) from the past year will also be interested in Vehicle Insurance provided
by the General Insurance company . ICEA Lion Group aims to capitalize on data analytics to implement a cross-selling strategy for motor vehicle insurance among the current life insurance customer base.


## Problem Statement

Cross-selling presents significant challenges for insurance companies like identifying the right cross-selling opportunities within the existing customer base, lack of personalization, integration with sales processes and measuring success. This project aims to develop a machine learning model that can accurately predict whether the life insurance policyholders (customers) of ICEA LION Group from the past year will also be interested in Vehicle Insurance provided by the General Insurance company.


## Objectives 

1.Identify factors that influence life insurance policy holders interest in motor vehicle insurance.


2.Evaluate performance of different machine learning models in insurance cross-selling by comparing accuracy metrics.


3.Identify machine learning model that shows superior performance in predicting the likelihood of a customer accepting an offer for vehicle insurance.


## Data 

The dataset was sourced from ICEA LION Group. Datasets provided for the analysis include:


***
Datasets Used:

1.  train_data_cross-sell.csv
   
This dataset contains information about customers who have an active  life insuarance cover.Features captured are id(customer unique indentifier) , Gender,Customer_Date_of_Birth, Driving_License, Customer_Residence_Sub_County, Previously_Insured, Vehicle_Year_of_Manufacture, Vehicle_Damage, Annual_Premium, Agent_name, Life_policy_start_date, Response .This dataset contains the target variable "Response" and will be utilized for training the model  

2. test_data_cross-sell.csv

This dataset resembles the training dataset but does not include the target-related variable


***
   
   
## Methods

1. Obtain:
Extracting the data 


2. Scrub:
Explore the raw data set and understand the values
Replacing values with meaningful data and converting data types
Deleting irrelevant and redundant columns

3. Explore:
Creating visualizations to better understand the data
Engineering New Columns
Deriving statistics from the data

![Response by Gender](https://github.com/rbgesembe/Predictive-Modeling-for-Cross-Selling-Motor-Vehicle-Insurance/assets/146054184/5d10bf73-b4d3-4539-8c4f-a02e9f96e536)

There is no significant variance on customer gender in terms of willingness to purchase motor vehicle insurance.(Reception low on both)



![Top 10 counties ](https://github.com/rbgesembe/Predictive-Modeling-for-Cross-Selling-Motor-Vehicle-Insurance/assets/146054184/75832b2a-d8ce-4e62-a9ac-3f0540bb32d0)

Embakasi and Kasarani have the highest numbers of life insurance policies compared to the rest of the subcounties



![Response by Age](https://github.com/rbgesembe/Predictive-Modeling-for-Cross-Selling-Motor-Vehicle-Insurance/assets/146054184/5b38edc5-ddcf-412c-ac60-9bd80f3e2d31)


5. Model:
Created multiple models including Logistic Regression,Decision Tree,Random Forest,KNN Model and XGBoost


6. Interpret:
Evaluating the accuracy and precision score .


## Results

### Original Data

The first steps to creating our model was to load the dataset the various data set separately and do cleaning.
We applied feature engineering to  

   * Gender
   * Vehicle_Damage
   * Customer_Date_of_Birth
   * Life_policy_start_date
   * Vehicle_Year_of_Manufacture


### Identifying Target
The target column is 'Response'. Customer is interested, 0 : Customer is not interested .


## Model
We tested the following models:
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. KNN Model
5. XGBoost

- On comparing the Metrics of the applied models, it was found that Random Forests have better precision and recall as well as a higher F1 score implying a better prediction of both true positives and negatives while minimizing the false positives and negatives. While KNN and XGBoost have similar Accuracy scores, KNN model has better Precision and F1 Scores
  
- ![Different models accuracy](https://github.com/rbgesembe/Predictive-Modeling-for-Cross-Selling-Motor-Vehicle-Insurance/assets/146054184/db104398-3c57-4c41-8d37-433d76aa9035)
  


## Findings
-We’ve 12% chance of converting a customer with a DL compared to 5% without DL

-Males are 4% likely to buy policy compared to females

-23% of policy holders previously insured are likely to buy motor vehicle policy

-Gen X(1965-1980) and Millennials(1981-1996) are more likely to buy motor vehicle policy

-Customers with history of accidents/repairs 23% likely to buy motor vehicle policy


## Recommendations

1. Target previously insured customers through policy upgrades & renewal incentives.
2. Customize marketing messages for customers who have experienced previous vehicle damage, emphasize on comprehensive coverage.
3. Provide customized insurance options based on the age of the vehicle to ensure all customers receive comprehensive protection.
4. Utilize sales agents for personalized recommendations.





