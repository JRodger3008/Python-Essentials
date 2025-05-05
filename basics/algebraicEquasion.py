# # 2.6.10 LAB
# This program evaluates the following expression:
#    1
# --------
#      1
# x + ---
#       1
#  x + ---
#        1
#   x + ---
#        x

x = float(input("Please enter a number for the x value: "))

y = 1. / (x + 1. / (x + 1. / (x + 1. / x)))

print("y = ", y)
