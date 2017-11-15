# -*- coding: utf-8 -*-
# @author puyangsky


from __future__ import print_function


def cos(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


v1 = (1, 10)
v2 = (1, 9)
print(cos(v1, v2))
