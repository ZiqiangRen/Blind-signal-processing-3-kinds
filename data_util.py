# coding: utf-8
from __future__ import division
import math
import matplotlib.pyplot as plt

import numpy as np

def get_sig(raw_sig):
    sig = [20 * math.log10(i) for i in raw_sig]
    return sig

#画频数分布直方图
def draw_hist(fig_name, data, bin_num=40):
    # bin_width = (max(data) - min(data)) / bin_num
    # n, nbins, patches= plt.hist(data, bin_num, normed=1, histtype='bar', alpha=0.75)
    plt.xlabel('signal')
    plt.ylabel('frequency')
    plt.title(fig_name)
    # plt.text(min(data), max(n)/1.2, 'bin_width=%f' %bin_width)
    plt.grid(True)
    plt.show()

#计算信号强度的频率分布
def get_hist(data, bin_num=40):
    n, nbins, patches = plt.hist(data, bin_num, normed=1, histtype='bar', alpha=0.75)
    bin_width = (max(data) - min(data)) / bin_num
    bins = list()
    #频数分布直方图的每个长方形的面积，才是该区间内的频率
    for i, _n in enumerate(n):
        n[i] = _n *bin_width
    #取每个bins的中点值（为了保持n和bins维度的一致）
    for i in range(len(nbins)-1):
        bins.append((nbins[i] + nbins[i+1])/2)
    return n, bins

def get_mean_square(narray):
    """计算均方值，即sum(x^2)/n"""
    sum_square = 0
    for _n in narray:
        sum_square += (_n*_n)
    mean_square = sum_square / len(narray)
    return mean_square

def get_sqrt_of_MS(mean_square):
    """计算均方根值"""
    return math.sqrt(mean_square)

def get_feature(data):
    feature = list()
    data_array = np.array(data)
    mean_square = get_mean_square(data_array)
    #print("mean_square=",mean_square)
    sqrt_mean_square = math.sqrt(get_mean_square(data_array))
    #print("sqrt_mean_square=",sqrt_mean_square)
    feature.append(np.max(data_array))
    feature.append(np.min(data_array))
    feature.append(np.mean(data_array)) #f[0]:均值
    feature.append(np.var(data_array))  #f[1]:方差
    feature.append(np.std(data_array))  #f[2]:标准差
    feature.append(mean_square) #f[3]:均方值
    feature.append(sqrt_mean_square)  #f[4]:均方根值
    return feature

'''
if __name__ == '__main__':
    draw_hist('hh',[range(40)], bin_num=40)
    data = range(3)
    print("data:", data)
    get_feature(data)
'''
