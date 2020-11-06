#!/usr/bin/python3

import sys

def main ():
        with open(sys.argv[1],"r") as fp:
                lines = fp.readlines()
                my_str = "bug"
                if lines[0].lower().find("bug")== 0:
                        print("Keyword found")
                else:
                        print("Keyword NOT found")
        sys.exit(1)

if __name__=="__main__":
        main()
