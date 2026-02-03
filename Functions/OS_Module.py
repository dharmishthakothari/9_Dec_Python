import os
import datetime
#print(os.getcwd())
#print(os.listdir("."))
#print(os.listdir("./List_Set_Tuple"))

print(datetime.date.today())
print(datetime.datetime.now())
cur_now=datetime.datetime.now()
print(cur_now.year)
print(cur_now.day)
print(cur_now.strftime("%d / %m / %Y"))