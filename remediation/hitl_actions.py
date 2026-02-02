


def risky_actions(metrics):
    actions = []

    if metrics["dns_latency"] > 250:
        actions.append("DNS configuration change")

    if metrics["firewall_change"] == 1:
        actions.append("Firewall port modification")

    return actions