import re

pattern = re.compile(r'\w*th\w*')
result = pattern.findall('Python is the best')
print(result)  # ['Python', 'the']

result2 = pattern.findall('Cython is the thing')  # ['Cython', 'the', 'thing']
print(result2)  # ['Cython', 'the', 'thing']
