#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = input()
    a = {"a", "e", "i", "o", "u", "y"}
    s = 0
    for i in u:
        if i in a:
            s += 1
    print(s)