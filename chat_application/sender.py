import socket     # network communication ke kam aati h 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # socket library me socket function jodne ka kam kaerta h 
ip_adress= "192.168.1.92"                          # ip adress
port_number=8888                              # port_number kuch bhi dal sakte h 
total_address=(ip_adress,port_number)              
message=input("Enter your message")
encript_message=message.encode("ascii")                    #  encode= binary me convert karne ke liya 
s.sendto(encript_message,total_address)             # sendto =message bhaj ne ka kam aata h 

