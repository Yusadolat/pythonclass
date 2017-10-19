#Example of a python exception

student_details = {

    'first_name' : 'Yusuf',
    'age' : 34,
    'class' : 'pre'
}

try:
    lastname = student_details['last_name']
except KeyError: #The will handle the KeyError Exception
    print("Error finding Lastname")

except Exception: # This will handle any type of error
    print("Unknown Error")

print("This code execute")