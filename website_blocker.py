import time

# Define the configuration
host_path = r"C:\Windows\System32\drivers\etc\hosts"
website_list=["instagram.com","spankbang.com"]
redirect = "127.0.0.1"

# Open the hosts file and read its contents
with open(host_path, "r+") as file:
    content = file.read()

    # Check and add the websites to the hosts file if they are not already blocked
    for website in web_sites_list:
        if website not in content:
            file.write(redirect + " " + website + "\n")

# Sleep for 10 seconds
time.sleep(10)
