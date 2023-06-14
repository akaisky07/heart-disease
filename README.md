# heart-disease

Cardiovascular disease can have various causes depending on the specific type. For instance, atherosclerosis contributes to coronary and peripheral artery disease, while arrhythmias can be caused by coronary artery disease, heart muscle scarring, genetic issues, or medications. Valve diseases, on the other hand, can be attributed to factors such as aging, infections, and rheumatic disease.

In terms of the machine learning aspect:

    Different ML models such as random forest, lgbm, cat regressor, etc., were utilized.
    The final model selected based on the least Mean Squared Error (MSE) was the Random Forest model.
    The heart-disease.ipynb file contains data preprocessing, cleaning, and training of various models. The best-performing model is saved as heart_disease_model.joblib, which is then used by the Flask app for the web application. The training data used for the model is stored in the train.csv file.

Regarding the web application:

    Flask is employed to develop the application.
    The app includes a form that collects input from the user and converts it into a dataframe.
    The input dataframe is then fed into the saved ML model, and the resulting output is displayed on the result.html file.

To run the web app, download the necessary files and execute the app.py file via the terminal. Ensure that the required packages mentioned in the code are installed on your system.
Video:

https://user-images.githubusercontent.com/104855741/232224039-5b2861be-2699-4f53-a3ff-187481d6518f.mp4

