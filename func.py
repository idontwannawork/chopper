#-*- coding:utf-8 -*-

import re
import sys
import argparse
import jaconv

# 引数取得
def get_args():
    # 準備
    parser = argparse.ArgumentParser()

    # 標準入力以外の場合
    if sys.stdin.isatty():
        # 必須引数
        parser.add_argument("file", help="please set me", type=str)

    # 任意の引数を設定したい場合は引数名の頭に"--"を書く
    # parser.add_argument("--type", type=int)
    # parser.add_argument("--alert", help="optional", action="store_true")

    # 設定したオプションを使いたいときは下記のように書く
    # print(args.alert)
    # if args.alert:
    #     None

    # 結果を受ける
    args = parser.parse_args()

    return(args)

# ファイルを読み込んで中身を返す
def get_file(src):

    # UTF-8を明示してファイルオープン
    input_data = open(src,"r", encoding='UTF-8')
    
    # 全行を読み込んでリスト化
    lines = input_data.readlines()

    input_data.close()

    return(lines)

# 文字列の整形
def change_str(input_string):
    # カナは全角に変換
    changed_line=jaconv.h2z(input_string)
    # 数字、記号、アルファベットの全角を半角に変換
    changed_line = jaconv.z2h(changed_line,kana=False,digit=True,ascii=True)
    # 前後のスペースと改行コードを除外
    changed_line = changed_line.strip()
    # 文中のスペースを除外
    changed_line = changed_line.replace(" ","")

    return changed_line

# ファイル内容を正規表現で判断し分割する
def chop_categoly(input_list):

    result_str = ''
    result_cat = ''

    # 1行ずつ処理
    # for line in input_list:
    it = iter(input_list)

    while True:
        try:
            i = change_str(next(it))
            # 正規表現
            cat = re.match(r"^\(.+\)$",i)
            
            if cat:
                result_cat = cat.group(0).replace("(","").replace(")","")
                
                i = change_str(next(it))

                while i != '':
                    result_cat = result_cat + ',' + i
                    i = change_str(next(it))

                result_str = result_str + result_cat + '\n'

                result_cat = ''
            else:
                pass

        except StopIteration:
            break

    return result_str

def write_file(output_string):
    f = open('./output.csv','w',encoding='utf-8')
    f.write(output_string)
    f.close()
