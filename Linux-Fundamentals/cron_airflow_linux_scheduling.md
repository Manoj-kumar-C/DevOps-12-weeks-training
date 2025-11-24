
# Cron, Airflow, and Linux Scheduling – Complete Notes

## 1. Cron (Linux Scheduler)

Cron is a built-in Linux scheduler used for automating recurring tasks.

### Common Cron Commands
```
crontab -l      # List cron jobs
crontab -e      # Edit cron jobs
crontab -r      # Remove all cron jobs
```

### Cron Syntax
```
* * * * * command
| | | | |
| | | | └── Day of week (0–6)
| | | └──── Month (1–12)
| | └────── Day of month (1–31)
| └──────── Hour (0–23)
└────────── Minute (0–59)
```

### Examples
```
0 5 * * * /home/user/backup.sh     # Run daily at 5 AM
* * * * * command                  # Every minute
*/10 * * * * command               # Every 10 minutes
0 0 * * 0 command                  # Every Sunday
```

---

## 2. Airflow (Workflow Orchestrator)

Apache Airflow is a workflow automation tool for complex pipelines.

### Features
- DAG-based workflows
- Task dependencies
- Retries & backfilling
- Web UI for monitoring
- Works with Python
- Ideal for ETL, ML pipelines, data engineering

### Airflow vs Cron

| Feature | Cron | Airflow |
|--------|------|---------|
| Complexity | Simple | Complex |
| Dependencies | No | Yes |
| Monitoring | No | Yes |
| Logging | Basic | Detailed |
| Distributed | No | Yes |
| Language | Shell | Python |

---

## 3. Linux Scheduling Commands

### at – One-time Scheduling
```
echo "backup.sh" | at 5pm
atq           # Show jobs
atrm <id>     # Remove
```

### sleep – Delay a Command
```
sleep 10      # Wait 10 seconds
sleep 5m && script.sh
```

### systemd timers – Modern Cron Alternative
Better monitoring, logs, dependencies.

Example files:
```
/etc/systemd/system/cleanup.timer
/etc/systemd/system/cleanup.service
```

---

## Summary

- **Cron** → Simple recurring tasks  
- **Airflow** → Complex, multi-step workflows  
- **at / sleep** → One-time or delayed execution  
- **systemd timers** → Advanced scheduling alternative  

