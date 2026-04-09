#memory view is a built in function that returns a memory view object which is a view of the memory of the original object. It is a built in data type for working with binary values.
a=bytearray(b'hello world')#it will create a bytearray object with the value 'hello world'.
mv=memoryview(a)#it will create a memory view object of the bytearray object a and assign it to mv.
print(mv)#it will print the memory view object mv which is <memory at 0x0000021B8C8B8E80>.memory location may vary.