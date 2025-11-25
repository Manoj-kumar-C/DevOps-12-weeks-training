# Process Management Commands in Linux

## 1. View Running Processes

### `ps` — Process Status
```bash
ps
ps aux
ps aux | grep nginx
ps axjf
```

## 2. Real-Time Process Monitoring

### `top` — Live Process Viewer
Useful shortcuts:
- `P` – Sort by CPU  
- `M` – Sort by Memory  
- `k` – Kill  
- `q` – Quit  
- `r` – Renice  

### `htop` — Advanced Viewer
Install:
```bash
sudo apt install htop
```

## 3. Kill or Terminate Processes

### `kill`
```bash
kill <pid>
kill -9 <pid>
```

### `killall`
```bash
killall apache2
```

## 4. Process Priority & Scheduling

### `nice`
```bash
nice -n 10 python3 script.py
```

### `renice`
```bash
renice -n 5 -p <pid>
```

## 5. Background & Foreground Job Control
```bash
command &
jobs
fg %1
bg %1
```

## 6. Process Information
```bash
pidof nginx
pgrep ssh
pgrep -l ssh
```

## 7. System Resource Monitoring
```bash
vmstat
iostat
free -h
```

## Summary Table
| Purpose | Command |
|--------|---------|
| List processes | `ps`, `ps aux` |
| Live monitoring | `top`, `htop` |
| Kill process | `kill`, `killall` |
| Job control | `jobs`, `fg`, `bg` |
| Priority control | `nice`, `renice` |
| Search processes | `pgrep`, `pidof` |
| System resource info | `free`, `vmstat`, `iostat` |
