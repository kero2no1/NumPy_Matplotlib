'''
Created on 2023/06/14

@author: Keroichi.T
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

def iris_test():
    iris = load_iris()
    X = iris.data[:,[0,2]]
    y = iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=77)

    model = RandomForestClassifier(random_state=77)
    model.fit(X_train,y_train)
    
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,pred)
    print(accuracy)

def data_load_pandas():
    df = pd.read_csv("../dataset/data.csv")
    print(df.head())
    print(df.tail())
    
    print(df.shape)
    print(df.isnull().sum())        # 欠損値の確認
    df.dropna(inplace=True)         # 欠損値除去
    print(df.shape)
    print(df.isnull().sum())
    
    
    df = pd.read_csv("../dataset/data.csv")
    print(df[["Age"]].tail())
    print(df[["Age"]].mean())       # ある列の平均値を求める
    print(df[["Age"]].describe())   # 統計値をまとめて取得する
    
    df_zero = df[["Age"]].fillna(0) # 欠損値をゼロで補完する
    print(df_zero[["Age"]].tail())  

    df_mean = df[["Age"]].fillna(int(df["Age"].mean()))     # 欠損値を平均値で補完する
    print(df_mean[["Age"]].tail())
    
    df_median = df[["Age"]].fillna(int(df["Age"].median())) # 欠損値を中央値で補完する
    print(df_median[["Age"]].tail())
    
    # 乱数を使った補完
    mean = df["Age"].mean()
    std = df["Age"].std()
    num = df["Age"].isnull().sum()
    rn = np.random.randint(mean-std,mean+std,size=num)
    print(rn)
    
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    ax1.hist(df["Age"].dropna().astype(int),bins=70)
    
    # df["Age"][df["Age"].isnull()] = rn
    # print(df["Age"][df["Age"].isnull()])
    
    plt.show()

def main():
    # iris_test()
    data_load_pandas()
    

if __name__ == '__main__':
    main()