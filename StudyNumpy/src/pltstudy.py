'''
Created on 2023/06/02

@author: Keroichi.T
'''

import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np


def exercise1():
    # 折れ線グラフ
    x = np.arange(10)
    y = np.random.randint(-10,10,10)
    
    # plt.plot(y)     # x軸を指定しない場合はyのインデックスを横軸にとる
    plt.plot(x,y)

    # グラフの詳細設定
    plt.title("Result")     # タイトル
    plt.xlabel("x axis")    # x軸ラベル
    plt.ylabel("y axis")    # y軸ラベル

    plt.show()

def exercise2():
    # 散布図
    x1 = np.random.randint(10,20,20)
    x2 = np.random.randint(20,30,20)
    y1 = np.random.randint(50,100,20)
    y2 = np.random.randint(0,40,20)
    
    plt.scatter(x1,y1)
    plt.scatter(x2,y2)

    # グラフの詳細設定
    plt.xlim(0,40)
    plt.ylim(0,120)


    plt.show()

def exercise3():
    # ヒストグラム
    data = np.random.randint(0,10,10)
    
    ret = plt.hist(data) # retに度数と階級値を取得できる
    print( ret )

    plt.show()

def exercise4():
    # 棒グラフ
    x = ["Sam","John","Kevin","Adam"]
    y = np.random.randint(0,200,4)
    
    plt.bar( x, y )
    
    plt.show()
    

def exercise5():
    # 対数軸
    x = np.linspace(0,10,500)   # 0～10 を 500分割
    y = np.exp(x)
    
    plt.plot(x,y)
    plt.yscale("log")           # Y軸を対数軸に
    
    plt.show()

def exercise6():
    # 凡例を追加する
    x = np.linspace(0,2*np.pi,500)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.plot(x,y1,label="sin")
    plt.plot(x,y2,label="cos")
    
    plt.ylim(-2,2)
    # plt.legend()
    plt.legend(loc=2)   # locで凡例表示位置を指定できる、これは左上(upper left)
    plt.show()

def exercise7():
    # マーカーの種類とサイズの変更
    x1 = np.random.randint(10,35,20)
    x2 = np.random.randint(5,45,20)
    x3 = np.random.randint(0,30,20)
    y1 = np.random.randint(50,100,20)
    y2 = np.random.randint(0,40,20)
    y3 = np.random.randint(20,80,20)
    
    plt.scatter(x1,y1,marker="*",s=80)  # sでマーカーサイズを指定可能
    plt.scatter(x2,y2,marker="^",s=60)
    plt.scatter(x3,y3,marker="x",s=30)
    
    plt.show()
    
def exercise8():
    # 注釈を入れる
    x = [5,3,4,2,0,3,2,1,4,6,8,5]
    
    plt.plot(x)
    plt.annotate("min value", xy=(4.2,0), xytext=(9,1),arrowprops=dict(facecolor="black",shrink=0.05))
    
    '''
    第1引数：表示する注釈文          … min value
    第2引数：矢印←の先頭座標        … x=4.2, y=0 のポイント
    第3引数：注釈文の表示座標        … x=9, y= 1 のポイント
    第4引数：←の色と長さ縮小率      … 黒色で長さ-5%
    '''
    
    # 目盛りを調整する(指定する)
    plt.xticks(np.arange(12))
    plt.yticks(np.arange(0,10,2))
    
    # グリッド線の表示
    plt.grid(True)
    
    plt.show()

def exercise9():
    # 複数のグラフを表示する
    names = ["Sam","John","Kevin","Adam"]
    values = [60,170,10,120]
    
    fig = plt.figure(figsize=(9,6))
    ax1 = fig.add_subplot(1,3,1)
    ax2 = fig.add_subplot(1,3,2)
    ax3 = fig.add_subplot(1,3,3)
    
    ax1.bar(names,values)
    ax2.scatter(names,values)
    ax3.plot(names,values)
    
    plt.show()

def exercise10():
    # ヒートマップとカラーバー
    data = np.random.rand(10,10)
    
    plt.imshow(data,vmin=0,vmax=1,cmap="Blues")
    plt.colorbar()
    
    plt.show()

def exercise11():
    
    plt.rcParams["font.size"] = 14
    fig,ax = plt.subplots()
    
    ax.plot(["月","火","水","木","金","土","日"],[19,22,24,21,20,22,20],
            label="最高気温",marker="o",color="r")
    ax.plot(["月","火","水","木","金","土","日"],[10,13,12,12,10,11,12],
            label="最低気温",marker="^",color="b")
    
    ax.set_xlabel("曜日")
    ax.set_ylabel("気温",rotation="horizontal")
    # ax.set_ylabel("気温",rotation="vertical")
    
    ax.set_yticks([0,5,10,15,20,25])

    
    ax.set_title("東京 10月1週目")
    ax.grid(True)
    
    ax.legend()

    plt.show()

def exercise12():
    # データ生成
    x = np.linspace(1,20,100)
    y1 = x[10:]
    y2 = np.log2(x[10:])
    y3 = np.ones_like(x[10:])
    
    
    # グラフ描画
    plt.figure(figsize=(4,3))
    plt.plot(x[10:], y1, label="線形探索")
    plt.plot(x[10:], y2, linestyle="--", label="2分探索")
    plt.plot(x[10:], y3,linestyle=":", label="ハッシュ表探索")
    plt.legend()
    plt.grid(True)
    plt.tick_params(labelleft=False,labelbottom=False)
    plt.show()

def main():
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
    # exercise8()
    # exercise9()
    # exercise10()
    # exercise11()
    exercise12()

if __name__ == '__main__':
    main()