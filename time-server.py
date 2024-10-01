from socket import AF_INET, SOCK_DGRAM
import socket
import struct, time

def getTime(host = 'pool.ntp.org'):
    port = 123
    buf = 2048
    address = (host,port)
    msg = '\x1b' + 47 * '\0'
    TIME1970 = 2208988800
    # connect to server
    client = socket.socket( AF_INET, SOCK_DGRAM)
    client.sendto(msg.encode('utf-8'), address)
    msg, address = client.recvfrom( buf )
    t = struct.unpack( '!12I', msg )[10]
    t -= TIME1970
    return time.ctime(t).replace("  ", " ")

if __name__ == "__main__":
    print(getTime())
