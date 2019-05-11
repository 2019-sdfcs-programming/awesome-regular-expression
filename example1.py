import re

compiled = re.compile(r'(\(쓰는코드\))\((안쓰)는코드\)')
a = compiled.search('(쓰는코드)(안쓰는코드)(쓰는코드)(쓰는코드)').group(2)
print(a)
