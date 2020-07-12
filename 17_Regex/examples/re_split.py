import re

result = re.split(r'\W+', 'Python is the best. Moreover, re is the best')
print(result)  # ['Python', 'is', 'the', 'best', 'Moreover', 're', 'is', 'the', 'best']
