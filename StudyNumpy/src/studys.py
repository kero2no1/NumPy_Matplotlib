'''
Created on 2023/05/29

@author: Keroichi.T
'''

import numpy as np

def exercise1():
    # ベクトル・行列の生成
    print( np.__version__ )
    print( np.sqrt(2) )
    
    arr_1 = np.zeros(10, dtype=np.int16 )
    print(arr_1)
    
    arr_1 = np.array([1,2,3,4])
    arr_2 = np.array([[4],[-1],[0]])
    print(arr_1)
    print(arr_2)
    
    arr_1 = np.array([[3,-2],[7,1]])
    arr_2 = np.array([[3,-2,0,1],
                      [7,1,-1,2],
                      [4,-5,1,3]])
    print(arr_1)
    print(arr_2)
    
    arr_1 = np.zeros((1,2), dtype=np.int16)
    arr_2 = np.ones((4,1), dtype=np.int8)
    print(arr_1)
    print(arr_2)
    
    # 単位行列の作り方
    arr_1 = np.eye(3)
    arr_2 = np.eye(3,4)
    print(arr_1)
    print(arr_2)
    
    # 基本情報の取得
    print( arr_1.shape )
    print( arr_1.ndim )     # 次元の取得
    print( arr_1.dtype )    # 要素の型
    print( arr_1.size )     # 要素の数
    
    # インデックスとスライシング
    # arr_1 = np.array([1,3,5,7,9,11], dtype=np.int16 )
    arr_1 = np.arange(1,13,2, dtype=np.int16 )
    print( arr_1[3:6] )
    print( arr_1[::-1] )
    
    arr_2 = np.array(
        [[2,4,6],
         [-1,5,-3],
         [0,-2,3]])
    
    print( arr_2[:1,] )
    print( arr_2[0] )
    print( arr_2[2,0] )
    print( arr_2[1:,1:])

def exercise2():
    pass

def exercise3():
    pass


def main():
    
    exercise1()
    
    

if __name__ == '__main__':
    main()