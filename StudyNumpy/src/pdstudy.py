'''
Created on 2023/06/15

@author: Keroichi.T
'''

import pandas as pd

def studyfunc01():
    df = pd.read_csv("../dataset/weather.csv")
    print(df.head(3))   # 先頭から引数を指定した行だけ表示
    print(df.tail(10))  # 末尾から引数を指定した行だけ表示


def main():
    studyfunc01()    
    # studyfunc02()    
    # studyfunc03()    
    # studyfunc04()    
    # studyfunc05()    

if __name__ == '__main__':
    main()