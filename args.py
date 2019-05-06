import sys
import pip._vendor.requests as requests

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting
r = requests.get('https://google.com')
print(r.status_code)

