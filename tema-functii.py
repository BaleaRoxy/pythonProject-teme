
# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n]

# def recursivall(n):
#     if n == 0:
#         return 0
#     return n + recursivall(n-1)
# print(recursivall(7))

# def sum_of_even(n):
#     if n==0:
#         return 0
#     if not n % 2 == 0:
#         return sum_of_even(n-1)
#     else:
#         return n + sum_of_even(n-1)
#
#
# print(sum_of_even(7))

#
# def sum_of_odd(n):
#     if n==0:
#         return 0
#     if  n % 2 == 0:
#         return sum_of_odd(n-1)
#     else:
#         return n + sum_of_odd(n-1)
#
#
# print(sum_of_odd(7))

# ● Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

# def multiply(*args):
#     print(args)
# multiply((1, 5, -3,  [12, 56, ‘cad’]))