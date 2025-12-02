import paramiko

class SSHClient:
    def __init__(self, host, user, password=None, port=22):
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def run(self, cmd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, username=self.user, password=self.password, port=self.port)
        _, stdout, stderr = client.exec_command(cmd)
        out = stdout.read().decode()
        err = stderr.read().decode()
        client.close()
        if err:
            raise Exception(err)
        return out
