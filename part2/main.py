import sys, os
sys.path.insert(1, os.getcwd())
from parser.parse import parseArgs

args = sys.argv
print(parseArgs(args))
