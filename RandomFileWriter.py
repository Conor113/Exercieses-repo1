import random

def random_num():
    random_num=random.randint(1,500)
    return random_num
def write():
    amount = int(input("enter amount of numbers: "))
    run=0
    file = open('randomNum.txt', 'w')
    while run < amount:
        run+=1
        file.write ((str(random_num()))+'\n')
    file.close()


def main():
    random_num()
    write()
main()
