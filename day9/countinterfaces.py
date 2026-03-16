output = """Interface       IP-Address      Status     Protocol
Fa0/0           192.168.1.1     up         up
Fa0/1           unassigned      down       down
Fa0/2           10.0.0.1        up         up"""
lines = output.split("\n")
count = 0

for line in lines:
    if "Fa" in line:
        count += 1

print("Total Interfaces:", count)