#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefgijklmnopqrstuvwxyz")

    a = {"a", "b", "g", "k", "m", "p"}
    b = {"b", "e", "f", "l", "r"}
    c = {"k", "l", "w", "x"}
    d = {"e", "j", "o", "p", "q", "u", "v"}

    x = (a.difference(b)).intersection(c.union(d))
    print(f"x = {x}")

    an = u.difference(a)
    bn = u.difference(b)

    y = (an.intersection(bn)).difference(c.union(d))
    print(f"y = {y}")
