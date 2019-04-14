# 1
def convert(miles):
  return miles * 1.609

# 2
def area(a, b):
  return a * b

# 3 (первый вариант - с использованием if)
def is_even(a):
  if a % 2 == 0:
    return True
  else:
    return False
  
# 3 (второй вариант - более короткий)
def is_even(a):
  return a % 2 == 0 # тоже возвращается bool