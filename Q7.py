import re

email = "kaushalendra.singh@gmail.com"
pat = "\w+@(\w+).com"
ans = re.findall(pat,email)
print(ans)