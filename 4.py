mn = open(r'C:\Users\supre\OneDrive\Рабочий стол\Новая папка (11)\Новая папка (4)\text1.txt')
line1=mn.readline()
print(f'{line1}')
mn1 = open(r'C:\Users\supre\OneDrive\Рабочий стол\Новая папка (11)\Новая папка (4)\text2.txt')
line2=mn1.readline()
print(f'{line2}')
line=f'{line1}+{line2}'
print(f'line: {line}')
lst = line.split('+')
print(f'lst: {lst}')
res=0
for x in lst:
    if '-' in x:
        a,b = x.split('-')
        res+=int(a)-int(b)
    else:
        res+=int(x)
print(res)

with open(r'C:\Users\supre\OneDrive\Рабочий стол\Новая папка (11)\Новая папка (4)\text3.txt', mode='w') as f:
    f.write(str(res))
    #f.close()



    