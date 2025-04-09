import math

#input보다 작은 2의 제곱수   
inputted = int(input())
num_square = int(math.log2(inputted))
num_mul = inputted - 2**num_square
last_num = 2 * num_mul
# inputted - 2**num_square = num_mul
# 2 * num_mul = 마지막수

print(last_num if num_mul != 0 else inputted)



#2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#2 2 4 2 4 6 8 2  4  6  8 10 12 14 16