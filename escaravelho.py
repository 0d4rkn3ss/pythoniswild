import platform
import os
import sys

def get_processor():
    proc = platform.processor()
    if not proc:
        # Try to get from /proc/cpuinfo (Linux)
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":", 1)[1].strip()
        except Exception:
            return "Unknown"
    return proc

print("System Information Dump")
print("-" * 30)
print(f"OS: {platform.system()} {platform.release()}")
print(f"Platform: {platform.platform()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {get_processor()}")
print(f"Python Version: {platform.python_version()}")
print(f"User: {os.getlogin()}")
print(f"Current Directory: {os.getcwd()}")
print(f"Executable: {sys.executable}")
print("valente bosta do corcundo do caralho do escaravelho. não me fales mais nisso. já estou farto de ouvir falar do escaravelho. não me fales mais nisso. já estou farto de ouvir falar do escaravelho. não me fales mais nisso. já estou farto de ouvir falar do escaravelho.")
print("-" * 30)