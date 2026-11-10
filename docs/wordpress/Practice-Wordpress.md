
# **Practice Wordpress in VirtualBox**

### **Complete Step-by-Step Guide to Run WordPress Preconfigured Virtual Machine**

This guide lets you run a **ready-made WordPress instance** using either **VirtualBox** (Windows/Linux/macOS Intel/AMD)** or  (macOS Apple Silicon M1/M2/M3).
It includes automated setup scripts that start the virtual machine and open WordPress automatically at:

```
http://wordpress:8000
```

---

<!--
## ⚡️ Quick Start Overview

| Processor Type                  | Platform      | Virtualization Tool           | Setup Script | Download Section                                                       |
| ------------------------------- | ------------- | ----------------------------- | ------------ | ---------------------------------------------------------------------- |
| Intel / AMD (Windows)           | Windows       | VirtualBox                    | `.bat`       | [Part 1](https://drive.google.com/file/d/1lYzC243wAijfeDqiAr5Wwy7MT9qptdIA/view?usp=sharing)                  |
| Intel / AMD (Mac)               | macOS (Intel) | VirtualBox                    | `.sh`        | [Part 2](https://drive.google.com/file/d/1EppBMiV9cP6XPaNT0O9XzTQrPqVK7W0K/view?usp=sharing)                      |
| Apple Silicon (M series/Silver) | macOS (ARM)   | VirtualBox (ARM build) | `.sh`        | [Part 3](https://drive.google.com/file/d/1EppBMiV9cP6XPaNT0O9XzTQrPqVK7W0K/view?usp=sharing) |

---  -->

## ⚙️ **Part 1 — For Intel Users (Windows) VirtualBox**



### Video Guide :  For Intel Users (Windows) VirtualBox

<iframe width="560" height="315" src="https://ltube.ac.lk/embed?m=mUIXiu35X" frameborder="0" allowfullscreen></iframe>


### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`) for Intel User (Windows)
  👉 [Download for Windows (VirtualBox)](https://drive.google.com/file/d/1sH2K2QzgE3GH696Q7E3xGxjMEh-7jkE_/view?usp=sharing)

* Automation Script for Windows User (`.bat`)
  👉 [Download Windows Setup Script](https://drive.google.com/file/d/1zZNyNqEwkhaNB0eP6HmI1v-I9IATKSXL/view?usp=sharing)

Make sure both files are saved in the **same folder** (e.g., `Downloads\WordPress_VM`).

---

### **2. Install VirtualBox**

1. Visit [https://www.virtualbox.org](https://www.virtualbox.org).
2. Download and install VirtualBox (default settings are fine).

---

### **3. Prepare Windows System**

Before running the script, temporarily **disable security features** that may block VM imports or local web services.

#### 🛡️ **Disable Windows Defender Protections**

1. Open **Windows Security → Virus & threat protection**.
2. Click **Manage settings**.
3. Turn **OFF**:

   * Real-time protection
   * Dev Drive protection
4. If you use third-party antivirus (e.g., Avast, McAfee), **pause real-time protection** temporarily.

<img src="https://raw.githubusercontent.com/LEARN-LK/lms/master/img/diffender.jpeg?raw=true" alt="image" style="max-width: 100%;width: 500px;">




> ⚠️ Re-enable protections once WordPress setup is complete.

---

### **4. Run the Setup Script**

1. Right-click the downloaded `.bat` file → **Run as Administrator**.
2. The script will automatically:

   * Add the `127.0.0.1 WordPress` entry to your Windows hosts file
   * Import the `.ova` file automatically into VirtualBox
   * Start the WordPress virtual machine
   * Wait until the web server is ready
   * Launch WordPress in your browser at:
     👉 **[http://wordpress:8000](http://wordpress:8000)**

---

### **5. Login to WordPress**

* **Username:** `learn`
* **Password:** `wd123`

---

### **6. Troubleshooting (Windows)**

#### 🔹 *“VBoxManage.exe not found”*

Check your PATH variable:

1. Open **System Properties → Advanced → Environment Variables**.
2. In **System Variables**, find `Path`.
3. Click **Edit → New** → add:

   ```
   C:\Program Files\Oracle\VirtualBox\
   ```
4. Click **OK**, then rerun the bat file.

#### 🔹 *Network Access*

Ensure your VirtualBox network adapter is set to  **NAT (default)**.
If WordPress doesn’t load, restart the VM.

---

## ⚙️ **Part 2 — For Intel Users (Mac) VirtualBox**


### Video Guide :  For Intel Users (Mac) VirtualBox

<iframe width="560" height="315" src="https://ltube.ac.lk/embed?m=tNXuhhTva" frameborder="0" allowfullscreen></iframe>


### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`) for Intel User (Mac)
  👉 [Download for Mac (VirtualBox)](https://drive.google.com/file/d/12Lp0Z-E1WiHfdT06a-1-xSoBMIQBzJMR/view?usp=sharing)

* Automation Script for Mac User (`.sh`)
  👉 [Download Mac Setup Script](https://drive.google.com/file/d/1Z_4JjU7T9IWEhz3r1A73VxK09itO5zLn/view?usp=sharing)

Save both files in the **same folder** (e.g., `Downloads/WordPress_VM`).

---

### **2. Install VirtualBox**

1. Visit [https://www.virtualbox.org](https://www.virtualbox.org).
2. Download and install VirtualBox for macOS Intel.
3. After installation:

   * Open **System Settings → Privacy & Security**
   * If macOS blocks VirtualBox, click **Allow**

---

### **3. Run the `.sh` File to Start VM and Browser**

1. Open **Terminal**.
2. Drag the `.sh` file into the Terminal window.
3. Press **Enter**.

The script will automatically:

* Import the OVA file
* Start the Virtual Machine
* Launch WordPress in your default browser at:
  👉 **[http://wordpress:8000](http://wordpress:8000)**

> 💡 If you see “permission denied”, run:
>
> ```bash
> chmod +x autopart-wp.sh
> ```
>
> and retry.

---

### **4. Access WordPress**

Open your browser (if not already open) and visit:
👉 **[http://wordpress:8000/wp-admin](http://wordpress:8000/wp-admin)**

**Login Details**

* Username: `learn`
* Password: `wd123`

---

## ⚙️ **Part 3 — Setup Guide for Mac (Apple Silicon / Silver Processor)**


### Video Guide :  Setup Guide for Mac (Apple Silicon / Silver Processor

<iframe width="560" height="315" src="https://ltube.ac.lk/embed?m=BzhHpuHTx" frameborder="0" allowfullscreen></iframe>


### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`) for Apple Silicon (ARM)
  👉 [Download for Apple Silicon (VirtualBox)](https://drive.google.com/file/d/16WnM-IbnP1MKMGXkOsbiCxPs4l7AQHCI/view?usp=sharing)

* Automation Script for Mac User (`.sh`)
  👉 [Download Mac Setup Script](https://drive.google.com/file/d/11UVBByiSgx9_N84KudMyPw1WzboHHN1W/view?usp=sharing)

Save both files in the **same folder** (e.g., `Downloads/WordPress_VM`).

---

### **2. Install VirtualBox**

Download and install the **Apple Silicon (ARM64)** macOS / Apple Silicon hosts:
👉 [https://www.virtualbox.org/wiki/macOS / Apple Silicon hosts](https://download.virtualbox.org/virtualbox/7.2.4/VirtualBox-7.2.4-170995-macOSArm64.dmg)


After installation:

* Open **System Settings → Privacy & Security**
* If macOS blocks VirtualBox, click **Allow**

---

### **3. Run the `.sh` File to Start VM and Browser**

1. Open **Terminal**
2. Drag the `.sh` file into the Terminal window
3. Press **Enter**

The script will automatically:

* Import the OVA file
* Start the Virtual Machine
* Launch your browser at 👉 **[http://wordpress:8000](http://wordpress:8000)**

> 💡 If you see “permission denied”, run:
>
> ```bash
> chmod +x autopart-wp.sh
> ```
>
> and retry.

---

### **4. Access WordPress**

Once the VM is running:

* Open your browser (if not already open)
* Visit **[http://wordpress:8000/wp-admin](http://wordpress:8000/wp-admin)**
* **Username:** `learn`
* **Password:** `wd123`

---

## ⚙️ **Troubleshooting**

| Issue                           | Possible Fix                                                |
| ------------------------------- | ----------------------------------------------------------- |
| Browser doesn’t open            | Manually visit **[http://wordpress:8000/wp-admin](http://wordpress:8000/wp-admin)** |
| VM won’t start                  | Ensure VirtualBox is installed correctly                    |
| Path error (Windows)            | Check **System Path** variables                             |
| macOS blocks file               | Go to **System Settings → Privacy & Security → Allow**      |
| “Permission denied” in Terminal | Run `chmod +x autopart-wp.sh` and retry                        |
| WordPress doesn’t load             | Restart the VM or check network adapter (use NAT)   |

---
