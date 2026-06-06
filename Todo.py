class TodoList:
    
    def __init__(self):
        self.tasks=[]

        
    def add_task(self,title,priority):
        if priority not in ["high","medium","low"]:
            raise ValueError(f"{priority} is an invalid priority.")
        task = {
        "title": title,
        "priority": priority,
        "completed": False
        }
        # task={}
        # task["title"]=title
        # task["priority"]=priority
        # task["completed"]=False
        self.tasks.append(task)
        # return self.tasks
        # return self.tasks[0]["title"]

        
    def complete_task(self,title):
        for task in self.tasks:

            if task["title"] == title:
                if  task["completed"]== True:
                    raise ValueError(f"The task {title} is already completed.")
                task["completed"]=True
                print(f"The task {title} is completed now.")
                return
        raise ValueError(f"The task {title} was not found in the TODO.")
            

        

        
    def delete_task(self,title):

        for task in self.tasks:
            if task["title"]==title:
                self.tasks.remove(task)
                return
        raise ValueError(f"{title} not found.")
        
    def show_tasks(self):
        print(f"All the Tasks in the Todo List : \n")

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task : {task["title"]} |  Priority : {task["priority"]}  |  Status : {status}")

        
    def save_tasks(self):

        with open("tasks.txt","w+") as f:
            for task in self.tasks:
                f.write(f"{task['title']} | {task['priority']} | {task['completed']}\n")
            print(f"Task saved successfully. ")
        
    def load_tasks(self):
        try:
            with open("tasks.txt","r") as f:
                data=f.readlines()
                print(f"The task in a Todo List are:\n ")
                for task in data:
                    print(f"{task.strip()}")
        except FileNotFoundError :
            print("NO saved task found .")



todo = TodoList()

# print(todo.add_task("Build Flask app", "high"))
try:

    todo.add_task("Build Flask app", "high")
    todo.add_task("Learn SQL", "medium")
    todo.add_task("Read Clean Code", "low")
    todo.add_task("Learn SQL", "extreme")  # should fail — invalid priority
except ValueError as e:
    print(f"Error : {e}")

try:

    todo.complete_task("Learn SQL")
    todo.complete_task("LearnL")
except ValueError as e:
    print(f"Error : {e}")


try:

    todo.complete_task("Learn SQL")        # should fail — already done
except ValueError as e:
    print(f"Error : {e}")


try:
 
    todo.delete_task("Read Clean Code")
    todo.delete_task("Invisible Task")     # should fail — not found
except ValueError as e:
    print(f"Error : {e}")

todo.show_tasks()
todo.save_tasks()
todo.load_tasks()