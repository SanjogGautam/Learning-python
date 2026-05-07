'''Challenge 3: The "Greedy" HTML Trap
You are trying to extract HTML tags from a string to see how a webpage is structured.'''
import re
data="<div>Python</div> <span>RegEx</span>"
pattern=r"<.*?>"
print(re.findall(pattern=pattern,string=data))