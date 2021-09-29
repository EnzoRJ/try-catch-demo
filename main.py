
a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError as e:
    print('You cant divide by Zero')
else:
    print('Something is wrong')
finally:
    print('You are done')
