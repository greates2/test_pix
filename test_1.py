import os

port = 80

check_nginx_status = 'sudo netstat -ntulp | grep {} | grep nginx'.format(port)
nginx_status = os.system(check_nginx_status)

# print(nginx_status)

if nginx_status == 0:
    print('OK - nginx server is working')
elif nginx_status == 256:
    print('ERROR - nginx server is stopped')
else:
    print('WARNING - неизвестный код ошибки')
