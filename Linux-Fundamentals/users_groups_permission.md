# Linux Users, Groups & Permissions Cheat Sheet

## ✅ User Management Commands
| Task                     | Command Example                          |
|-------------------------|-----------------------------------------|
| List all users          | `cat /etc/passwd`                      |
| Add a user             | `sudo adduser username`                |
| Delete a user          | `sudo userdel username`                |
| Delete user + home dir | `sudo userdel -r username`             |
| Modify user            | `sudo usermod options username`        |
| Show current user      | `whoami`                               |
| Show logged-in users   | `who` / `w`                            |

## ✅ Group Management Commands
| Task                     | Command Example                          |
|-------------------------|-----------------------------------------|
| List all groups         | `cat /etc/group`                       |
| Add a group            | `sudo groupadd groupname`              |
| Delete a group         | `sudo groupdel groupname`              |
| Add user to group      | `sudo usermod -aG groupname username`  |
| Show user’s groups     | `groups username`                      |

## ✅ Permissions & Ownership
| Task                     | Command Example                          |
|-------------------------|-----------------------------------------|
| View permissions        | `ls -l`                                |
| Change permissions      | `chmod 755 filename`                   |
| Change owner            | `sudo chown user:group filename`       |
| Detailed file info      | `stat filename`                        |

## ✅ Permission Basics
| Symbolic | Numeric | Meaning                |
|----------|---------|------------------------|
| `r`      | 4       | Read                  |
| `w`      | 2       | Write                 |
| `x`      | 1       | Execute               |
| Example  | 755     | Owner: rwx, Group: r-x, Others: r-x |
