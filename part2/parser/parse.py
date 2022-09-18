# import utils.commands here

# parse the command line arguments and execute the appropriate commands.
from part2.db.manager import get_all_tasks
from part2.utils.commands import add_task_cmd, list_all_tasks_cmd, remove_task_cmd, showhelp


def parseArgs(args):
    i = 0
    if (len(args) == 1): return "Missing Required argument. Type -h to seek help"
    while (i < len(args)):
        if (args[i] == "-h" or args[i] == "--help"):
            return showhelp()
        if (args[i] == "-l" or args[i] == "--list"):
            return "".join(get_all_tasks())
        if (args[i] == "-a" or args[i] == "--add"):
            try:
                if ((args[i+2] != "-p" and args[i+2] != "--priority") or (args[i+1] == "-p" and args[i+1] != "--priority")): 
                    return "Error: Incorrect priority option"
            except: return "Error: Incorrect priority option"
            try: 
                if (not str(args[i+3]).isnumeric()): return "Priority must be integer"
            except IndexError: return "Error: Cannot add a task with empty priority"
            try:
                args[i+4]; return "Error: Found extraneous options"
            except: pass
            return add_task_cmd(args[i+1], int(args[i+3]))
        if (args[i] == "-r" or args[i] == "--remove"):
            try:
                if (not str(args[i+1]).isnumeric()): return "Task ID must be a number"
            except: return "Task ID missing"
            try:
                args[i+2]; return "Error: Found extraneous options"
            except: pass
            return remove_task_cmd(args[i+1])
        i += 1
