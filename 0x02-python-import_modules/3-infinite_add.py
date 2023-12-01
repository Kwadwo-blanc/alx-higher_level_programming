#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for j in range(1, len(sys.argv)):
        result += int(sys.argv[j])
    print("{}".format(result))
