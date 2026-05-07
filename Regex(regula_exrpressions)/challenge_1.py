'''
Challenge 1: The "Identity" Scraper (The Junior Level)
You are cleaning up a user database. Some people entered their usernames and IDs in a weird format. You need to extract just the ID numbers.'''
import re
data="User: s_jobs (ID: 1955), User: woz_01 (ID: 1950), User: tim_apple (ID: 1960)"
pattern=r"\(ID: (\d+)\)"
print(re.findall(pattern=pattern,string=data))

