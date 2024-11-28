import socket                                      # network communication ke kam aati h 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # socket library me socket function jodne ka kam kaerta h 
ip_adress= "192.168.159.29"                          # ip adress
port_number=2326                                   # port_number kuch bhi dal sakte h 
total_address=(ip_adress,port_number)
s.bind(total_address)                              # aapne adress ko bind (jodne ka )karne ka kam akarta h
while True:
    message=s.recvfrom(100)                        # recvform = limit hoti h receive karne ki 
    print(message)
    data=message[0]                                # first indexing hoti h 
    data="\n"                                      #  new line ke liya 
    print(data.encode("ascii"))

    

