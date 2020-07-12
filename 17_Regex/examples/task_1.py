import re

s = ''

pattern = re.compile(r'^\w+')
result = pattern.match('Python is the best')
print(result)  # <re.Match object; span=(0, 6), match='Python'>
print(result.group(0))  # Python

result = pattern.match('Nah is the best')
print(result.group(0))  # None
