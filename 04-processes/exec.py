# exec example in Python

import os

print("Hello! I am starting a new process...")
os.execl('/bin/ls', 'ls', '-l') # Replace the current process with a new one
print("I started the new process!") # This will never be executed