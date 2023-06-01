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

    # 等間隔に分割する、第三引数未指定の場合は50分割
    arr_1 = np.linspace( 0,3*np.pi )
    print( arr_1 )


def exercise2():
    # 四則演算
    arr_1 = np.array([[1,3],[-2,4]])
    arr_2 = np.array([[2,-1],[3,0]])

    # 足し算    
    arr_3 = arr_1 + arr_2
    print( arr_3 )

    # 引き算
    arr_3 = arr_1 - arr_2
    print( arr_3 )

    # かけ算(行列積)
    arr_1 = np.array([[-2,-5],[1,3]])
    arr_2 = np.array([[3,0],[6,2]])
    arr_3 = arr_1 @ arr_2           # 方法①：@を使う
    print( arr_3 )
    print( arr_1.dot( arr_2 ) )     # 方法②：dotメソッドを使う
    
    # アダマール積(要素同士(同じ場所同士)のかけ算のこと)
    arr_1 = np.array([[3,5],[4,-1]])
    arr_2 = np.array([[-2,1],[0,-3]])
    arr_3 = arr_1 * arr_2
    print( arr_3 )
    
    
    # 転置
    arr_1 = np.array([[2,3,4]])     # 1次元ではなく2次元になるように定義する
    arr_2 = np.array([[1.2,3.5,5.1],[-0.3,1.1,-4.5]])
    print( arr_1 )
    print( arr_1.T )    # ベクトルの転置はndarrayの作り方に注意
    arr_1 = np.array([2,3,4])
    print( arr_1.reshape(-1,1) )    # 無理やりreshape
    print( arr_2 )
    print( arr_2.T )

    # 逆行列と行列式
    arr_1 = np.array([[4,-2],[1,0]])
    print( arr_1 )
    print( np.linalg.det( arr_1 ) ) # linalgは線形代数、detはdeterminationで行列式のこと
                                    # 行列式≠0 なので逆行列が存在する
    arr_2 = np.linalg.inv( arr_1 )  # invはinverse
    print( arr_2 )
    print( arr_1.dot( arr_2 ) )     # 逆行列との行列積は単位行列になる


def exercise3():
    pass


def main():
    
    # exercise1()
    exercise2()
    
    

if __name__ == '__main__':
    main()