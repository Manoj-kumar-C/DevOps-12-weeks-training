# Commonly Used `systemctl` Commands in Linux

## 1. Service Management

### Start a service
```bash
sudo systemctl start service_name
```

### Stop a service
```bash
sudo systemctl stop service_name
```

### Restart a service
```bash
sudo systemctl restart service_name
```

### Reload a service (without stopping)
```bash
sudo systemctl reload service_name
```

### Check service status
```bash
systemctl status service_name
```

---

## 2. Enable/Disable Services (Startup Control)

### Enable at boot
```bash
sudo systemctl enable service_name
```

### Disable at boot
```bash
sudo systemctl disable service_name
```

### Enable & start
```bash
sudo systemctl enable --now service_name
```

### Disable & stop
```bash
sudo systemctl disable --now service_name
```

### Check if enabled
```bash
systemctl is-enabled service_name
```

---

## 3. Logs (journalctl)

### View service logs
```bash
journalctl -u service_name
```

### Real-time logs
```bash
journalctl -u service_name -f
```

---

## 4. System Control Commands

### Reboot
```bash
sudo systemctl reboot
```

### Shutdown
```bash
sudo systemctl poweroff
```

### Suspend
```bash
sudo systemctl suspend
```

### Hibernate
```bash
sudo systemctl hibernate
```

---

## 5. Unit & Daemon Management

### List services
```bash
systemctl list-units --type=service
```

### List failed services
```bash
systemctl --failed
```

### Show service info
```bash
systemctl show service_name
```

### Reload systemd manager
```bash
sudo systemctl daemon-reload
```

---

## 6. Mask/Unmask Services

### Mask (block usage)
```bash
sudo systemctl mask service_name
```

### Unmask
```bash
sudo systemctl unmask service_name
```

---

## 7. Dependencies

### View service dependencies
```bash
systemctl list-dependencies service_name
```

---

## Summary Table

| Action | Command |
|--------|----------|
| Start | `systemctl start` |
| Stop | `systemctl stop` |
| Restart | `systemctl restart` |
| Status | `systemctl status` |
| Enable | `systemctl enable` |
| Disable | `systemctl disable` |
| Logs | `journalctl -u <service>` |
| Reload daemon | `systemctl daemon-reload` |

