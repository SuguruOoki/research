# -*- coding: utf-8 -*-
import os
import csv
import numpy as np
import matplotlib as mpl

def read_data(id):
    ''' 関数のDocstring '''
    trdatafile = id + '_data.txt'
    trlabelfile = id + '_label.txt'
    # 訓練データの読み込み
    os.chdir('/Users/suguruoki/Documents/研究/共起単語データ')
    tmp = np.genfromtxt(trdatafile, delimiter='\t')
    trdata = tmp[:,:tmp.shape[1]-1]
    trlabel = np.genfromtxt(trlabelfile, delimiter='\t')
    tmp = 0
    print("trdata")
    print(trdata)
    print("trlabel")
    print(trlabel)
    print("trdata.shape")
    print(trdata.shape)
    print("trlabel.shape")
    print(trlabel.shape)
    
    tedatafile = 'ans-' + id + '_data.txt'
    telabelfile = 'ans-' + id + '_label.txt'
    # テストデータの読み込み
    os.chdir('/Users/suguruoki/Documents/研究/answer_data')
    tmp = np.genfromtxt(tedatafile, delimiter='\t')
    tedata = tmp[:,:tmp.shape[1]-1]
    telabel = np.genfromtxt(telabelfile, delimiter='\t')
    print("tedata")
    print(tedata)
    print("telabel")
    print(telabel)
    print("tedata.shape")
    print(tedata.shape)
    print("telabel.shape")
    print(telabel.shape)


def main():
    ''' main関数 '''
    wid = '117'
    read_data(wid)


if __name__ == '__main__':
    main()

