from cgi import print_arguments
from tokenize import Number


Number = [10,20,33,46,55,62,70]
result = list(filter (lambda X:(X%5==0),Number))
print ('Numbers that are divisible by 5 are):