list=[1,2,3,4,5]
n=2
start=0
end=len(list)-1

def reverse(start,end):
    while end>start:
        list[start], list[end] = list[end], list[start]
        start = start + 1
        end = end-start


reverse(start,end)
print(list)
reverse(start,n-1)
print(list)
reverse(n,end)
print(list)