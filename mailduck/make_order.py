import os
import sys
import yaml
import random

def show_help():
    if any([x == "--help" or x == "-h" for x in sys.argv]):
        print(f"Usage: {sys.argv[0]} map n")
        print("  map - map path")
        print("  k   - number of packages")
        sys.exit(0)

def main():
    Y = None
    with open(sys.argv[1]) as file:
        Y = yaml.safe_load(file)

    M = Y["tiles"]

    # Candidates
    C = []

    n, m = len(M), len(M[0])
    for i in range(n):
        for j in range(m):
            if M[i][j].startswith("straight"):
                C.append((j, i))

    k = int(sys.argv[2])
    random.shuffle(C)
    print("./maps/" + os.path.basename(sys.argv[1]))
    for i in range(k):
        print(C[i][0], C[i][1])

if __name__ == "__main__": show_help(); main()
