def the_file():
    file_name = input("Enter file: ")
    return file_name
def main():
    open_text=open(the_file(), 'r')
    read=open_text.readline()
    count=0
    while read !="":
        count+=1
        print(count,": ", read.rstrip(),sep="")
        read=open_text.readline()



main()
