#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res_dic = a_dictionary.copy()
    list_keys = list(res_dic.keys())

    for a in list_keys:
        res_dic[a] *= 2

    return res_dic
