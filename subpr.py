import numpy as np
import matplotlib.pyplot as plt
from db_oper import data_set


def by_min(cx):
    cx_min = cx
    cx_min[0] = 10000
    # print(cx_min)
    min_qv_num = []
    cx_np_min = np.array(cx_min)
    temp = []
    x = 10000
    for i in range(1, 15):
        temp_q = cx_np_min.min()
        temp_n = cx_np_min.argmin()
        # print('times :', temp_q, 'number :', temp_n)
        if temp_q != x:
            x = temp_q
            if len(temp) != 0:  min_qv_num.append(temp)
            temp = []
            temp.append(temp_q)
            temp.append(temp_n)
        else:
            temp.append(temp_n)
        cx_np_min[temp_n] = 20000
    # print(min_qv_num)
    # print(cx_np_min)
    return min_qv_num


def by_max(cx, cycl):
    cx_max = cx
    # print(cx_max)
    max_qv_num = []
    cx_np_max = np.array(cx_max)
    temp = []
    x = 0
    for i in range(cycl):
        temp_q = cx_np_max.max()
        temp_n = cx_np_max.argmax()
        # print('times :', temp_q, 'number :', temp_n)
        if temp_q != x:
            x = temp_q
            if len(temp) != 0: max_qv_num.append(temp)
            temp = []
            temp.append(temp_q)
            temp.append(temp_n)
        else:
            temp.append(temp_n)
        cx_np_max[temp_n] = 0
    # print(max_qv_num)
    # print(cx_np_max)
    return max_qv_num


def graph(cx):
    gr = cx
    xx = list(range(51))
    x = np.array(xx)
    y = np.array(gr)

    plt.bar(x, y)
    plt.title("Kiek iškrito kamoliuku")
    plt.show()


def transf(reg):

    dlist = data_set(reg)  # True/False
    dl_cnt = len(dlist)
    # print(dl_cnt)
    ax = [[0] * 51 for i in range(dl_cnt)]
    bx = ([0] * 51)

    for i in range(dl_cnt):
        ax[i][0] = dlist[i][0]
        for j in range(1, 6):
            ax[i][dlist[i][j]] = 1
        # print(ax[i])

    for j in range(1, 51):
        for i in range(dl_cnt):
            bx[j] += ax[i][j]
    # print(bx)
    return bx


def fibo():
    fb = transf(True)
    # print(fb)
    recom = by_max(fb, 20)
    return recom