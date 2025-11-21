# Most Commonly Used Linux Commands

## 🧭 Basic Navigation
- `pwd` – Show current directory  
- `ls` – List files and folders  
- `ls -l` – Long listing  
- `ls -a` – Show hidden files  
- `cd <path>` – Change directory  
- `cd ..` – Go up one directory  
- `cd ~` – Go to home directory  

---

## 📁 File & Directory Operations
- `touch file.txt` – Create empty file  
- `mkdir folder` – Create directory  
- `mkdir -p a/b/c` – Create nested directories  
- `cp file1 file2` – Copy file  
- `cp -r dir1 dir2` – Copy directory  
- `mv a b` – Move/rename  
- `rm file` – Remove file  
- `rm -r folder` – Remove folder  
- `rm -rf folder` – Force delete (dangerous)  

---

## 📄 View File Content
- `cat file` – Print whole file  
- `tac file` – Reverse cat  
- `less file` – View file page-by-page  
- `head file` – First 10 lines  
- `tail file` – Last 10 lines  
- `tail -f file` – Real-time log monitoring  

---

## 🔍 Search
- `grep "text" file` – Search inside file  
- `grep -i "text" file` – Case-insensitive search  
- `grep -r "text" dir/` – Recursive search  
- `find /path -name "*.log"` – Find files by name  

---

## 🖥️ System Info
- `uname -a` – OS & kernel info  
- `hostname` – Show hostname  
- `uptime` – System running time  
- `df -h` – Disk usage  
- `du -sh folder` – Folder size  
- `free -h` – RAM usage  
- `top` – Real-time processes  
- `htop` – Better process view (if installed)  
- `ps aux` – List running processes  

---

## 🌐 Network Commands
- `ifconfig` or `ip a` – Show IP address  
- `ping google.com` – Test connectivity  
- `curl URL` – Fetch URL  
- `wget URL` – Download file  
- `netstat -tulpn` – Ports & services  
- `ss -tulpn` – Modern netstat alternative  
- `ssh user@host` – Remote login  

---

## 🔐 Permissions
- `chmod 755 file` – Change permissions  
- `chown user:group file` – Change owner  
- `sudo <command>` – Run as root  

---

## 📦 Package Management

### Ubuntu/Debian
- `apt update` – Refresh package list  
- `apt upgrade` – Upgrade packages  
- `apt install package` – Install  
- `apt remove package` – Remove  

### RedHat/CentOS
- `yum install package` – Install  
- `dnf install package` – Modern installer  

---

## 📦 Archive / Compression
- `tar -cvf file.tar folder/` – Create tar file  
- `tar -xvf file.tar` – Extract tar  
- `tar -czvf file.tar.gz folder/` – Compress  
- `tar -xzvf file.tar.gz` – Extract gzip  

---

## 🧰 Git (Common in DevOps/Linux)
- `git clone repo` – Clone repo  
- `git status` – Check changes  
- `git add .` – Stage changes  
- `git commit -m "msg"` – Commit  
- `git push` – Push changes  

---

## ⚙️ Process Management
- `kill <pid>` – Kill process  
- `kill -9 <pid>` – Force kill  
- `systemctl start service` – Start service  
- `systemctl status service` – Check service  
- `systemctl restart service` –
