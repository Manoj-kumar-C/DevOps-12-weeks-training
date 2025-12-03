# Cron Job Commands & Important Concepts

## 1. Crontab Commands
```
crontab -l        # list cron jobs
crontab -e        # edit cron jobs
crontab -r        # remove all cron jobs
crontab -u user -e  # edit cron for a user
crontab -u user -l  # list cron for a user
```

## 2. Cron Time Format
```
*  *  *  *  *  command
|  |  |  |  |
|  |  |  |  └── Day of week (0-6)
|  |  |  └──── Month (1-12)
|  |  └────── Day of month (1-31)
|  └──────── Hour (0-23)
└────────── Minute (0-59)
```

### Symbols
- `*` every
- `,` multiple values
- `-` range
- `/` step

## 3. Common Examples
```
* * * * * cmd          # every minute
*/5 * * * * cmd        # every 5 minutes
0 2 * * * cmd          # daily 2 AM
0 15 * * 1 cmd         # every Monday 3 PM
0 0 1 * * cmd          # 1st of month
```

## 4. Log Output
```
>> /var/log/job.log 2>&1
```

## 5. Cron Logs
```
grep CRON /var/log/syslog
journalctl -u cron.service
grep CRON /var/log/cron   # RHEL/CentOS
```

## 6. System-Wide Cron
```
/etc/crontab
/etc/cron.d/
/etc/cron.hourly/
etc/cron.daily/
etc/cron.weekly/
etc/cron.monthly/
```

## 7. Special Keywords
```
@reboot
@hourly
@daily
@weekly
@monthly
@yearly
```

## 8. Best Practices
- Use absolute paths
- Redirect logs
- Add PATH in crontab
```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin
```
