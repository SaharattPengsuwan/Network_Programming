import paramiko

hostname = "192.168.1.124"
username = "saharatt"
passwd = 'password'
port = 22

try:
    p = paramiko.Transport((hostname,port))
    p.connect(username=username,password=passwd)
    print("[*] Connected to "+ hostname + " wia SSH")
    sftp = paramiko.SFTPClient.from_transport(p)
    print("[*] Starting file download")
    sftp.get("/home/saharatt/test.txt","/Users/saharatt/Download/d.txt")
    print("[*] file dowlad complete")
    print("[*] Starting file upload")
    sftp.get("/Users/saharatt/Download/d.txt","/Home/saharatt/Download/u.txt")
    print("[*] file upload complete")
    p.close()
    print("[*] Disconnected from server")

except Exception as err:
    print("[!] "+str(err))