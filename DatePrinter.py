

def date(user_date):
    user_date=user_date.split('/')
    day_portion = user_date[1]
    year_portion=user_date[2]
    if user_date[0]==('01'):
        month="January"
    elif user_date[0]==('02'):
        month="February"
    elif user_date[0]==('03'):
        month="March"
    elif user_date[0]==('04'):
        month="April"
    elif user_date[0]==('05'):
        month="May"
    elif user_date[0]==('06'):
        month="June"
    elif user_date[0]==('07'):
        month="July"
    elif user_date[0]==('08'):
        month="August"
    elif user_date[0]==('09'):
        month="September"
    elif user_date[0]==('10'):
        month="October"
    elif user_date[0]==('11'):
        month="November"
    elif user_date[0]==('12'):
        month="December"

    return month+' '+day_portion+','+' '+year_portion+'.'
def main():
    user_date = input("please enter date in mm/dd/yyyy format: ")
    print(date(user_date))


main()