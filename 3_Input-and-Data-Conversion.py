# learn about input and data conversion

str_num_a = input("Enter the first number: ")
str_num_b = input("Enter the second number: ")

num_a = int(str_num_a)
num_b = int(str_num_b)

print(type(num_a))
print(type(num_b))

total = num_a + num_b
print(total)

# ----------------------------------------------------------
# Data types
# 1 str()
# 2 int()
# 3 float()
# 4 bool()
# ------------------#
# 5 list()
# 6 tuple()
# 7 set()
# 8 dict()

# ----------------------------------------------------------

# 📊Data Conversion

# number

x = 10

str_x = str(x)  # int -> string
float_x = float(x)  # int -> float
bool_x = bool(x)  # int -> bool(true), because non-zero
bool_neg_x = bool(0)  # int -> bool(false), because zero

# string

s = "123"

int_s = str(s)  # str -> int
float_s = float(s)  # str -> float
bool_s = bool(s)  # str -> bool(true), because non-empty
bool_empty = bool('')  # str -> bool(false), because empty

# booleans

bool_true = bool(1)  # true  (because non-zero
bool_false = bool(0)  # false (because zero
bool_list = bool([])  # false (because empty
bool_dict = bool({})  # false (because empty
bool_str = bool("hello")  # true  (because not empty
