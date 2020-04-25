import socket


# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.baidu.com', 80))

# 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn/\r\nConnection: close\r\n\r\n')
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')


# 接收数据:
buffer = []
while True:  # 循环接受所有字节
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)  # append函数把字节接到原序列后面
    else:
        break
data = b''.join(buffer)  # 空字节用join连接

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)  # 1是分割次数，默认是无数次
print(header.decode('utf-8'))  # decode解码为utf-8

# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

