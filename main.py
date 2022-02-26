import math


def reverse_base_conversion(number, base):
  result = 0
  digit = 0 
  midnumber = number
  while midnumber != 0:
    result += (midnumber % 10) * (base**digit)
    midnumber = (midnumber - midnumber % 10) / 10
    digit += 1
  return int(result)


def legalnumberinbase(number, base):
  midnumber = number
  result = True
  while midnumber != 0:
    result = result and (midnumber % 10 < base)
    midnumber = (midnumber - midnumber % 10) / 10
  return result


def base_conversion(number, base):
  result = 0
  digit = 0
  if base > 10:
    print('There is no support for this function yet until hexadecimal numbers are implemented, please give 3-5 business days.')
    #insert thingy thing here
  elif base < 2:
    print('An error has occurred in the code, check all features having to do with base if you are the developer.')
  elif isinstance(base, int):
    while int(number) > 0:
      result += (int(number) % (base)) * (10**digit)
      digit += 1
      number = (number - (int(number) % (base))) / base
    return result
  else:
    return result

number = 0
base = 10
multi = 1
numberbase10 = reverse_base_conversion(number, base)
sp1 = False

def sp1():
if multi>5:
  sp1=True
  return "Success"
else:
  return "Nope"


def megascaling(x):
  if x<100:
    return 1
  else:
    y=(x-99)//5
    z=(x-99)%5
    result=1
    for i in range(0,y):
      result*=(1.01+.002*i)**5
    result*=(1.01+.002*y)**z
    return result

def scaling(x):
  if x<25:
    return 1
  elif x<50:
    return (1.1)**((x-20)//5)
  elif x<100:
    return (1.1)**((x-20)//5)*(1.5)**((x-40)//10)
  else:
    return (1.1)**((x-20)//5)*(1.5)**((x-40)//10)*megascaling(x)

def multi_formula(multii):
  global number
  global base
  global numberbase10
  global multi
  if multii==multi+1: 
    x=multii-2
    y=x%2
    z=x//2
    result=z*81+y*40+81
    return base_conversion(result*scaling(x),3)
  elif sp1 and multii>multi:
    x=multii-2
    y=x%2
    z=x//2
    result=z*81+y*40+81
    w=multi_formula(multi+1)
    return w+(result-w)*2
  else:
    "Nope"
    

def valid_count(x):
  global number
  global base
  global numberbase10
  global multi
  return x == base_conversion(numberbase10 + multi, base)

def digits(numbert):
  number=str(numbert)
  int_list = []
  for i in range(len(number)):
    int_list.append(int(number[i]))
  return int_list
  
def reverse_digits(digits):
  result=0
  for i in range(len(digits)):
    result+=10**(len(digits)-i-1)*int(digits[i])
  return result
  
def round_down(number,base):
  x=digits(number)
  y=[]
  for i in range(len(x)):
    if x[i]>=base:
      new_item=base-1
    else:
      new_item=x[i]
    y.append(new_item)
  return reverse_digits(y)

def base_formula(x):
  global number
  global base
  global numberbase10
  global multi
  values=[0,0,0,1000,400,300,250,200,150,100]
  return values[x]


def update():
  global number
  global base
  global numberbase10
  global multi
  numberbase10=reverse_base_conversion(number,base)

def c(x):
  global number
  global base
  global numberbase10
  global multi
  if valid_count(x):
    number = x
    update()
    return x

def b(x):
  global number
  global base
  global numberbase10
  global multi
  if base-1==x and x>=3:
    if number>=base_formula(x):
      base=x
      number=0
      update()
      return "Success"
    else:
      return "Nope"
  else:
    return "Nope"

def m(x):
  global number
  global base
  global numberbase10
  global multi
  if isinstance(x,int):
    if number>=multi_formula(x) and x==multi+1 and base==3:
      multi=x
      base=10
      number=0
      update()
      return "Success"
    else:
      return "Nope"
  else:
    return "Nope"