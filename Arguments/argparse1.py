import argparse

parser = argparse.ArgumentParser(description='Process some integers')  #creating a ArgumentParser object
parser.add_argument('integers', metavar='N', type=int, nargs='+', help="an integer for the accumulator") 
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the intergers(default: find the max')
args = parser.parse_args()
print(args.accumulate(args.integers))