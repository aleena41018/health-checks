import shutil
import sys
import os 

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_root_full():
    return check_disk_usage("/", 2, 10)

def check_disk_usage(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True

def main():
    checks = [ (check_reboot, "Pending reboot!!"), (check_disk_usage, "Root partition Full!!"), ]
    everything_ok=True
    if check, msg in checks:
        if check():
            print(msg)
            everything_ok=False
    if not everything_ok:
        sys.exit(0)
    print("Everything OK!")
    sys.exit(0)