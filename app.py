x = '2'
y = 5

try:
    z = x + y
except TypeError:
    print("sorry you can't add a string to an int")
except:
    print('something bad has happened get help')
finally:
    print('I will always happen, error or no error')