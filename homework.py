# import random
# def create_show(fireworks, show_time):
#     fireworks.sort()     #o(n)
#     show = []            #o(1)
#     remaining_time = show_time    #o(1)
#     while remaining_time > 0 and fireworks:   #o(1)
#            # Select a random firework
#            firework = random.choice(fireworks)
#            if firework <= remaining_time:   # o(1)
#                # Add the firework to the show
#                show.append(firework)  #o(1)
#                remaining_time -= firework # o(1)
#             else:
#               # This firework is too long, remove it from consideration
#               fireworks.remove(firework)   #o(n)
#   return show  o(1)

# total would be o (n^2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# codeware example 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)
# def solution(number):
#     result = []      #o(1)
#     for i in range(1, number):    #o(n)
#         if i % 3 == 0 or i % 5 == 0:   o(1)
#             result.append(i)  o(1)

#     return sum(result)  o(n)
# print(solution(10))
# total o(n^2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# total o(n^2)
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
# def digital_root(n): #o(1)
#     xe = sum(int(i) for i in str(n)) #o(n)  o(n) = o(n)
#     if xe > 9: o(1)
#         return digital_root(xe) o(1)
#     return xe o(1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
# def milad():
#     return bin(n).count("1")   o(n)o(n) = o(n)