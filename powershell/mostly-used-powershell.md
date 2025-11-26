# ⭐ Most Commonly Used PowerShell Commands (Beginner → Advanced)

---

## 📌 1. Basic Commands

| Command | Description |
|--------|-------------|
| `Get-Help` | Shows help for any command. |
| `Get-Command` | Lists all available PowerShell commands. |
| `Get-Service` | Lists Windows services. |
| `Get-Process` | Displays running processes. |
| `Stop-Process -Name chrome` | Kills a process. |
| `Start-Service <name>` | Starts a service. |
| `Stop-Service <name>` | Stops a service. |

---

## 📁 2. File & Directory Commands

| Command | Description |
|--------|-------------|
| `Get-ChildItem` or `ls` | List files & folders. |
| `Set-Location` or `cd` | Change directory. |
| `Copy-Item` | Copy files/folders. |
| `Move-Item` | Move files/folders. |
| `Remove-Item` or `rm` | Delete files/folders. |
| `New-Item` | Create file/folder. |
| `Get-Content` or `cat` | Read file content. |
| `Set-Content` | Overwrite a file. |
| `Add-Content` | Append to a file. |

---

## 🔍 3. System Information Commands

| Command | Description |
|--------|-------------|
| `Get-ComputerInfo` | Detailed system information. |
| `Get-HotFix` | Show installed Windows updates. |
| `Get-WmiObject Win32_OperatingSystem` | OS details. |
| `Get-WmiObject Win32_Processor` | CPU info. |
| `Get-WmiObject Win32_LogicalDisk` | Disk info. |

---

## 🌐 4. Network Commands

| Command | Description |
|--------|-------------|
| `Test-Connection google.com` | Ping alternative. |
| `Get-NetIPAddress` | Shows IP configuration. |
| `Get-NetIPConfiguration` | IP, DNS, Gateway info. |
| `nslookup` | DNS lookup. |
| `Resolve-DnsName` | DNS resolver. |
| `Get-NetAdapter` | Network adapter info. |

---

## 🔒 5. User, Account & Security Commands

| Command | Description |
|--------|-------------|
| `Get-LocalUser` | Show local users. |
| `New-LocalUser` | Create user. |
| `Set-LocalUser` | Modify user. |
| `Remove-LocalUser` | Delete user. |
| `Get-LocalGroup` | Show groups. |
| `Add-LocalGroupMember` | Add user to a group. |
| `Get-ExecutionPolicy` | Shows script execution policy. |
| `Set-ExecutionPolicy RemoteSigned` | Enable script execution. |

---

## ⚙️ 6. Package Management (PowerShell + Winget)

| Command | Description |
|--------|-------------|
| `Get-Package` | Lists installed packages. |
| `Install-Package -Name xyz` | Installs package. |
| `winget search chrome` | Search app. |
| `winget install vscode` | Install app. |
| `winget upgrade` | Check available updates. |

---

## 💻 7. PowerShell Scripting Essentials

| Command | Description |
|--------|-------------|
| `Get-Variable` | Shows variables. |
| `$name = "Manoj"` | Create variable. |
| `if (...) {}` | Condition. |
| `foreach (...) {}` | Loop. |
| `function Test-Me {}` | Function creation. |
| `.\script.ps1` | Run script. |

---

## 🧰 8. Process & Task Management

| Command | Description |
|--------|-------------|
| `Get-Process` | List processes. |
| `Stop-Process -Id 1234` | Kill by process ID. |
| `Start-Process notepad.exe` | Opens an app. |
| `Get-ScheduledTask` | List scheduled tasks. |
| `Register-ScheduledTask` | Create task. |

---

## ☑️ 9. Useful Administrative Commands

| Command | Description |
|--------|-------------|
| `Get-EventLog -LogName Application` | Read event logs. |
| `Clear-EventLog -LogName System` | Clear event logs. |
| `Get-Service` | List all services. |
| `Restart-Service Spooler` | Restart print spooler. |
| `Restart-Computer` | Reboot. |
| `Stop-Computer` | Shutdown. |

---

## 🔎 10. Searching & Filtering

| Command | Description |
|--------|-------------|
| `Where-Object { $_.Name -like "*chrome*" }` | Filter results. |
| `Select-Object Name, Status` | Select specific properties. |
| `Sort-Object` | Sort output. |

### Example (Filtering services)
```powershell
Get-Service | Where-Object {$_.Status -eq "Stopped"}
