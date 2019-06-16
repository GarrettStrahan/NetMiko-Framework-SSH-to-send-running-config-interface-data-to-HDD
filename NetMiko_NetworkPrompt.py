#Configured with Windows10, modify if your Linux
#My first attempt to learn python and netmiko

from netmiko import Netmiko


ipaddr = input("What is the IP-Address?")
username = input("What is the username?")
password = input("What is the password?")
secret = input("What is the enable password? if none state none")
networknodetype = input("Are you using an ASA? yes/no")

if networknodetype == "yes" or "y":
     networknodetype = "cisco_asa"
else:
     networknodetype = "ciso_ios"

if secret == "none":
     cisconoenable = {
          "host": ipaddr,
          "username": username,
          "password": password,
          "device_type": "networknodetype"}
     net_connect = Netmiko(**cisconoenable) #This is where it connect with SSH for no enable/secret


else:
     ciscoioswithenable = {
          "host": ipaddr,
          "username": username,
          "password": password,
          "device_type": networknodetype,
          "secret": secret}
     net_connect = Netmiko(**ciscoioswithenable) #This is where it connect with SSH for an enable password

print()
print(net_connect.find_prompt())
print(net_connect.enable())
print(net_connect.send_command("sh clock"))
clock =  net_connect.send_command("sh clock")
print(net_connect.send_command("sh int ip brief"))
interfaces = net_connect.send_command("sh int ip brief")
shrun = net_connect.send_command("sh run")
print(net_connect.send_command("sh run"))

net_connect.disconnect()

print("WE HAVE DISCONNECTED")
print(clock)
print(interfaces)
print(type(interfaces))


File_object = open("Interfaces.txt","w")
File_object.write(interfaces)
print("The interfaces has been been written to Interfaces.txt")

File_object2 = open("Running-Config.txt","w")
File_object2.write(shrun)
print("The Running-configuration has been been written to Running-Config.txt")