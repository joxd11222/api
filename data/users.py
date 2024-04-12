import data.groups as groups

users = ["John", "Jane", "Jack"]

visits = {
  users[0]: 100,
  users[1]: 10843,
  users[2]: 10000000
}

date = {
  users[0]: "2023-01-01",
  users[1]: "2020-01-01",
  users[2]: "2009-01-01"
}

verification = {
  users[0]: "Not Verified",
  users[1]: "Verified",
  users[2]: "Verified Plus"
}

def get_visits(user):
  if user in visits:
    print(visits[user])
  else:
    print(f"Unknown user: {user}")

def get_date(user):
  if user in date:
    print(date[user])
  else:
    print(f"Unknown user: {user}")

def get_verification(user):
  if user in verification:
    print(verification[user])
  else:
    print(f"Unknown user: {user}")

def new_user(name):
  if name not in users:
    users.append(name)
    visits[name] = 0
    date[name] = "Unknown"
    verification[name] = "Unknown"
    print(f"New user added: {name}")
  else:
    print(f"User already exists: {name}")
