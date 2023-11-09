# 4A:

#
# import math
#
# def angenaherten_wert(nr):
#     wurzel = math.sqrt(nr)
#     ang_wert = round(wurzel)
#     return ang_wert
#
# print('Angenaherten Wert einer Quadratwurzel ist:', angenaherten_wert(10))
#

# 4B:


# def prim(nr):
#     teiler = 2
#     ct = 0
#     if nr > 1:
#         if nr % teiler == 0:
#             nr = nr / teiler
#             ct += 1
#         else:
#             teiler += 1
#     if ct > 0:
#         return 0
#     else:
#         return 1
# string = [25, 28, 39, 44, 52, 57, 101, 113]
# max_subseq = [string[0]]
# crt_subseq = [string[0]]
# for n in range(1, len(string)):
#     crt_num = string[n]
#     prev_num = string[n - 1]
#     if crt_num > prev_num:
#         dif = crt_num - prev_num
#     else:
#         dif = prev_num - crt_num
#     if prim(dif) == 1:
#         crt_subseq.append(string[n])
#     else:
#         crt_subseq = [string[n]]
#     if len(crt_subseq) >= len(max_subseq):
#         max_subseq = crt_subseq
#
# print('Langste aufeinanderfolgende Folge ist:', max_subseq)


# 9A:

#
# def zerlegen(nr):
#     teiler = 2
#     faktoren = []
#     while nr > 1:
#         if nr % teiler == 0:
#             nr = nr / teiler
#             faktoren.append(teiler)
#         else:
#             teiler += 1
#
#     return faktoren
#
# print("Die Primfaktoren von gegebenen Zahl sind:", zerlegen(140))
#

# 9B:

#
# string = [123, 321, 213, 897, 789, 451]
# max_subseq = [string[0]]
# crt_subseq = [string[0]]
#
# for n in range(1, len(string)):
#     crt_num = string[n]
#     prev_num = string[n - 1]
#
#     if sorted(set(str(crt_num))) == sorted(set(str(prev_num))):
#         crt_subseq.append(crt_num)
#     else:
#         crt_subseq = [string[n]]
#
#     if len(crt_subseq) >= len(max_subseq):
#         max_subseq = crt_subseq
#
# print('Langste aufeinanderfolgende Folge ist:', max_subseq)