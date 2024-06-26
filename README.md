# Student Performance Predictor


## Introduction

- This is an `End to End Production Grade Data Science Project`.
- This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course. 
- Based on these Gender, Ethnicity, Parental level of education, Lunch and Test preparation courses, we will predict the students' performance.

## Project Description

- The project covers `Data preprocessing, Model training, Hyperparameter Tunning and Evaluation`.
- Main focus areas: `Modular Coding, MLops, Cloud Services, and CI/CD`.
- Utilizes Custom Exception handling mechanisms and custom logs to record each action.
- Implemented using Industry Standard Folder Structure.
- Research conducted using Jupyter Notebook and stored in the Notebook folder.
- Cloud Deployment: The project is deployed on `Microsoft Azure` for scalability and accessibility.
- CI/CD: Implemented using `GitHub Actions` to automate integration & deployment.

### Backend
- Flask web Framework
### Frontend
- HTML & CSS

### Dataset

- Source: - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

- Description: The dataset contains 1000 instances with 8 parameters.

- Preprocessing: Missing values were imputed, and categorical features were encoded using `One Hot Encoding`. And also use `StandardScaler` for standardization.

### Methodology

- Data Cleaning: Handled missing values and outliers.
- Exploratory Data Analysis: Visualized distributions and correlations. The `EDA STUDENT PERFORMANCE.ipynb` file shows the visualization part.
- Feature Engineering: Created new features based on existing data.
- Modeling: Trained `Decision Tree, Random Forest, Gradient Boosting, Linear Regression, XGBRegressor, AdaBoost Regressor` models. `Hyperparameter Tunning` is done for all models.
- Evaluation: Used accuracy, precision and R2-score to evaluate models.

## Installation
Follow these steps to install the necessary dependencies and set up the project.

- clone the repository:
````bash 
    git clone https://github.com/chandima2000/students-performance-predictor.git
````
- go to the root folder: 
````bash
    cd students-performance-predictor
````
- build project: 
````bash 
    pip install -r requirements.txt
````
## Usage
To use the Student Performance Predictor website, run the following command:

````bash 
    python app.py
````
## You can Try 👇
- URL: https://student-performance-indicator.azurewebsites.net/
  
## User Interface
![image](https://github.com/chandima2000/students-performance-predictor/assets/101726882/4118a56f-0b1f-4a17-9e88-0a92aa6b438d)

## Contributions
All contributions are welcome. Feel free to open issues or submit pull requests.

