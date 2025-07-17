import pyttsx3
import time
import datetime
task={}
class Task_remainder:
    def __init__(self):
        self.main()
        self.message=None
        self.name=None
        self.time1=None

    def main(self):
        action=int(input(("""1. Create task 
                2. Edit task
                3. Delete task""")))
        
        if action==1:
            self.Create_task()
        elif action==2:
            self.Edit_task()
        elif action==3:
            self.Delete_task()
        else:
            print("selec valid action")
            self.main()
    
    def Create_task(self):
        self.name=input("please enter name of task ")
        self.message=input("Please enter custmised message which will play at task time")
        timein=input("please enter time in HH:MM format")
        self.time1=datetime.datetime.strptime(timein,"%H:%M").time()
        print("task is set for ",self.time1)
        task[self.name]={"message":self.message , "time":self.time1}

    def Edit_task(self):
        action=input("enter task name which you have to edit")
        if action in task.keys():
            edit=int(input("""1. to edit time
                       2. To edit message"""))
            if edit==1:
                timein=input("please enter time in HH:MM format")
                new_time=datetime.datetime.strptime(timein,"%H:%M").time()
                print("task time is set for ",new_time)
                task[action]["time"]=new_time

            elif edit==2:
                new_message=input("Please enter custmised message which will play at task time")
                task[action]["message"]=new_message

    def Delete_task(self):
        delete=input("enter name of task to delete")
        task.pop(delete)
task1=Task_remainder()

while True:
    now = datetime.datetime.now().replace(second=0, microsecond=0).time()

    for i in task.keys():
        if(task[i]["time"]==now):
            engine= pyttsx3.init()
            engine.say(task[i]["message"])
            engine.runAndWait()
    time.sleep(1)

