# Disney Characters
# 1st result's creation
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

# 2nd result's creation

disney_users_B = {}

for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

# 3rd result's creation

disney_users_C = {}

for user in sorted(users):
    disney_users_C[user] = users.index(user)
print(disney_users_C)

# 1st result's creation with names contains "i"
disney_users_D = {}

for user in users:
    if 'i' in user:
        disney_users_D[user] = users.index(user)
print(disney_users_D)

# 1st result's creation with names start by "m" or "p"

disney_users_E = {}

for user in users:
    if user.startswith(('m', 'p')):
        disney_users_E[user] = users.index(user)
print(disney_users_E)