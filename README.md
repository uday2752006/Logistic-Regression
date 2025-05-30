# Logistic Regression - Social Network Ads Purchase Prediction

This project demonstrates the complete application of a **Logistic Regression** model using Python to predict whether a user will purchase a product based on demographic data such as **Age** and **Estimated Salary**.

---

##  Dataset

**File:** `Social_Network_Ads.csv`  
This dataset includes:

- `Age`: Age of the user
- `EstimatedSalary`: Estimated annual salary
- `Purchased`: Target variable (0 = No, 1 = Yes)

---

##  Objective

To build a classification model that predicts purchase behavior using logistic regression, while demonstrating good ML practices including feature scaling, evaluation metrics, ROC-AUC analysis, and threshold tuning.

---

##  Workflow Summary

1. **Data Preprocessing**
   - Load and inspect dataset
   - Select features (`Age`, `EstimatedSalary`)
   - Standardize features using `StandardScaler`

2. **Modeling**
   - Train-test split (80%/20%)
   - Train a `LogisticRegression` model

3. **Evaluation**
   - Predict on test and train data
   - Calculate:
     - Accuracy
     - Confusion Matrix
     - Precision, Recall, F1-Score
     - ROC-AUC Score
     - Optimal threshold based on TPR - FPR
   - Visualize:
     - ROC Curve
     - Sigmoid output probabilities

---

##  Evaluation Metrics Used

- **Accuracy Score**  
- **Confusion Matrix**  
- **Classification Report**  
- **ROC-AUC Score**  
- **Threshold Tuning (TPR - FPR Optimization)**  
- **Sigmoid Probability Visualization**

---

##  Visuals

- **ROC Curve**: AUC shows the model's ability to distinguish between classes.
- **Sigmoid Output Plot**: Visualizes predicted probabilities for each test sample.
- **Confusion Matrix**: Shows TP, FP, FN, TN for performance insights.

---

##  Libraries Used

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

##  Files Included

- `logistic_regression_social_ads.py` – Full implementation code
- `Social_Network_Ads.csv` – Dataset used
- `README.md` – Project documentation

---

##  How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python logistic_regression_social_ads.py
