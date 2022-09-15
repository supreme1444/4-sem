n = float(input("Число"))
t = float(input("Точность"))
chislo=n/7
n=0
while t<1:
    t*=10
    n+=1
print(f'{chislo:.{n}}')

