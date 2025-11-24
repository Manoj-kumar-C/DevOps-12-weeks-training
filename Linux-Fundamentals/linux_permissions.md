# Linux File Permissions (rwx) and chmod

## 1. What are Linux File Permissions?
Every file and directory in Linux has three types of permissions for three categories of users.

### Permission Types
| Symbol | Meaning | File Action | Directory Action |
|--------|---------|-------------|------------------|
| r | Read | View file contents | List directory contents |
| w | Write | Modify the file | Create/delete files inside it |
| x | Execute | Run the file as a program | Enter (cd) into the directory |

### Permission Groups
- **Owner (u)**
- **Group (g)**
- **Others (o)**

Example:
```
-rwxr-x---
```

## 2. Viewing Permissions
```
ls -l
```

## 3. chmod — Change Permissions

### A) Symbolic Method
```
chmod u+x file.sh
chmod o-w file.txt
chmod g+rw notes.txt
chmod a=r file.txt
```

### B) Numeric Method
| Permission | Value |
|-----------|--------|
| r | 4 |
| w | 2 |
| x | 1 |

Example:
```
chmod 755 script.sh
```

## Common Numeric Permissions
| Code | Meaning |
|-------|-------------|
| 777 | Everyone full access |
| 755 | Owner rwx; others r-x |
| 700 | Only owner full access |
| 644 | Owner rw; others r |
| 600 | Owner rw only |
