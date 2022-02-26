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
numberbase10 = reverse_base_conversion(number, base)

def valid_count(x):
  global number
  global base
  global numberbase10
  return x == base_conversion(numberbase10 + 1, base)

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
  values=[0,0,0,1000,400,300,250,200,150,100]
  return values[x]

def update():
  global number
  global base
  global numberbase10
  numberbase10=reverse_base_conversion(number,base)

def c(x):
  global number
  global base
  global numberbase10
  if valid_count(x):
    number = x
    update()
    return x

def b(x):
  global number
  global base
  global numberbase10
  if base-1==x and x>=3:
    if number>=base_formula(x):
      base=x
      number=0
      update()
      return 'Success'
    else:
      return 'Nope'
  else:
    return 'Nope'