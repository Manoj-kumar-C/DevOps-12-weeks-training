# Storing Output of a Command into a Variable or File in Bash

## ⭐ 1. Storing Output into a Variable

### ✔ Using \$(command) — Recommended
```bash
today=$(date)
echo "$today"
```

### ✔ Using backticks (old style)
```bash
files=`ls`
```

---

## ⭐ 2. Storing Output into a File

### ✔ Overwrite file
```bash
date > output.txt
```

### ✔ Append to file
```bash
date >> output.txt
```

### ✔ Using tee (show + save)
```bash
ls -l | tee list.txt
ls -l | tee -a list.txt   # append
```

---

## ⭐ 3. Store Output to BOTH Variable and File

```bash
output=$(ls | tee list.txt)
```

---

## ⭐ 4. Useful Examples

### Count files
```bash
count=$(ls | wc -l)
```

### Disk usage
```bash
disk_usage=$(df -h /)
```

### Save system info
```bash
uname -a > system_info.txt
```

### Append logs
```bash
echo "Backup run at $(date)" >> backup.log
```

---

## ⭐ Summary Table

| Task | Syntax |
|------|--------|
| Variable store | `var=$(command)` |
| Overwrite file | `command > file.txt` |
| Append file | `command >> file.txt` |
| Output + save | `command | tee file.txt` |
| Append with tee | `command | tee -a file.txt` |
