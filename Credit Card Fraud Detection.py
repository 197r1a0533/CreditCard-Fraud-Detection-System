# 1.Importing all the necessary Libraries:
# import the necessary packages 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from matplotlib import gridspec

# 2.Loading the Data:
data = pd.read_csv("credit.csv")

3.Understanding the Data:
data.head()

# 4. Describing the Data:
print(data.shape)
print(data.describe()) 

# 5. Imbalance in the Data:
fraud = data[data['Class'] == 1] 
valid = data[data['Class'] == 0] 
outlierFraction = len(fraud)/float(len(valid)) 
print(outlierFraction) 
print('Fraud Cases: {}'.format(len(data[data['Class'] == 1]))) 
print('Valid Transactions: {}'.format(len(data[data['Class'] == 0]))) 


#  6.Print the amount details for Fraudulent Transaction

print(“Amount details of the fraudulent transaction”)
fraud.Amount.describe() 

# 7.Print the amount details for Normal Transaction:

print(“details of valid transaction”) 
valid.Amount.describe() 

# 8.Plotting the Correlation Matrix:

# Correlation matrix 
corrmat = data.corr() 
fig = plt.figure(figsize = (12, 9)) 
sns.heatmap(corrmat, vmax = .8, square = True) 
plt.show()

# 9.Separating the X and the Y values:
# dividing the X and the Y from the dataset 
X = data.drop(['Class'], axis = 1) 
Y = data["Class"] 
print(X.shape) 
print(Y.shape) 
# getting just the values for the sake of processing 
# (its a numpy array with no columns) 
xData = X.values 
yData = Y.values

# 10.Training and Testing Data Bifurcation:

# Using Skicit-learn to split data into training and testing sets 
from sklearn.model_selection import train_test_split 
# Split the data into training and testing sets 
xTrain, xTest, yTrain, yTest = train_test_split( 
		xData, yData, test_size = 0.2, random_state = 42)

# 11.Building a Random Forest Model using skicit learn:

# Building the Random Forest Classifier (RANDOM FOREST) 
from sklearn.ensemble import RandomForestClassifier 
# random forest model creation 
rfc = RandomForestClassifier() 
rfc.fit(xTrain, yTrain) 
# predictions 
yPred = rfc.predict(xTest)

# 12.Building all kinds of evaluating parameters:

# Evaluating the classifier 
# printing every score of the classifier 
# scoring in anything 
from sklearn.metrics import classification_report, accuracy_score 
from sklearn.metrics import precision_score, recall_score 
from sklearn.metrics import f1_score, matthews_corrcoef 
from sklearn.metrics import confusion_matrix 
n_outliers = len(fraud) 
n_errors = (yPred != yTest).sum() 
print("The model used is Random Forest classifier") 
acc = accuracy_score(yTest, yPred) 
print("The accuracy is {}".format(acc)) 
prec = precision_score(yTest, yPred) 
print("The precision is {}".format(prec)) 
rec = recall_score(yTest, yPred) 
print("The recall is {}".format(rec)) 
f1 = f1_score(yTest, yPred) 
print("The F1-Score is {}".format(f1)) 
MCC = matthews_corrcoef(yTest, yPred) 
print("The Matthews correlation coefficient is{}".format(MCC))


# 13.Visulalizing the Confusion Matrix:

# printing the confusion matrix 
LABELS = ['Normal', 'Fraud'] 
conf_matrix = confusion_matrix(yTest, yPred) 
plt.figure(figsize =(12, 12)) 
sns.heatmap(conf_matrix, xticklabels = LABELS, 
			yticklabels = LABELS, annot = True, fmt ="d"); 
plt.title("Confusion matrix") 
plt.ylabel('True class') 
plt.xlabel('Predicted class') 
plt.show()
