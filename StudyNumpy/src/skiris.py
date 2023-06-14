'''
Created on 2023/06/14

@author: Keroichi.T
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    iris = load_iris()
    X = iris.data[:,[0,2]]
    y = iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=77)

    model = RandomForestClassifier(random_state=77)
    model.fit(X_train,y_train)
    
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,pred)
    print(accuracy)
    

if __name__ == '__main__':
    main()