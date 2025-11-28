# File, Process, and Service Handling in PowerShell

## 1. File Handling

### List Files & Directories
```
Get-ChildItem
Get-ChildItem -Recurse
Get-ChildItem C:\Logs
```

### Create Files & Folders
```
New-Item -ItemType File -Path C:\temp\test.txt
New-Item -ItemType Directory -Path C:\temp\newfolder
```

### Read File
```
Get-Content C:\temp\test.txt
```

### Write & Append
```
Set-Content C:\temp\test.txt "Hello World"
Add-Content C:\temp\test.txt "Another line"
```

### Copy / Move / Delete
```
Copy-Item C:\temp\a.txt C:\backup\
Move-Item C:\temp\a.txt C:\temp\new.txt
Remove-Item C:\temp\old.txt
```

### Search Text
```
Select-String -Path C:\logs\*.log -Pattern "Error"
```

---

## 2. Process Handling

### List Processes
```
Get-Process
Get-Process chrome
```

### Start/Stop Processes
```
Start-Process notepad
Stop-Process -Name notepad
Stop-Process -Id 1234
```

### Process Details
```
(Get-Process chrome).CPU
(Get-Process chrome).Id
(Get-Process chrome).StartTime
```

---

## 3. Service Handling

### List Services
```
Get-Service
```

### Running/Stopped
```
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-Service | Where-Object {$_.Status -eq "Stopped"}
```

### Start/Stop/Restart
```
Start-Service spooler
Stop-Service spooler
Restart-Service spooler
```

### Check Status
```
(Get-Service spooler).Status
```

### Startup Type
```
Set-Service -Name spooler -StartupType Automatic
Set-Service -Name spooler -StartupType Manual
Set-Service -Name spooler -StartupType Disabled
```

---

## 4. Combined Examples

### Log heavy processes
```
Get-Process |
Where-Object {$_.CPU -gt 300} |
Out-File C:\logs\heavy_processes.txt
```

### Auto-start service if stopped
```
$svc = Get-Service -Name spooler
if ($svc.Status -ne "Running") {
    Start-Service spooler
    Write-Output "Spooler service started"
}
```

### Backup old files
```
Get-ChildItem C:\logs -File |
Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-15)} |
Copy-Item -Destination C:\backup\
```
