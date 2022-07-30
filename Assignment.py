
A = 20
B = 6
def divide(A,B):
    try:
        print (A/B)   
    except Exception as e:
        print ('Incorrect, Do not divide by zero, e')
    
    finally:
        print ('This is correct, go ahead!')
        
divide(20,6)







A = 12
B = 3
def divide(A,B):
    try:
        print (A/B)
    except ZeroDivisionError as e:
        print('Cant divide by zero')
    except TypeError as e:
        print('cant divide different types of values')
    except Exception as e:
        print('Error, please check again')
        
    finally:
        print('Successful!')
        
divide(12,3)