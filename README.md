# Diabetes Prediction 🩺

<img width="640" height="320" alt="c3a2c9ce-cbc6-4c47-9c29-7dfc4c97c13e" src="https://github.com/user-attachments/assets/30799135-5599-4047-80ca-bab0a9fadd43" />


## Project Overview  
This is an end-to-end machine learning project that builds a predictive model to determine whether a person has diabetes based on health metrics. The project covers data preprocessing, exploratory data analysis, model training, evaluation, and deployment.

## Features & Highlights  
- Data preprocessing: handled missing values, scaling, outlier detection, feature engineering.  
- Model building: trained models (e.g., Logistic Regression, Random Forest) and selected the best performing one.  
- Evaluation: used metrics such as accuracy, ROC-AUC, confusion matrix to assess model performance.  
- Deployment: packaged the best model and set up a simple web app (via `app.py`) for inference.  
- Reproducible pipeline: all steps documented and versioned; model saved as `.pkl`.

## Tech Stack  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, scikit-learn, Matplotlib / Seaborn  
- **Web App / Deployment:** Flask (or whichever you used)  
- **Model Serialization:** Pickle (or joblib)  
- **Versioning / Environment:** requirements.txt for dependencies  
- **Dataset:** [Describe dataset,“Diabetes Dataset”]

## Installation & Setup  
1. **Clone the repository**  
 git clone https://github.com/rahul-1419/Diabetes_prediction.git
 cd Diabetes_prediction

2. **Create a virtual environment (optional but recommended)**
python3 -m venv venv 
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the notebook or web app**
To explore the analysis and modelling: open NoteBook/Script.ipynb in Jupyter.

To run the web app:
python app.py

## Usage

Input relevant patient health metrics (e.g., glucose level, BMI, age) in the web form.

Submit to get a prediction (Diabetic / Non-Diabetic) along with probability (if implemented).

Use the model for batch inference by loading best_logistic_regression_model.pkl in your own scripts.


<img width="640" height="320" alt="c3a2c9ce-cbc6-4c47-9c29-7dfc4c97c13e" src="https://github.com/user-attachments/assets/30799135-5599-4047-80ca-bab0a9fadd43" />

## Featues in dataset
Pregnancies	<br>
Glucose	<br>
BloodPressure	<br>
SkinThickness	<br>
Insulin	<br>
BMI	<br>
DiabetesPedigreeFunction	<br>
Age	<br>
Outcome <br>

**NO Null Values Present** <br>
 Here Outcome is Our Target variable <br>

## Skewness
| Features                   |  Skewness              | Type of Skewness       |
|----------------------------|------------------------|------------------------|
| Pregnancies                |  0.901674              | Right-Skewness Present |
| Glucose                    |  0.173754              | Right-Skewness Present |
| BloodPressure              | -1.843608              | Left-Skewness Present  |
| SkinThickness              |  0.109372              | Right-Skewness Present |
| Insulin                    |  2.272251              | Right-Skewness Present |
| BMI                        | -0.428982              | Left-Skewness Present  |
| DiabetesPedigreeFunction   |  1.919911              | Right-Skewness Present |
| Age                        |  1.129597              | Right-Skewness Present |

## Correlation of Numerical-features with each other

<img width="1128" height="736" alt="{DFEE85F5-B6F3-4B9B-B1F2-5A53E43228BC}" src="https://github.com/user-attachments/assets/ae5467b3-96c4-4e31-a2e9-e09e5c17cef7" />

Here BloodPressure & SkinThickness columns are less correlated with Target column. So Drop both columns

## Model Training

With the rename columns (Pregnancies,Glucose,Insulin,BMI,DiabetesPedigreeFunction,Age) we train our model.

This is Classification Problem so we use Classifer Models.('Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM', 'KNN')

===== Logistic Regression ===== <br>
Train Accuracy: 0.776<br>
Test Accuracy : 0.752<br>
MSE           : 0.248<br>
Fit Status    : Good Fit<br>
Confusion Matrix:<br>
[[140  28]<br>
 [ 35  51]]<br>


===== Decision Tree =====<br>
Train Accuracy: 0.825<br>
Test Accuracy : 0.752<br>
MSE           : 0.248<br>
Fit Status    : Good Fit<br>
Confusion Matrix:<br>
[[141  27]<br>
 [ 36  50]]<br>


===== Random Forest =====<br>
Train Accuracy: 0.901<br>
Test Accuracy : 0.756<br>
MSE           : 0.244<br>
Fit Status    : Overfitting<br>
Confusion Matrix:<br>
[[139  29]<br>
 [ 33  53]]<br>

===== SVM =====<br>
Train Accuracy: 0.800<br>
Test Accuracy : 0.756<br>
MSE           : 0.244<br>
Fit Status    : Good Fit<br>
Confusion Matrix:<br>
[[143  25]<br>
 [ 37  49]]<br>

===== KNN =====<br>
Train Accuracy: 0.817<br>
Test Accuracy : 0.748<br>
MSE           : 0.252<br>
Fit Status    : Good Fit<br>
Confusion Matrix:<br>
[[138  30]<br>
 [ 34  52]]<br>

 **Here One Model Are Overfited.**

 ## Hyperparameter Tuning and Model Evaluation

 **Compare all Models**

<img width="989" height="590" alt="output_2" src="https://github.com/user-attachments/assets/3fb832a5-b993-4708-8f78-addcca6d4fbd" />

<img width="1989" height="425" alt="output" src="https://github.com/user-attachments/assets/7ae29fd1-dc28-4600-b823-09d0c36c8c13" />

From this our best model is Logistic Regression
