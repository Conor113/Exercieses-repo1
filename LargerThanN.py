def display(number_list,n):
    number_list.sort()
    for number in number_list:
        if number > n:
            print(number)

def main():
    number_list=[1,4,10,200,30,5,6,33,77,8,88,99,9]
    n=10
    display(number_list,n)


main()