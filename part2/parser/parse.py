# import utils.commands here

# parse the command line arguments and execute the appropriate commands.
from part2.db.manager import gettasks
from part2.utils.commands import add_task_cmd, change_priority_cmd, complete_task_cmd, gettasks, remove_task_cmd, search_cmd, showhelp, sort_cmd, update_cmd


def parseArgs(args):
    i = 1
    if (len(args) == 1): return "Missing Required argument. Type -h to seek help"
    if (args[i] == "-h" or args[i] == "--help"):
        return showhelp()
    if (args[i] == "-l" or args[i] == "--list"):
        return "".join(gettasks())
    if (args[i] == "-a" or args[i] == "--add"):
        if (len(args) > 5): return "Error: Found extraneous options"
        try:
            if ((args[i+2] != "-p" and args[i+2] != "--priority") or (args[i+1] == "-p" and args[i+1] != "--priority")): 
                return "Error: Incorrect priority option"
        except: return "Error: Incorrect priority option"
        try: 
            if (not str(args[i+3]).isnumeric()): return "Priority must be integer"
        except IndexError: return "Error: Cannot add a task with empty priority"
        return add_task_cmd(args[i+1], int(args[i+3]))
    if (args[i] == "-r" or args[i] == "--remove"):
        if (len(args) > 3): return "Error: Found extraneous options"
        try:
            if (not str(args[i+1]).isnumeric()): return "Task ID must be a number"
        except: return "Task ID missing"
        return remove_task_cmd(args[i+1])
    if (args[i] == "-c" or args[i] == "--complete"):
        if (len(args) > 3): return "Error: Found extraneous options"
        try:
            if (not str(args[i+1]).isnumeric()): return "Task ID must be a number"
        except: return "Task ID missing"
        return complete_task_cmd(args[i+1])
    if (args[i] == "-cp" or args[i] == "--changepriority"):
        if (len(args) > 4): return "Error: Found extraneous options"
        try:
            if (not str(args[i+1]).isnumeric()): return "Task ID must be a number"
            if (not str(args[i+2]).isnumeric()): return "Priority must be a number"
        except: return "Task ID or priority missing"
        return change_priority_cmd(int(args[i+1]), int(args[i+2]))
    if (args[i] == "-u" or args[i] == "--update"):
        if (len(args) > 4): return "Error: Found extraneous options"
        try:
            if (not str(args[i+1]).isnumeric()): return "Task ID must be a number"
            args[i+2]
        except: return "Task ID or description missing"
        return update_cmd(int(args[i+1]), args[i+2])
    if (args[i] == "-s" or args[i] == "--search"):
        if (len(args) < 4): return "Search Criteria Missing"
        id = None; priority = None; desc = None; i += 1
        while i < len(args):
            if (args[i] == "-i" or args[i] == "--id"):
                try:
                    if (not str(args[i+1]).isnumeric()): return "search ID and priority must be integer."
                except: return "search ID and priority must be integer."
                if (id == None): id = int(args[i+1])
                i += 1
            elif (args[i] == "-dp" or args[i] == "--description"):
                try:
                    args[i+1]
                except: return "Description missing"
                if (desc == None): desc = args[i+1]
                i += 1
            elif (args[i] == "-p" or args[i] == "--priority"):
                try:
                    if (not str(args[i+1]).isnumeric()): return "search ID and priority must be integer."
                except: return "search ID and priority must be integer."
                if (priority == None): priority = int(args[i+1])
                i += 1
            else:
                if (id == None and priority == None and desc == None): return "".join(gettasks())
                else: return search_cmd(id, desc, priority)
            i += 1
        if (id == None and priority == None and desc == None): return "Search Criteria Missing"
        return search_cmd(id, desc, priority)
    if (args[i] == "-t" or args[i] == "--sort"):
        if (len(args) > 3): return "Error: Found extraneous options"
        try:
            if (args[i+1] != "-d" and args[i+1] != "--desc"): return sort_cmd(1)
            else: return sort_cmd("-d")
        except: return sort_cmd(1)