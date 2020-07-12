import re

result = re.findall(r'\w*th\w*', 'Python is the best')
print(result)  # ['Python', 'the']
print(type(result))


result = re.findall(r'\w*thwww\w*', 'Python is the best')
print(result)  # ['Python', 'the']
print(type(result))