groups = ["Group 1"]

group1 = {
  "users": ["John", "Jane", "Jack"],
  "perms": ["read", "write", "delete"],
  "date": "2023-01-01"
}

def get_users():
  for x in group1["users"]:
    print(f"User: {x}")
