# -*- coding: utf-8 -*-
"""DAY-4(Logistic Regression).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SkEa4oVRVCAymIl-c7KXu-C8_6tNEJAK
"""

import numpy as np        # For numerical operations and arrays
import pandas as pd         # For data loading, manipulation, and analysis
import matplotlib.pyplot as  plt # for data visualzing
import seaborn as sns        # For advanced data visualization with better styling

data=pd.read_csv("/content/Social_Network_Ads.csv") # read the dataset from csv
data # display the data

data.info() # information about the dataset

x=data[['Age','EstimatedSalary']] # taking the input attributs in x variable

x.head() # printing top 5 input attributes only

y=data['Purchased'] # taking the output attribute in y variable

y

from sklearn.model_selection import train_test_split# we cam spilit the dataset into train,test

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

x_train # displaying the train data in random

from sklearn.linear_model import LogisticRegression # importing the logistic regression

model=LogisticRegression()

model.fit(x_train,y_train) # giving the training data to model to find out relation between input and output

model.predict(x_test) # testing the model by giving the testing data

y_test # displaying the output test

"""test data"""

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score, roc_curve # importing evaluation metrics for logistic regression

acc=accuracy_score(y_test,model.predict(x_test)) # gives the accuracy of the model
confma=confusion_matrix(y_test,model.predict(x_test)) # gives the confusion matrix of the data
classrep=classification_report(y_test,model.predict(x_test)) # gives the precision,recall of the model

print(acc)
print(confma)
print(classrep)

"""predicting accuracy , confusion matrix and classification report for Trained data"""

model.predict(x_train) # predicting the x_train values

y_train # y-train values

acc=accuracy_score(y_train,model.predict(x_train))  # gives the accuracy of the model
confma=confusion_matrix(y_train,model.predict(x_train)) # gives the confusion matrix of the data
classrep=classification_report(y_train,model.predict(x_train)) # gives the precision,recall of the model

print(acc)
print(confma)
print(classrep)

# ROC-AUC Analysis
y_scores = model.predict_proba(x_test)[:, 1]  # Probabilities for the positive class
roc_auc = roc_auc_score(y_test, y_scores)
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc

# Plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()

#Threshold Tuning
optimal_threshold = thresholds[np.argmax(tpr - fpr)]
optimal_threshold

# Use the tuned threshold for prediction
y_pred_custom = (y_scores >= optimal_threshold).astype(int)
classification_report(y_test, y_pred_custom)

# Sigmoid Explanation
# Plot the sigmoid probabilities vs. actual label
plt.figure(figsize=(8, 5))
plt.scatter(range(len(y_scores)), y_scores, c=y_test, cmap='bwr', alpha=0.7)
plt.axhline(y=0.5, color='gray', linestyle='--')
plt.xlabel("Sample Index")
plt.ylabel("Predicted Probability")
plt.title("Predicted Probabilities (Sigmoid Output)")
plt.grid()
plt.show()