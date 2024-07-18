import matplotlib.pyplot as plt
n=int(input('Input a positive integer:'))

sequence=[n]
print(n)
while n>1:
    if n%2==0:
        n=n//2
        print(n)
    elif n%2!=0:
        n=(3*n)+1
        print(n)
    else:
        print('break')
    sequence.append(n)
x=range(len(sequence))
y=sequence
plt.plot(x,y)
plt.xlim(0, len(sequence) - 1)
plt.ylim(0, max(sequence))
plt.show()
print('Done')