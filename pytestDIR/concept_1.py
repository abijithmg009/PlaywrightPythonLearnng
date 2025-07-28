from s3transfer import random_file_extension

new_list = [1,2,3,4,5]

dict= [{"name":"Alice","age":18},
       {"name":"bob","age":20}]


print(dict[0]["name"])



add = lambda x,y:x+y
d = add(2,4)
print(d)


print_list = list(map(lambda x:x*x,new_list))
print(new_list)
print(print_list)

#filter
print(list(filter(lambda x:x%2 !=0,new_list)))


#sorting in list

num = [3,2,4,1,0]
print(sorted(num))
print(num[::-1])
n = len(num)
for i in range (n):
    swapped = False
    for j in range(0,n-i-1):
        if num[j] >num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            swapped = True

    if not swapped:
        break
print(num)


num1 = [4,3,5,1,2,3,5]
rev_num1 = []

lenth = len(num1)

for i in range(lenth-1,-1,-1):
    rev_num1.append(num1[i])

print(rev_num1)




