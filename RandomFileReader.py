try:
    file = open('randomNum.txt', 'r')
    num = file.readline()
    count=0
    total=0
    while num!='':
        new_num=int(num.rstrip('\n'))
        count+=1
        total+=new_num
        print(num.rstrip('\n'))
        num=file.readline()
    print("count:", count)
    print('total:', total)
    file.close()
except ValueError:
    print("Value Error occurred")
except IOError:
    print("IO error occurred")
except:
    print("An Error occurred")




