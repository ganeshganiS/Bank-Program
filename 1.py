try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There is a divided by zero error")
finally:
    print("Manalni evadra apedhi")
