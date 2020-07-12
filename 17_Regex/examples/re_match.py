import re

result = re.match(r'(P)(yt)hon', 'Python is the best')
print(result)  # <re.Match object; span=(0, 6), match='Python'>
print(result.groups())  # ('P', 'yt')
print(result.group())   # Python
print(result.group(1))  # P
print(result.group(2))  # yt
print(result.start())   # 0
print(result.end())     # 6

result = re.match(r'the', 'Python is the best')
print(result)  # None

result = re.match(r'the', 'the Python is the best')
print(result)  # <re.Match object; span=(0, 3), match='the'>


