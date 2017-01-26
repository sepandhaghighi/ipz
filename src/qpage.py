import socket
import requests
import re
ip_pattern=r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
api_1="http://www.ip2location.com"

def local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Error"

def global_ip():
    try:
        new_session=requests.session()
        response=new_session.get(api_1)
        ip_list=re.findall(ip_pattern,response.text)
        new_session.close()
        return ip_list[0]
    except:
        return "Error"





if __name__=="__main__":
    print(global_ip())

