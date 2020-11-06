#!/usr/bin/python3

import sys

def main ():
        with open(sys.argv[1],"r") as fp:     # sys.argv[1] is the .git/COMMIT_EDITMSG file that holds the commit message
                lines = fp.readlines()
                my_str = "bug"
                if lines[0].lower().find("bug")== 0:
                        print("Keyword found")
                        sys.exit(0)
                else:
                        print("Keyword NOT found")
                        sys.exit(1)
                        
if __name__=="__main__":
        main()
