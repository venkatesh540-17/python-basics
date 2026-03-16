input="""Interface       IP-Address      Status     Protocol
Fa0/0           192.168.1.1     up         up
Fa0/1           unassigned      down       down
Fa0/2           10.0.0.1        up         up"""
#to print only interfaces are up:

lines=input.split("\n")

print(lines)
for line in lines:
    if "up" in line and "Interface" not in line:
        parts=line.split()
        interface=parts[0]
        ip = parts[1]
        print(interface,"is up in the ip ",ip)