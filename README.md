# heart-disease

The causes of cardiovascular disease can vary depending on the specific type. For example, atherosclerosis (plaque buildup in your arteries) causes coronary and peripheral artery disease. Coronary artery disease, scarring of your heart muscle, genetic problems, or medications can cause arrhythmias. Aging, infections, and rheumatic disease can cause valve diseases.

Machine Learning Model

The ML models used were random forest, lgbm, cat regressor,etc. The Final model selected with least MSE is Random Forest. 

heart-disease.ipynb contains the data pre-processiing, cleaning, training pf diffrent models and the best performed model is then saved as heart_disease_model.joblib which is used by the flask app for web application. train.csv is the data used for the model

Web Application

Flask is used here for the app purpose, it consist of a form which takes various input and convert it into dataframe which is input to ml saved model and output is then displayed over result.html file.

For runnning the web app, download the files and run the app.py file over terminal. The packages used in the code should be downloaded by the user.
