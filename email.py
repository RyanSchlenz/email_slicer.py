# Email slicer project


# Get user for email address
email = input("What is your email address?: ").strip() # use strip to take out extra spaces if user adds them

# Slice out username
#everything until the @ sign
user = email[:email.index("@")].strip()

# Slice domain name
# everything after the @ symbol
domain = email[email.index("@")+ 1 :]

# Format message
output = "Your username is {} and your domain name is {}".format(user, domain)

# Display output message
print(output)
