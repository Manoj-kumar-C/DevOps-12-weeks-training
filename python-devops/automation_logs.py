import os, time

def clean_logs(log_dir, days=7):
    cutoff = time.time() - (days * 86400)
    for file in os.listdir(log_dir):
        p = os.path.join(log_dir, file)
        if os.path.isfile(p) and os.path.getmtime(p) < cutoff:
            os.remove(p)
