# learn about input and data conversion

str_num_a  = input ("Enter the first number: ")
str_num_b = input ("Enter the second number: ")

num_a = int(str_num_a)
num_b = int(str_num_b)

print(type(num_a))
print(type(num_b))

total = num_a + num_b
print(total)