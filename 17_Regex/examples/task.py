"""
r'\w*'

re.match(r'[a-zA-Z]+')
"""

import re
word = '.... пример, строки'
pattern = re.compile(r'\w+')
pattern = re.compile(r'(\w{2})\w*\b')
#"(\w{2})\w*\b"
pattern.findall(word)[0]
#'пример'
















