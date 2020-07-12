import re

result = re.search(r'\w*th\w*', 'Python is the best')
print(result)  # <re.Match object; span=(0, 6), match='Python'>
print(result.group(0))  # Python
print(result.start())  # 0
print(result.end())  # 6


result = re.search(r'(\w*)th\w*', 'Python is the best')
print(result)  # <re.Match object; span=(0, 6), match='Python'>
print(result.group(0))  # Python
print(result.group(1))  # Py
#print(result.group(2))  # Python
print(result.start())  # 0
print(result.end())  # 6


