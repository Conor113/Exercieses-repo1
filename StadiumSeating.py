def c_a(number):
    a = format(number * 20, ',.2f')
    print("seat a: $", a)


def c_b(number):
    b =  format(number * 15, ',.2f')
    print("seat b: $",b)


def c_c(number):
    c = format(number * 10, ',.2f')
    print("seat c: $", c)


def main():
    a1=int(input("Number of class a seats sold: "))
    c_a(a1)
    b1=int(input("Number of class b seats sold: "))
    c_b(b1)
    c1=int(input("Number of class c seats sold: "))
    c_c(c1)


main()
