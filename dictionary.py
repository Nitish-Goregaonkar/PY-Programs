instagram_profile = {
    "name": "Nitish Goregaonkar",
    "bio": " I am a softwar developer",
    "followers": "12000",
    "following": "2000",
    "posts": ["post1","post2"]
}

#print(instagram_profile["name"])
#print(instagram_profile["bio"])
#print(instagram_profile["posts"])

#print(type(instagram_profile))
#print(instagram_profile["followers"])
#print(instagram_profile["following"])

print(instagram_profile.keys())
for key in instagram_profile.keys():
    print(key)
print((instagram_profile. values()))