import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="Display the square of a given no.")
parser.add_argument("-v", "--verbose", type=int, choices = [0, 1, 2], help="Increase the visibility of the output")
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
    print("The square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
    print("{}^s == {}".format(args.square,answer))
else:
    print(answer)

