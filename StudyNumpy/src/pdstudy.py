'''
Created on 2023/06/15

@author: Keroichi.T
'''

import pandas as pd

def studyfunc01():
    df = pd.read_csv("../dataset/weather.csv")
    print(df.head(3))   # 先頭から引数を指定した行だけ表示
    print(df.tail(10))  # 末尾から引数を指定した行だけ表示
    
    print(df.columns)
    
    # 指定したカラムだけを抽出する
    df = df[['年月日', '平均気温(℃)', '最高気温(℃)', '最低気温(℃)', '降水量の合計(mm)',
       '最深積雪(cm)', '平均雲量(10分比)', '平均蒸気圧(hPa)',
       '平均風速(m/s)', '日照時間(時間)']][1:]
    print(df)
    
    print(df.dtypes)    # データの型
    print(df.shape)     # データフレームのサイズ
    print(df.columns)   # 列名の取得
    print(df.index)     # 行名の取得
    
    # 任意の要素を取得(要素番号で指定する方法)
    print(df.iloc[4:10,2:6])    # 5行目から10行目(要素4~9)、3列目から6列目(要素2~5)
    
    # 任意の要素を取得(名前で指定する方法)
    print(df.loc[5:10,'最高気温(℃)':'最深積雪(cm)'])
    
    
def studyfunc02():
    # 条件抽出あれこれ
    df_people = pd.read_csv("../dataset/people.csv")
    print(df_people)
    
    # メソッドを使わない方法
    print(df_people[df_people["nationality"] == "America"])

    # メソッドを使う方法
    print(df_people.query("nationality == 'America'"))
    print(df_people[df_people["nationality"].isin(["America"])])
    
    # 複合条件
    print(df_people[(df_people["age"] >= 20) & (df_people["age"] < 30)])
    print(df_people.query("age >= 20 & age < 30"))
    
    # ユニークな値の抽出(DataFrameではなくSeriesに対して使える)
    print(df_people["nationality"].unique())
    
    # 重複除去
    print(df_people.drop_duplicates())  # 全カラムで一致している行の削除
    print(df_people.drop_duplicates(subset="nationality"))
    
    

def studyfunc03():
    # カラム名の変更
    df = pd.read_csv("../dataset/weather.csv")
    print(df.head(3))
    df = df[['年月日', '平均気温(℃)', '最高気温(℃)', '最低気温(℃)', '降水量の合計(mm)',
       '最深積雪(cm)', '平均雲量(10分比)', '平均蒸気圧(hPa)',
       '平均風速(m/s)', '日照時間(時間)']][1:]
    print(df.head(3))
    print(df.columns)
    
    # まとめて変更
    df.columns = ['年月日', '平均気温', '最高気温', '最低気温', '降水量の合計', '最深積雪',
       '平均雲量', '平均蒸気圧', '平均風速', '日照時間']
    print(df.columns)
    
    # カラムを指定して変更
    df = df.rename(columns={"平均気温":"平均"})
    print(df.columns)
    
    # 並べ替え
    print(df.sort_values("最高気温",ascending=False))   # 降順

def studyfunc04():
    # pandas Series型の基本
    s = [50,60,70,80,90]
    sr = pd.Series(s)
    print(sr, type(sr), sr.dtype, sr.size, len(sr))
    
    # インデックスの設定
    print(sr.index)
    sr.index=["a","b","c","d","e"]
    print(sr)
    print(sr.index)
    
    # インデックスの貼り直し。drop＝Trueでindexを削除。
    sr.reset_index(drop=True,inplace=True)
    print(sr)
    
    # インデックスを指定して削除やデータの変更
    sr.drop(0,inplace=True)
    print(sr)
    sr[1] = "6"
    print(sr)
    

def main():
    # studyfunc01()    
    # studyfunc02()    
    studyfunc03()    
    # studyfunc04()    
    # studyfunc05()    

if __name__ == '__main__':
    main()