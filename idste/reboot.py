import http.client, urllib.request, urllib.parse, urllib.error
import socket, os

socket.setdefaulttimeout(10)


def main():
    path = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(path)
    fp = open("ip.txt", 'r')
    data = []
    for line in fp:
        if line not in data:
            data.append(line.strip('\n'))
    fp.close()

    for line in data:
        reboot(line)


def reboot(ip):
    try:
        headers = {'Authorization': 'Basic YWRtaW46YWRtaW4='}
        conn = http.client.HTTPConnection(ip)
        conn.request("POST", "/cgi-bin/reboot.cgi", None, headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        print(data + "\n")
        conn.close()
    except:
        print("failed to reboot " + ip)
        return


if __name__ == '__main__':
    main()
