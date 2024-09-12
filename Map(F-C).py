# map(): Convert a list of Fahrenheit temperatures to Celsius
def faren_celsius(f):
  return (f-32)* 5/9

def convert_temperature(lst):
  return list(map(faren_celsius, lst))

print(convert_temperature([22, 34, 46]))
