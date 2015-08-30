# hellovirus
Self-replicating program - unloaded worm

This is a demonstration of how easy it is to write a self-replicating program. 
This virus will infect all files with names ending in FILETYPE in the directory in
which you execute an infected file. If you send an infected file to someone else and 
they execute it, their FILETYPE files will be damaged also.

Note that this is a safe virus (for educational purposes only) since it does not 
carry a harmful payload. All it does is prints out this message and comment out the
code in FILETYPE files.
