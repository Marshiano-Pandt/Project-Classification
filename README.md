# Project-Classification

Telco Churn Analysis

Project Description

Telco, a telecommunications enterprise, provides a wide array of services catering to a diverse clientele. This project we will try to find out why some Telco customers are churning.

Project Goal:

- Look into drivers for customers churning
- Develop models to see if features chosen result in churning
- Use the findings to understand why customers are churning and develop a plan to lower customers from churning



# The Plan

Aquire data from Codeup MYSQL Database

# Prepare data

Create Engineered columns from existing data
Explore data in search of drivers of churn

Answer the following initial questions:
Does being a senior_citizen affect customer churn? 
Does gender affect customer churn?
Does having a partner affect customer churn?
Does dependents affect customer churn?

Develop a Model to predict if a customer will churn or not

Use drivers identified in Explore to build predictive models of different types
Evaluate models on the train and validate data
Select the best model 
Evaluate the best model on test data
Draw conclusions

## **Data Dictionary**

| Feature | Definition |
|:--------|:-----------|
|customer_id|Unique identifier for each customer|
|gender|The gender of the customer (male,female)|
|senior_citizen|Indicates whether the customer is a senior citizen|
|partner|Indicates whether the customer has a partner|
|dependents|Indicates whether the customer has dependents|
|tenure|The duration in months that a customer has been with the service provider|
|phone_service|Indicates whether the customer subscribes to phone service|
|multiple_lines|Indicates whether the customer has multiple phone lines|
|internet_service|Indicates whether the customer subscribes to internet service|
|online_security|Indicates whether the customer has online security features|
|online_backup|Indicates whether the customer has online backup features|
|device_protection|Indicates whether the customer has device protection features|
|tech_support|Indicates whether the customer has technical support services|
|streaming_tv|Indicates whether the customer subscribes to streaming TV services|
|streaming_movies|Indicates whether the customer subscribes to streaming movie services|
|paperless_billing|Indicates whether the customer has opted for paperless billing|
|monthly_charges|The amount charged to the customer monthly |
|total_charges|The total charges incurred by the customer|
|churn|Indicates whether the customer has churned|
|contract_type|Type of contract subscribed by the customer (month-to-month, one-year, two-year)|
|internet_service_type|Type of internet service subscribed by the customer (DSL, fiber optic)|
|payment_type|The method of payment chosen by the customer (bank transfer, credit card, electronic check, mailed check)|

Clone this repo.
If you have access to the Codeup MYSQL DB:
Save env.py in the repo that follows the "sample env.py file" format below.
Ensure the env.py has the appropriate database connection.
If you don't have access:
Request access from Codeup
Follow step 2 after obtaining access.
Run notebook.
sample env.py file:
host = 'data.codeup.com'
username = 'sample_username'
password = 'sample_password'

def get_db_url(database_name, host_name=host, password=password, username=username):
    return f'mysql+pymysql://{username}:{password}@{host_name}/{database_name}'

Conclusion:

- Customers that are senior citizens are more likely to churn.
- We can conclude that there is NO significant relationship between gender and churn.
- Customers that have a partner are less likely to churn
- Customers that do not have dependents are more likely to churn

Recommendations:

- Look into why senior citizens are more likely to churn, is it because of other companies offering better products or is it because of survival rate. If it is because of product look into products that could benefit senior citizens more.
- There is no significant relationship between gender and churn, I recommend looking at different variable within the data set.
- For customers with no dependents or partners, what features or offers could be marketed to customers that are single.
- Given more time, I would look into all variables on why customers are likely ro churn.
