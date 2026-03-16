input="""Vlan    Mac Address       Type        Ports
1       0001.434c.2376    DYNAMIC     Fa0/1
1       0002.abcd.1111    DYNAMIC     Fa0/2"""

lines=input.split("\n")

for line in lines:
    parts=line.split()
    if "Vlan" not in line:
        mac=parts[1]
        interface=parts[3]
        print(mac,interface)