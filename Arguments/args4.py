import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type =int, help="Display the square of the given number")
parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase the visiblity of the output") #Action  flag similar to store_true 
#Default keyword makes by default the position argument can be 0 
args = parser.parse_args()
answer = args.square**2
if args.verbose >= 2:
    print (" the square of {} equals to {}".format(args.square, answer))
elif args.verbose >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)