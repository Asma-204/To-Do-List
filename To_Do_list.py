import datetime #datetime builtin module he jiske functions use krny ki python se access li jaa rhi hai
import json  #json B-I module he jo javascipt ka format istmal krna allow krta hai(universal format)
import os  #another B-I module file handlig k liye. operating system se related toolbox ki access
FILENAME="tasks.json"  #ek file create hui jisko initialize bhi kiya gya. cap me likhny se ye constant bna diya gyahai.
if os.path.exists(FILENAME): #Agar FILENAME naam ki file ya folder maujood hai, to neeche ka code chalao.
    with open (FILENAME,"r") as file: #File FILENAME ko read mode mein khol kar file naam se use karo. Jab kaam khatam ho jaye to file automatically close ho jaye.
        todo_list= json.load(file) # .load Function jo JSON file se data read karta hai phir usko python smjhny k layak dict ya list me change krna.
else:
    todo_list=[] #agar if true ni he to ek todo list k variable main empty list create ki ab file khud hi create ho jaye gi
def save_tasks(): # saving k liye ek function bna diya kiu k program me br br is ka use hona hai
    with open(FILENAME,"w") as file: # "w" mode me file open krny se agr file nahi bhi exist krti to ni create ho.
        json.dump(todo_list,file) # File tasks.json ko write mode mein kholo, aur todo_list mein jo data hai usay JSON format mein file ke andar likh do. 
        #   json.dump  Python object ko JSON format mein file ke andar likhta hai    
while True: 
    print("\n---to do list---")
    print("1. enter task")
    print("2. view task")
    print("3. Delete task")
    print("4. edit task")
    print("5. exit")
    choice=int(input("Enter your choice 1-5: "))
    if choice==1:
        task=input("enter task\n") # ek var bnaya task us me input li  
        time_added=datetime.datetime.now().strftime("%y-%m-%d %H-%M")# exact time bhi list main sath likhny k liye 
        tasks={"text":task,"time":time_added} #input ko is Dictionary me store kra liya. Ek nayi dictionary banti hai
        todo_list.append(tasks) # phir Us dictionary ko task list (list of tasks) mein add kiya jata hai "todo_list me add kro tasks"
        save_tasks()   
        print("Task Added!")
    
    elif choice==2:
        if not todo_list:
            print("no tasks yet!") 
        else:
            print("your tasks")
            for i, task in enumerate(todo_list,start=1):# i ka mtlb hai k list me mjood idx,or task actual task hai
                print(f"{i}.{task['text']}(added:{task['time']})")
            #dictionary main ek to hum text add kr rhy_ dusra time
    elif choice==3:
        if not todo_list: 
            print("no task to delete!")
        else:
            print("Delete Options...")
            print("1. delete a specific task")
            print("2. delete list")
            sub_choice=int(input("Enter your choice 1 or 2: "))
            if sub_choice==1:
                print("which task you want to delete?")
                for i,task in enumerate(todo_list,start=1):
                  print(f"{i}.{task['text']}(added:{task['time']})") #{task['text']} → Insert ho raha hai task dictionary ka "text" value
                     #f" string ke andar variables ka value dikhana
                try:
                   task_num=int(input("Enter task number: "))    
                   if task_num<=len(todo_list) and task_num>=1:
                      deleted_task=todo_list.pop(task_num -1)#user ka number – 1 = correct Python index
                      save_tasks()
                      print("Task deleted...!")
                   else:
                      print("Invalid task number")    
                except IndexError:
                    print("Enter a valid task number")  
            elif sub_choice==2:
                confirm=input("are you sure you want to delete all tasks yes/no: ")
                if confirm== "yes":
                    todo_list.clear()
                    save_tasks()
                    print("tasks deleted")
                else:
                    print("cancelled...")    
    elif choice==4:
        if not todo_list:
            print("No tasks to edit")
        else:   
            for i, task in enumerate(todo_list, start=1):
                 print(f"{i}.{task['text']}")
            try:
                 num=int(input("enter task number to edit:  "))
                 if 1<=num<=len(todo_list):
                     new_text=input("enter new task text:  ")
                     todo_list[num-1]['text']=new_text
                     save_tasks()
                     print("Task updated..!")
                 else:
                     print("invalid task number ")    
            except IndexError:      
                     print("please enter a valid number ") 
                                
    elif choice==5:
        print("exiting and saving tasks...!")
        save_tasks()
        exit()
        break
    else:
        print("Invalid choice. Enter number between 1-5: ")

        # PROGRAM_ENDED