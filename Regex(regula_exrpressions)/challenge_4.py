import re

# This pattern says: 
# 1. Start at the beginning (^)
# 2. Look ahead for a digit (?=.*\d)
# 3. Look ahead for an uppercase letter (?=.*[A-Z])
# 4. If those are true, match any character 8 or more times .{8,}
# 5. End of string ($)

pattern = r"^(?=.*\d)(?=.*[A-Z]).{8,}$"

test_passwords = ["apple123", "Apple", "Nepal@2026"]

for p in test_passwords:
    if re.match(pattern, p):
        print(f"'{p}' is STRONG")
    else:
        print(f"'{p}' is WEAK")