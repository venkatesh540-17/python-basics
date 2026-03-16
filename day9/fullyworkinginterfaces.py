output = """Interface       IP-Address      Status     Protocol
Fa0/0           192.168.1.1     up         up
Fa0/1           unassigned      down       down
Fa0/2           10.0.0.1        up         down
Fa0/3           172.16.1.1      up         up"""

lines = output.split("\n")

for line in lines:
    parts = line.split()

    if  parts[2] == "up" and parts[3] == "up":
        print(parts[0], "is fully operational")