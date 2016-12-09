def course_room ():
    room_num={'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
    return room_num
def course_instructor ():
    instructor={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    return instructor
def course_time():
    time={'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}
    return time
def main():
    room=course_room()
    instructor=course_instructor()
    time=course_time()
    user_input=input("Enter Course Number: ")
    print("Room Number:",room[user_input])
    print("Instructor:",instructor[user_input])
    print("Course Time:",time[user_input])


main()