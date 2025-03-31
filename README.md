# OpenVAS Installation Script 🚀

## Overview
This script automates the installation of **OpenVAS (Greenbone Vulnerability Management - GVM)** on Debian-based systems such as Ubuntu and Kali Linux. It streamlines package installation, service configuration, feed syncing, and admin user setup.

## Features
- ✅ **Automated Installation** – Installs OpenVAS with all necessary dependencies.
- ✅ **Service Management** – Starts and verifies OpenVAS services (`gvmd`, `gsad`, `ospd-openvas`).
- ✅ **Feed Synchronization** – Ensures up-to-date vulnerability databases with retry logic.
- ✅ **Admin Account Setup** – Prompts for a secure password and initializes OpenVAS.
- ✅ **Error Handling** – Provides status checks and failure notifications.

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/your-repo/openvas-install.git
cd openvas-install

# Run the installation script
sudo python3 openvas_install.py
```

## Access OpenVAS Web UI
- **URL:** `https://localhost:9392`
- **Username:** `admin`
- **Password:** Set during installation

## Requirements
- Ubuntu 20.04 / 22.04 or Kali Linux
- Internet connection for downloading dependencies
- `sudo` privileges

## Contributing & Issues
Feel free to submit **pull requests** or report any **issues** in the repository. 🚀
