import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="Increases output visibility", action="store_true")  #Action keyword, assign the value True or False
args = parser.parse_args()
if args.verbose:
    print("Verbosity turned on")