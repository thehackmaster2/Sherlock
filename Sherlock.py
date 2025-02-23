import requests

# List of websites to check for the username
websites = [
    {"site": "Instagram", "url": "https://www.instagram.com/"},
    {"site": "Twitter", "url": "https://twitter.com/"},
    {"site": "Facebook", "url": "https://www.facebook.com/"},
    {"site": "GitHub", "url": "https://www.github.com/"},
    {"site": "YouTube", "url": "https://www.youtube.com/c/"},
    {"site": "TikTok", "url": "https://www.tiktok.com/@"},
    {"site": "Telegram", "url": "https://t.me/"},
    {"site": "Snapchat", "url": "https://www.snapchat.com/add/"},
    {"site": "Reddit", "url": "https://www.reddit.com/user/"},
    {"site": "Pinterest", "url": "https://www.pinterest.com/"},
    {"site": "LinkedIn", "url": "https://www.linkedin.com/in/"}
]

def check_username(username):
    for website in websites:
        url = website["url"] + username
        try:
            response = requests.get(url)
            if response.status_code == 404:
                print(f"[+] {username} is available on {website['site']}")
            else:
                print(f"[-] {username} is taken on {website['site']} : {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error visiting {website['site']}: {e}")

# Get username from the user
username_to_check = input("Enter the username you want to check: ")
check_username(username_to_check)