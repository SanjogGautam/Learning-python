import pandas as pd

# 1. Create a dataset to practice on
data = {
    "Name": ["Sanjog", "Sarin", "Swagat", "Susan", "Bibek", "Kushal"],
    "Age": [20, 21, 21, 22, 22, 21],
    "Address": ["Parbat", "Kirtipur", "Nuwakot", "Dang", "Bajang", "Dhading"]
}
df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4", "S5", "S6"])

print("--- Original DataFrame ---")
print(df)

# --- A. DELETING COLUMNS ---

# 1. Using del (Permanent and Immediate)
del df["Address"] 

# 2. Using .drop() (Safe - requires re-assignment)
df = df.drop(columns=["Age"]) 

# --- B. DELETING ROWS ---

# 1. Removing by Index Label
df = df.drop("S1") 

# 2. Removing Multiple Rows by Labels
df = df.drop(["S2", "S3"]) 

# 3. Removing by Numerical Position (e.g., removing the first row of what's left)
df = df.drop(df.index[0]) 

# --- C. DELETING BASED ON CONDITIONS (Filtering) ---
# Technically, we "keep" what we want, which effectively deletes the rest
# Let's recreate a row to show this
new_row = pd.DataFrame({"Name": ["Temporary"]}, index=["S7"])
df = pd.concat([df, new_row])

# Delete rows where Name is "Temporary"
df = df[df["Name"] != "Temporary"]

# --- D. RESETTING THE INDEX ---
# This "deletes" my custom S1, S2 labels and replaces them with 0, 1, 2...
df = df.reset_index(drop=True)

print("\n--- Final DataFrame After All Deletions ---")
print(df)