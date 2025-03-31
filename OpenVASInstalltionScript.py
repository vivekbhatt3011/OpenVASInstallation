import subprocess
import time

# Function to execute shell commands
def run_command(command, check=True):
    """
    Runs a shell command and returns the output.
    If the command fails, it prints an error message.
    """
    try:
        result = subprocess.run(command, shell=True, check=check, text=True, capture_output=True)
        print(f"[✔] {command} completed successfully")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[✖] Command failed: {command}\nError: {e.stderr}")
        return None

# Update and upgrade system packages
print("[+] Updating system and installing dependencies...")
run_command("sudo apt update && sudo apt upgrade -y")

# Install required dependencies
print("[+] Installing required dependencies...")
dependencies = " \\
    software-properties-common \\
    cmake pkg-config gcc-mingw-w64 \\
    libgnutls28-dev libglib2.0-dev \\
    libgpgme-dev libksba-dev \\
    libsqlite3-dev libpcap-dev \\
    libxml2-dev libssh-gcrypt-dev \\
    python3 python3-pip python3-venv \\
    python3-lxml python3-defusedxml \\
    python3-psutil python3-paramiko \\
    bison flex texlive-science \\
    texlive-fonts-recommended \\
    gnutls-bin nmap \\
    redis-server \\
    curl sudo"
run_command(f"sudo apt install -y {dependencies}")

# Add Greenbone's PPA repository
print("[+] Adding Greenbone PPA repository...")
run_command("sudo add-apt-repository -y ppa:mrazavi/gvm")
run_command("sudo apt update")

# Install OpenVAS (GVM)
print("[+] Installing Greenbone Vulnerability Management (GVM)...")
run_command("sudo apt install -y gvm")

# Enable and start required OpenVAS services
print("[+] Enabling and starting OpenVAS services...")
run_command("sudo systemctl enable --now ospd-openvas gvmd gsad")

# Check service status
print("[+] Checking service status...")
services = ["gvmd", "gsad", "ospd-openvas"]
for service in services:
    status = run_command(f"systemctl is-active --quiet {service}", check=False)
    if status == "active":
        print(f"[✔] {service} is running")
    else:
        print(f"[✖] {service} failed to start")

# Sync vulnerability feeds with retries
print("[+] Syncing vulnerability databases (this may take time)...")
for attempt in range(1, 6):
    if run_command("sudo -u _gvm greenbone-feed-sync", check=False):
        print("[✔] Feed sync successful")
        break
    print(f"[-] Feed sync failed, retrying ({attempt}/5)...")
    time.sleep(60)
else:
    print("[✖] Feed sync failed after 5 attempts. Please check logs.")

# Initialize OpenVAS and create an admin user
print("[+] Initializing OpenVAS scanner...")
admin_pass = input("Enter a secure password for the admin user: ")
run_command(f"sudo -u _gvm gvmd --create-user=admin --password='{admin_pass}'")
run_command("sudo -u _gvm gvmd --update")

# Restart OpenVAS services
print("[+] Restarting OpenVAS services...")
run_command("sudo systemctl restart ospd-openvas gvmd gsad")

# Final service status check
print("[+] Final service status check...")
for service in services:
    status = run_command(f"systemctl is-active --quiet {service}", check=False)
    if status == "active":
        print(f"[✔] {service} is running")
    else:
        print(f"[✖] {service} failed to start")

# Completion message
print("[✔] Installation complete!")
print("Access OpenVAS Web UI at: https://localhost:9392")
print("Login with username: admin and the password you provided.")
