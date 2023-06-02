'''
Created on 2023/06/02

@author: Keroichi.T
'''

import matplotlib.pyplot as plt 
import numpy as np


def exercise1():
    x = np.arange(10)
    y = np.random.randint(-10,10,10)
    
    # 折れ線グラフ
    # plt.plot(y)     # x軸を指定しない場合はyのインデックスを横軸にとる
    plt.plot(x,y)

    plt.show()

def exercise2():
    x1 = np.random.randint(10,20,20)
    x2 = np.random.randint(20,30,20)
    y1 = np.random.randint(50,100,20)
    y2 = np.random.randint(0,40,20)
    
    # 散布図
    plt.scatter(x1,y1)
    plt.scatter(x2,y2)

    plt.show()

def exercise3():
    data = np.random.randint(0,10,10)
    
    # ヒストグラム
    ret = plt.hist(data) # retに度数と階級値を取得できる
    print( ret )

    plt.show()

def exercise4():
    pass

def exercise5():
    pass

def exercise6():
    pass

def main():
    # exercise1()
    # exercise2()
    exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()

if __name__ == '__main__':
    main()