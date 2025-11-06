from statistics import LinearRegression
from sklearn.conftest import fetch_california_housing
from sklearn.metrics import r2_score

from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

X,y=load_iris(return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=RandomForestClassifier()
model.fit(X_train,y_train) #Train the model
print(X_train.shape)
print(X_test.shape)
print("Accuracy:",model.score(X_test,y_test))

from sklearn.metrics import classification_report, mean_squared_error
y_pred=model.predict(X_test)
print(classification_report(y_test,y_pred))

pipeline=Pipeline([
    ('scaler',StandardScaler()),
    ('model',RandomForestClassifier())
     ]) 


pipeline.fit(X_train,y_train)
print("Pipeline Accuracy:",pipeline.score(X_test,y_test))

housing=fetch_california_housing()
X,y=housing.data,housing.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

model=LinearRegression()

model.fit(X_train_scaled,y_train)

y_pred=model.predict(X_test_scaled)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("Mean Squared Error:",mse)
print("R^2 Score:",r2)