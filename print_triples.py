#!/usr/bin/env python3

start= 0
end  = 100

print("Preparing to print numbers {}..{}".format(start,end))

for num in range(start,end+1,1):
    star = ""
    if num > 0 and (num % 3) == 0:
        star = "*"
#    if num == 0:
#        star = ""
        
    print(num,star)
    
# Your code goes next
