import instaloader
import getpass

# Create an instance of instaloader
L = instaloader.Instaloader()

# Prompt for login to instagram
USERNAME = input("Enter your Instagram Username: ")
PASSWORD = getpass.getpass("Enter your Instagram Password: ")
L.login(USERNAME, PASSWORD)

# Attempt to log in to instagram
try:
    L.login(USERNAME, PASSWORD)
except instaloader.exceptions.BadCredentialsException:
    print("Incorrect username or password.")
    exit(1)
except instaloader.exceptions.ConnectionException:
    print("Network problem. Please check your internet connection.")
    exit(1)
# Load profile
try:
    profile = instaloader.Profile.from_username(L.context, USERNAME)
    print("Loading...")
except instaloader.exceptions.ProfileNotExistsException:
    print("The profile does not exist")
    exit(1)

# Get Followers
followers = set(profile.get_followers())

# Get Following
followees = set(profile.get_followees())

# Find users not following back
not_following_back = followees - followers

# Print the usernames
print("Users not following back:")
for user in not_following_back:
    print(user.username)