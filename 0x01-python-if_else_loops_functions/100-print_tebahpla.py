#!/usr/bin/python3
for e in range(ord('z'), ord('a') - 1, -2):
    print("{:e}{:s}".format(e, chr(e - 33)), end="")
