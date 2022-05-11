import math

num1 = 0
num2 = 1
denom1 = 1
denom2 = 1

number_to_approx = math.e / 3
curr = (num2+num1)/(denom1+denom2)

while abs(number_to_approx- curr) > 1e-20:
    if number_to_approx > curr:
        num1 += num2
        denom1 += denom2
    else:
        num2 += num1
        denom2 += denom1

    curr = (num2+num1)/(denom1+denom2)
    # print(f'\n\n{num2 + num1}|{denom1 + denom2}\n\n')

print(f'\n\n{num2+num1} / {denom1+denom2}\n\n')

