# import db/manager here.
from db.manager import add_task, change_priority, complete_task, get_all_tasks, is_tasks_file_exists, remove_task, search, sort, update_desc

def showhelp():
    print('usage: python main.py <options>')
    print('===== options =====')
    print('-h or --help to print this menu.')
    print('-l or --list to list all tasks.')
    print('-a or --add <DESCRIPTION> to add a new task')
    print('-p or --priority <NUMBER> to assign a priority to a new task. Must use with -a or -s.')
    print('-r or --remove <ID> remove a task.')
    print('-c or --complete <ID> mark a task as complete.')
    print('-cp or --changepriority <ID> <NUMBER> change an existing task\'s priority.')
    print('-u or --update <ID> <DESCRIPTION> update an existing task\'s description.')
    print('-s or --search <OPTIONS> search a task by options.')
    print('-t or --sort show sorted list of tasks by increasing order of priority.')
    print('-d or --desc decreasing order of priority. Must use with -t.')
    print('-i or --id <ID> task ID. Must use with -s for search task with ID.')
    print('-dp or --description <TEXT> task description. Must use with -s for search task with description.')

# command to list all tasks
def list_all_tasks_cmd():
    if not is_tasks_file_exists(): return "TODO List empty. Add some tasks."
    out = get_all_tasks(); output = ""
    if out == None: return "TODO List empty. Add some tasks."
    for item in out:
        output += 'ID: %s DESC: %s PRIORITY: %s STATUS: %s' %(item.split(",")[0], item.split(",")[1], item.split(",")[2], item.split(",")[3])
    return output

# command to add a task
def add_task_cmd(task, priority):
    if (task == None or task == ''): return "Failed to add task"
    if (priority <= 0): return "Failed to add task"
    return 'Task added and assigned ID %s' %add_task(task, priority)

# command to delete a task
def remove_task_cmd(id):
    output = remove_task(id)
    if output:
        return "Removed task ID %s" %id
    return "Failed to remove task ID %s" %id

# command to complete a task
def complete_task_cmd(id):
    output = complete_task(id)
    if output:
        return "Task %s completed" %id
    return "Task %s could not be completed" %id

# command to edit task priority
def change_priority_cmd(id, priority):
    output = change_priority(id,priority)
    if output:
        return "Changed priority of task %s to %s" %(id, priority)
    return "Priority of task %s could not be changed" %id

# command to edit task description
def update_cmd(id, desc):
    output = update_desc(id, desc)
    if output:
        return "Task %s updated" %id
    return "Failed to update task %s" %id

# command to search a task by id, description, or priority
def search_cmd(id, desc, priority):
    output = search(id, desc, priority)
    if output != "":
        return output
    return "Task not found"

# command to sort the tasks in specified order
def sort_cmd(order):
    if (order == "-d"): return sort(2)
    else: return sort(1)
