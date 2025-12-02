import paramiko

def upload(host, user, password, local, remote):
    t = paramiko.Transport((host, 22))
    t.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(local, remote)
    sftp.close()
    t.close()

def download(host, user, password, remote, local):
    t = paramiko.Transport((host, 22))
    t.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remote, local)
    sftp.close()
    t.close()
