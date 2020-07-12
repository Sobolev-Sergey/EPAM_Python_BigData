import re

result = re.search(r'the', 'Python is the best')
print(result)  # <re.Match object; span=(10, 13), match='the'>
print(result.group(0))  # the
print(result.start())  # 10
print(result.end())  # 13
