import subprocess
import json
from pathlib import Path

def generate_static_data():
    networks = []
    try:
        # Fetch wireless network names
        raw_profiles = subprocess.check_output(
            ["nmcli", "-t", "-f", "NAME,TYPE", "connection", "show"], 
            text=True
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
                        text=True
                    ).strip()
                    password = raw_pass if raw_pass else "Open Network / No Password"
                except Exception:
                    password = "Requires Root Access / Not Found"
                
                networks.append({"name": name, "password": password})
                
    except Exception as e:
        print(f"Error fetching network profiles: {e}")

    # Output to the static file consumed by the interface
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(networks, f, indent=4)
    print("Successfully generated data.json!")

if __name__ == "__main__":
    generate_static_data()
