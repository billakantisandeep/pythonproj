from __future__ import print_function
import sys
print(sys.argv, len(sys.argv))
script_name = sys.argv[0]
print(script_name)
filename = sys.argv[1]
print(filename)
users_args = sys.argv[1:]
print(users_args)

