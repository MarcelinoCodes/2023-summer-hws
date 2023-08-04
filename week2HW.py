#problem 1 Aplhabet Slices
alphabet=['a','b','c','d','e','f','g','h','i','j']
print(len(alphabet)) #should print 10

#problem 2
# Solve rapper names here
rappers = ['lil wayne', 'nicki minaj', 'drake']

for i in range(len(rappers)):
  rappers[i]=rappers[i].title()

print(rappers)

#problem 3
def OddOrEven(a):
  if a%2==0:
    return True
  else:
    return False
  
OddOrEven(3)
OddOrEven(4)
  
  
#problem 4 sum and average  
# Solve problem here:

my_list = [1, 5, 10, 55, 88, 44, 42, 50, 20, 38]
list_sum = 0
for i in range(len(my_list)):
  list_sum += my_list[i]
list_avg = list_sum/len(my_list)

import numpy as np

secndsum=np.sum(my_list)
secndmean=np.mean(my_list)
print(secndsum,secndmean)

# Keep this as your last line in this cell.
print(list_sum, list_avg)

#problem 5
def fizz(a):
  if a%3==0 and a%5==0:
    return "fizzbuzz"
  elif a%3==0:
    return "fizz"
  elif a%5==0:
    return "buzz"
  else:
    return None

fizz(3)



#problem 6
def duplets(a):
  b=[]
  for i in a:
    if i not in b:
      b.append(i)
  return b

names=["Michele", "Robin", "Sara", "Michele","Michele"]
duplets(names) 
  
#problem 7

def fal(a):
  b=[]
  if len(a)<3:
    return a
  else:
    b.append(a[0])
    b.append(a[len(a)-1])
    return b
a=[5, 10, 99, 20, 25]   
fal(a)    

#problem 8
def your_function(a, b, c):
  # 3 choose 2 if statements
  if a>b and a>c:
    return a
  if b>a and b>c:
    return c
  if c>a and c>b:
    return c
your_function(1, 5, 10) 
