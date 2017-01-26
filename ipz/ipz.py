import socket
import requests
import re
import platform
import subprocess as sub
ip_pattern=r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
api_1="http://ipinfo.io/ip"

def local_ip():
    '''
    return local ip of computer in windows by socket module and in unix with hostname command in shell
    :return: local ip as string
    '''
    try:
        ip=socket.gethostbyname(socket.gethostname())
        if ip!="127.0.0.1":
            return ip
        elif platform.system()!="Windows":
            command=sub.Popen(["hostname","-I"],stdout=sub.PIPE,stderr=sub.PIPE,stdin=sub.PIPE,shell=False)
            response=list(command.communicate())
            if len(response[0])>0:
                return str(response[0])[2:-4]
            else:
                return "Error"
        else:
            return "Error"

    except Exception as e:
        print(e)
        return "Error"

def global_ip():
    '''
    retur ip with by http://ipinfo.io/ip api
    :return: global ip as string
    '''
    try:
        new_session=requests.session()
        response=new_session.get(api_1)
        ip_list=re.findall(ip_pattern,response.text)
        new_session.close()
        return ip_list[0]
    except:
        return "Error"

