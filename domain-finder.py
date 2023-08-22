import socket
import sys

txtfile = input("Enter txt file path : ")
while len(txtfile) == 0 :
    print("Enter txt file path (e.g C:/demo.txt or demo.txt)")
    txtfile = input("Enter txt file path : ")

target_ip = input("Enter your target ip : ")
while len(target_ip) == 0 :
    print("Enter your target ip (e.g 127.0.0.1 or google.com)")
    target_ip = input("Enter your target ip : ")

urls = open(txtfile, "r")

output_file = open("out.txt","w")

for lines in urls :

    results = lines.strip()

    try:
        ips_list = socket.gethostbyname(results)
        if ips_list == target_ip :
            output_file.write(results + "\n")
            print(results)

    except:
        continue

