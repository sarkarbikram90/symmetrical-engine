

def auto_heal(metrics):
    actions = []

    if metrics["disk_usage"] > 85:
        actions.append("Disk cleanup executed")

    if metrics["memory_usage"] > 85:
        actions.append("Memory cleanup executed")

    if metrics["cpu_usage"] > 90:
        actions.append("Restarted high CPU service")

    return actions