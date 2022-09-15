n = int(input("Integer: "))
factors = []
d = 2
m = n 
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
factors.append(n) 
print('{} = {}' .format(m, factors))

        

        
