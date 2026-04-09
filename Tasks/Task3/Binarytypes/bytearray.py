#bytearray is a mutable sequence of bytes. It is a built in data type for working with binary values.
a=bytearray(b'hello world')#it will create a bytearray object with the value 'hello world'.
a[0]=72#it will change the first byte of the bytearray object a to 72 which is the ascii value of 'H'.
print(a)#it will print the bytearray object a which is bytearray(b'Hello world').