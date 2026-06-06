name = "Bob"

print("======== or =======")
valid_user = None or "User"
print(f"Hello {valid_user}")

name = "Bob"
 
print("========= or =========")
valid_user = name or "User"
print(f"Hello {valid_user}")
 
print("========= and =========")
email = "bob@example.com"
 
valid_email = email and email != "" # email and True
print(f"Valid email: {valid_email}")
 
if valid_email:
    print(f"Hello {valid_user}, your email is {email}")
else:
    print(f"Hello {valid_user}, please enter your email.")