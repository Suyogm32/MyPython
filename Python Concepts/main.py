import sys
out=open("target.txt",'w')
print("Systems Arguments are ",sys.argv,file=out)
print("Version of system is",sys.version,file=out)
print("System version info ",sys.version_info,file=out)

print("Standard I/O streams")
print(" The standard input stream is ",sys.stdin,file=out)
print(" The standard output stream is ",sys.stdout,file=out)
print(" The standard Error stream is ",sys.stderr,file=out)

print("Largest integer of variable is ",sys.maxsize,file=out)
print("An integer giving the value of the largest Unicode code point",sys.maxunicode,file=out)

print("Python path in system is ",sys.path)
