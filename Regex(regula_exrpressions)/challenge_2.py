'''Challenge 2: The "International" Scraper
Now, let's see if you can apply that same logic to the phone numbers. This one is trickier because you have to handle an optional prefix without letting Python "cut" the number into pieces.'''
import re
data2 = "Call +977-9841234567 or 9801112223. Ignore 123."
a=re.findall(pattern=r"(?:\+977-)?\d{10}",string=data2)
print(a)
