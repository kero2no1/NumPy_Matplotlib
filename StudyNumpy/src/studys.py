'''
Created on 2023/05/29

@author: Keroichi.T
'''

import numpy as np
import matplotlib.pyplot as plt

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
    print( arr_1.T )                # ベクトルの転置はndarrayの作り方に注意
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
    # 行列にスカラーをかける（ブロードキャストという）
    arr_1 = np.array([[4,-2],[1,0]])
    print( arr_1 * 0.5 )
    arr_2 = np.array([[8,1,5],[-3,0,-7]])
    print( arr_2 * 2 )
    
    # ベクトルのサイズ変更
    arr_1 = np.arange(12)
    print( arr_1 )
    arr_2 = arr_1.reshape(3,4)
    print( arr_2 )
    
    # 統計値
    arr_1 = np.array([[2,4,6],[-1,5,-3],[0,-2,3]])
    print( arr_1.max() )            # 各要素の最大(引数にaxis=を追加すると、列ごと行ごとの統計値を算出可能)
    print( arr_1.min() )            # 各要素の最小
    print( arr_1.sum() )            # 各要素の総和
    print( arr_1.mean() )           # 各要素の平均
    print( arr_1.var() )            # 各要素の分散
    print( arr_1.std() )            # 各要素の標準偏差
    
    

def exercise4():
    # ユニバーサル関数 ・・・ndarrayの全要素の要素ごとに演算処理するもの
    arr_1 = np.array([0,1,2,4]).reshape(2,-1)
    print( arr_1 )
    print( np.sqrt( arr_1 ) )       # 平方根
    print( np.exp( arr_1 ) )        # exp
    
    arr_1 = np.array([0, np.pi, np.pi/2, -np.pi/4]).reshape(2,-1)
    print( arr_1 )
    print( np.sin( arr_1 ) )
    print( np.cos( arr_1 ) )

def exercise5():
    # 行列の結合と分解
    arr_1 = np.array([0,1,-1,2,4,-3,5,-2,7]).reshape(3,-1)
    arr_2 = np.array([-2,0,1,5,-1,2,-6,3,4]).reshape(3,-1)
    print( arr_1 )
    print( arr_2 )
    
    arr_3 = np.vstack( (arr_1,arr_2) )  # 縦方向(vertical)結合
    print( arr_3 )
    print( np.vsplit( arr_3, 2 ) )      # 縦方向の分解(２つに分解した)
    print( np.vsplit( arr_3, 2 )[0] )   # ２つのうちの1つ目は配列要素で抽出できる
    print( np.vsplit( arr_3, 2 )[1] )
    
    arr_3 = np.hstack( (arr_1,arr_2) )  # 横方向(horizontal)結合
    print( arr_3 )
    print( np.hsplit( arr_3, 2 ) )      # 横方向の分解(２つに分解)
    print( np.hsplit( arr_3, 2 )[0] )   # ２つのうちの1つ目は配列要素で抽出
    print( np.hsplit( arr_3, 2 )[1] )

def exercise6():
    x1 = np.linspace(0,2*np.pi,500)
    x2 = np.random.randint(0,30,100)
    y1 = np.sin(x1)
    y2 = np.cos(x1)
    
    fig = plt.figure()
    ax1 = fig.add_subplot( 2,1,1 )
    ax2 = fig.add_subplot( 2,1,2 )
    ax1.plot(x1,y1)
    ax1.plot(x1,y2)
    
    ax2.hist( x2, bins=20 )
    
    plt.show()
    
def exercise7():
    arr_1 = np.array([-10,-8,-6,-4,-2,0,2,4,6,8,10,12]).reshape(4,-1)
    arr_2 = np.array([-1,-2,-2,-2,-2,-1,-2,-2,-2,-2,-1,-2]).reshape(3,-1)
    print(arr_1.shape,arr_2.shape)

    if arr_1.shape[1] == arr_2.shape[0]:
        arr_3 = arr_1 @ arr_2
        print( arr_3 )
        
        arr_4 = arr_3[:2,:2]
        print( arr_4 )
        print( np.linalg.det(arr_4.T))
        print( np.linalg.inv(arr_4.T))
        
def exercise8():
    arr_1 = np.random.randint(-100,100,300)
    arr_2 = np.random.randint(-100,100,300)

    plt.scatter(arr_1,arr_2)
    plt.show()

def main():
    
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
    exercise8()
    
    

if __name__ == '__main__':
    main()