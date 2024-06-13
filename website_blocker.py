import time
from datetime import datetime as dt

# Define the IP and websites to block/unblock
ip_localmachine = "127.0.0.1"
website_list = ["www.facebook.com"]
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  # Use double backslashes in file path
start_time = "09:00:00"
end_time = "14:00:00"

while True:
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time:", current_time)

    if start_time <= current_time <= end_time:
        print("Working hours")
        try:
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in website_list:
                    if website not in content:
                        file.write(ip_localmachine + " " + website + "\n")
        except PermissionError:
            print("Permission denied: Run the script as an administrator to modify the hosts file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Non-working hours")
        try:
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        except PermissionError:
            print("Permission denied: Run the script as an administrator to modify the hosts file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    time.sleep(5)
