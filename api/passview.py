import subprocess
import json

def onRequest(request, context):
    """
    Kusum PassView API Endpoint
    """
    networks = []
    
    try:
        # Fetch wireless network profiles using nmcli
        raw_profiles = subprocess.check_output(
            ["nmcli", "-t", "-f", "NAME,TYPE", "connection", "show"], 
            text=True,
            timeout=5
        )
        
        for line in raw_profiles.splitlines():
            if not line.strip():
                continue
            parts = line.split(":")
            if len(parts) >= 2 and "802-11-wireless" in parts[1]:
                name = parts[0]
                
                # Fetch corresponding password
                try:
                    raw_pass = subprocess.check_output(
                        ["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", name],
                        text=True,
                        timeout=3
                    ).strip()
                    password = raw_pass if raw_pass else "Open Network / No Password"
                except Exception:
                    password = "Requires Root Access / Not Found"
                
                networks.append({"name": name, "password": password})
                
    except Exception as e:
        # Return fallback empty state if nmcli fails in the execution runtime environment
        pass

    # Build Response payload object
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "X-Powered-By": "Kusum PassView API"
        },
        "body": json.dumps(networks)
    }
