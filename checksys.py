import platform
import os

def get_os_info():
    os_name = platform.system()
    os_version = platform.version()
    
    if os_name == "Linux":
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME"):
                        os_version = line.split("=")[1].strip().strip('"')
                        break
        except FileNotFoundError:
            pass
    elif os_name == "Windows":
        os_version = platform.release()
        if os_version == "10":
            try:
                if int(platform.version().split('.')[2]) >= 22000:
                    os_version = "11"
            except (IndexError, ValueError):
                pass
    
    return os_name, os_version

os_name, os_version = get_os_info()
print(f"Sistema Operativo: {os_name}")
print(f"Versão de SO: {os_version}")