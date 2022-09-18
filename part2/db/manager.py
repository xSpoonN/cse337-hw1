import os

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')

# creates tasks file is none exists
def create():
    if (not is_tasks_file_exists()):
        file = open(tasks_file, 'w')
        file.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
        file.close()
        return True
    return False

# check if tasks file exists
def is_tasks_file_exists():
    return os.path.exists(tasks_file)

# adds a task to the task file and returns the task id.
def add_task(desc, priority):
    file = open(tasks_file, 'r+')
    upto = 0
    for line in file:
        upto += 1
    file.write('%s,%s,%s,Incomplete\n' %(upto, desc, priority))
    file.close()
    return upto

# returns list of tasks in the task file.
def get_all_tasks():
    if not is_tasks_file_exists(): return None
    file = open(tasks_file, 'r')
    out = file.readlines()[1:]
    file.close(); return out

# remove a task from the task file.
def remove_task(id):
    if id == None: return False
    file = open(tasks_file, "r")
    modify = file.readlines(); matched = False; i = 0
    while i < len(modify):
        if not matched:
            line = modify[i].split(",")
            if line[0] != "ID" and int(line[0]) == id:
                modify.remove(modify[i])
                i -= 1; matched = True
        else: 
            modify[i] = str(int(modify[i].split(",")[0])-1) + "," + ",".join(modify[i].split(",")[1:])
        i += 1
    if not matched: return False
    file.close(); file = open(tasks_file, "w")
    file.write("".join(modify)); file.close()
    return True

# complete a task in the task file.
def complete_task(id):
    if id == None: return False
    file = open(tasks_file, "r")
    modify = file.readlines(); completed = False; i = 0
    while i < len(modify):
        line = modify[i].split(",")
        if line[0] != "ID" and int(line[0]) == id:
            completed = True
            line[3] = "Complete\n"
            modify[i] = ",".join(line)
        i += 1
    if not completed: return False
    file.close(); file = open(tasks_file, "w")
    file.write("".join(modify)); file.close()
    return True

# change the priority of a task in the task file.
def change_priority(id, priority):
    if id == None or priority == None or priority <= 0: return False
    file = open(tasks_file, "r")
    modify = file.readlines(); modified = False; i = 0
    while i < len(modify):
        line = modify[i].split(",")
        if line[0] != "ID" and int(line[0]) == id:
            modified = True
            line[2] = str(priority)
            modify[i] = ",".join(line)
        i += 1
    if not modified: return False
    file.close(); file = open(tasks_file, "w")
    file.write("".join(modify)); file.close()
    return True

# update the task description of a task in the task file.
def update_desc(id, desc):
    if id == None or desc == None or desc == '': return False
    file = open(tasks_file, "r")
    modify = file.readlines(); modified = False; i = 0
    while i < len(modify):
        line = modify[i].split(",")
        if line[0] != "ID" and int(line[0]) == id:
            modified = True
            line[1] = desc
            modify[i] = ",".join(line)
        i += 1
    if not modified: return False
    file.close(); file = open(tasks_file, "w")
    file.write("".join(modify)); file.close()
    return True

# search for a task in the task file.
def search(id, desc, priority):
    if desc == '': return False
    file = open(tasks_file, "r")
    search = file.readlines(); out = ""
    if (id == None and desc == None and priority == None): return out
    for item in search:
        line = item.split(",")
        if (id != None and str(id) != line[0]): continue
        if (desc != None and desc.lower() != line[1].lower()): continue
        if (priority != None and str(priority) != line[2]): continue
        out += ",".join(line)
    return out

# sort the tasks in the task file. Default order is 1.
def sort(order=1):
    file = open(tasks_file, "r")
    search = file.readlines(); out = ""
    if order == 1:
        while len(search) != 1:
            min = int(search[1].split(",")[2]); index = 1
            for i in range(1, len(search)):
                line = search[i].split(","); 
                if line[0] != "ID" and int(line[2]) < min:
                    min = int(line[2]); index = i
            
            out += search[index]; search.remove(search[index])
        return out
    else:
        while len(search) != 1:
            max = int(search[1].split(",")[2]); index = 1
            for i in range(1, len(search)):
                line = search[i].split(","); 
                if line[0] != "ID" and int(line[2]) > max:
                    max = int(line[2]); index = i
            
            out += search[index]; search.remove(search[index])
        return out
