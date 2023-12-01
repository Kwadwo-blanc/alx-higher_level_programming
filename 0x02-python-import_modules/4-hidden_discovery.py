#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for j in range(0, len(arr)):
        if arr[j][0:2] != "__":
            print("{}".format(arr[j]))
