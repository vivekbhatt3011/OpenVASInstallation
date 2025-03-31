OpenVAS Automated Installation Script 🚀
This Python script automates the installation and setup of OpenVAS (Greenbone Vulnerability Management - GVM) on a Debian-based system (Ubuntu/Kali). It simplifies the process by handling package installation, service configuration, feed syncing, and user creation.

Features
✅ Automated installation – Installs OpenVAS with all necessary dependencies.
✅ Service management – Starts and verifies OpenVAS services (gvmd, gsad, ospd-openvas).
✅ Feed synchronization – Ensures up-to-date vulnerability databases with retry logic.
✅ Admin account setup – Prompts for a secure password and initializes OpenVAS.
✅ Error handling – Provides status checks and failure notifications.

Usage
bash
Copy
Edit
git clone https://github.com/your-repo/openvas-install.git
cd openvas-install
python3 openvas_install.py
Note: Run the script with sudo privileges.

Access OpenVAS Web UI:
🔗 URL: https://localhost:9392
👤 Login: admin
🔑 Password: Set during installation

Requirements
Ubuntu 20.04 / 22.04 or Kali Linux

Internet connection for downloading dependencies

sudo privileges

Contributions & Issues
Feel free to submit pull requests or report any issues in the repository. 🚀
