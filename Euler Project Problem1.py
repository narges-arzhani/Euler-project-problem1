n=int(input('number='))

def multiples(n):
    if n%3==0 or n%5==0:
        return True
    else:
        return False
sum=0
for n in range (1,n):
    if multiples(n):
        sum=sum+n
print(sum)