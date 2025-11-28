
# PowerShell for DevOps — Complete Deep Dive

## Contents
- API calls & JSON handling
- Remote execution
- Modules & Azure Az module
- Advanced DevOps patterns
- DSC (Desired State Configuration)
- Azure Automation
- Testing with Pester
- PowerShell in CI/CD pipelines
- Troubleshooting & Best Practices
- Appendix

---

## 1) API calls & JSON handling
### Key cmdlets
- `Invoke-RestMethod`
- `Invoke-WebRequest`
- `ConvertTo-Json`
- `ConvertFrom-Json`

### GET Example
```powershell
$uri = "https://api.github.com/repos/PowerShell/PowerShell"
$headers = @{ "User-Agent" = "DevOpsGuide" }
$data = Invoke-RestMethod -Uri $uri -Headers $headers
$data.full_name
```

### POST Example
```powershell
$body = @{ name="demo"; enabled=$true } | ConvertTo-Json
Invoke-RestMethod -Uri "https://example.com/api" -Method Post -Body $body -ContentType "application/json"
```

---

## 2) Remote execution
### WinRM Remoting
```powershell
Enable-PSRemoting -Force
Invoke-Command -ComputerName "server01" -ScriptBlock { hostname }
```

### SSH Remoting (PowerShell Core)
```powershell
Invoke-Command -HostName "linuxhost" -UserName "ubuntu" -ScriptBlock { uname -a }
```

### PSSessions
```powershell
$s = New-PSSession -ComputerName "server01"
Invoke-Command -Session $s -ScriptBlock { Get-Service }
Remove-PSSession $s
```

---

## 3) Modules & Azure Az module

### Install Module
```powershell
Install-Module -Name Az -Scope CurrentUser
```

### Connect to Azure
```powershell
Connect-AzAccount
New-AzResourceGroup -Name rg-demo -Location eastus
```

### Create a Simple Module
```
MyModule/
  MyModule.psm1
  MyModule.psd1
```

---

## 4) Advanced DevOps-specific patterns

### Idempotency
```powershell
if (-not (Test-Path "C:\App")) {
    New-Item -Path "C:\App" -ItemType Directory
}
```

### Secrets Handling (Example: Azure Key Vault)
```powershell
$secret = Get-AzKeyVaultSecret -VaultName "kv-demo" -Name "mysecret"
$secret.SecretValueText
```

---

## 5) PowerShell DSC

### Basic DSC Example
```powershell
Configuration WebConfig {
    Node "localhost" {
        WindowsFeature IIS {
            Ensure = "Present"
            Name   = "Web-Server"
        }
    }
}
WebConfig -OutputPath "C:\DSC"
Start-DscConfiguration -Path "C:\DSC" -Verbose -Wait -Force
```

---

## 6) Azure Automation

### Runbook Example
```powershell
Connect-AzAccount -Identity
Stop-AzVM -ResourceGroupName "rg" -Name "vm1" -Force
Start-AzVM -ResourceGroupName "rg" -Name "vm1"
```

---

## 7) Testing with Pester

### Simple Test
```powershell
Describe "Math Test" {
    It "Adds numbers" {
        (1 + 1) | Should -Be 2
    }
}
```

---

## 8) PowerShell in CI/CD pipelines

### GitHub Actions Example
```yaml
name: Pester-CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-powershell@v2
    - run: pwsh -Command "Invoke-Pester -Output Detailed"
```

---

## 9) Troubleshooting & Best Practices

### Common Issues
- WinRM failures → check firewall, listener, HTTPS binding.
- Module version conflicts → use dedicated virtual env or module path.

### Logging Best Practice
```powershell
Write-Output ( @{ time=(Get-Date); level="info"; msg="Deployment started" } | ConvertTo-Json )
```

---

## 10) Appendix
- Use `Get-Help` extensively
- Use `Invoke-ScriptAnalyzer` for static code analysis
- Use Pester for all modules and automation scripts

---
