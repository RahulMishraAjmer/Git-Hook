#!/usr/bin/python

import sys

def main ():
    with open(sys.argv[1],"r") as fp:
	lines = fp.readlines()
	for line in lines:
            if line[0]=="keyword"
		print("Keyword found")
		sys.exit(0)
	    else:
		print("Keyword NOT found")
		sys.exit(1)

 if __name__=="__main__":
	main()
