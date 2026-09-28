






# **Practice Moodle in VirtualBox**

### **Complete Step-by-Step Guide to Run Moodle Preconfigured Virtual Machine**

This guide lets you run a **ready-made Moodle instance** using either **VirtualBox** (Windows/Linux/macOS Intel/AMD)** or  (macOS Apple Silicon M1/M2/M3).
It includes automated setup scripts that start the virtual machine and open Moodle automatically at:

```
http://moodle:9000
```

---

<!--## ⚡️ Quick Start Overview

| Processor Type                  | Platform      | Virtualization Tool           | Setup Script | Download Section                                                       |
| ------------------------------- | ------------- | ----------------------------- | ------------ | ---------------------------------------------------------------------- |
| Intel / AMD (Windows)           | Windows       | VirtualBox                    | `.bat`       | [Part 1](https://drive.google.com/file/d/1lYzC243wAijfeDqiAr5Wwy7MT9qptdIA/view?usp=sharing)                  |
| Intel / AMD (Mac)               | macOS (Intel) | VirtualBox                    | `.sh`        | [Part 2](https://drive.google.com/file/d/1EppBMiV9cP6XPaNT0O9XzTQrPqVK7W0K/view?usp=sharing)                      |
| Apple Silicon (M Series/Silver) | macOS (ARM)   | VirtualBox (ARM build) | `.sh`        | [Part 3](https://drive.google.com/file/d/1EppBMiV9cP6XPaNT0O9XzTQrPqVK7W0K/view?usp=sharing) |

--- -->

## ⚙️ **Part 1 — For Intel Users (Windows) VirtualBox**

<h2> Video Guide - Practice Moodle in VirtualBox (Windows)</h2>
<iframe width="560" height="315" src="https://ltube.ac.lk/embed?m=EqJ0hhewm" frameborder="0" allowfullscreen></iframe>

### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`) for Intel User (Windows)
  👉 [Download for Windows (VirtualBox)](https://drive.google.com/file/d/1PQkj9OFvMLmeoYCvKyDjWV06VEp-Nwbk/view?usp=sharing)

* Automation Script for Windows User (`.bat`)
  👉 [Download Windows Setup Script](https://drive.google.com/file/d/14wCCr7081K3877nfIRaNutB8hCRsgGJ9/view?usp=sharing)

Make sure both files are saved in the **same folder** (e.g., `Downloads\Moodle_VM`).

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

> ⚠️ Re-enable protections once Moodle setup is complete.

---

### **4. Run the Setup Script**

1. Right-click the downloaded `.bat` file → **Run as Administrator**.
2. The script will automatically:

   * Add the `127.0.0.1 moodle` entry to your Windows hosts file
   * Import the `.ova` file automatically into VirtualBox
   * Start the Moodle virtual machine
   * Wait until the web server is ready
   * Launch Moodle in your browser at:
     👉 `http://moodle:9000`

---

### **5. Login to Moodle**

* **Username:** `moodle`
* **Password:** `Mdl@1234`

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

Ensure your VirtualBox network adapter is set to **NAT (default)**.
If Moodle doesn’t load, restart the VM.

---

## ⚙️ **Part 2 — For Intel Users (Mac) VirtualBox**

<h2> Video Guide - Practice Moodle in VirtualBox (Mac -Intel)</h2>

<iframe width="560" height="315" src="https://ltube.ac.lk/embed?m=XCeQdpcoY" frameborder="0" allowfullscreen></iframe>

### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`) for Intel User (Mac)
  👉 [Download for Mac (VirtualBox)](https://drive.google.com/file/d/1FLTVFAJnVV4rmu04fMtf0YQW3cmtvYxI/view?usp=sharing)

* Automation Script for Mac User (`.sh`)
  👉 [Download Mac Setup Script](https://drive.google.com/file/d/1Aq_XVHcH06PshUcIOPaHbjrEpxDHVrE-/view?usp=sharing)

Save both files in the **same folder** (e.g., `Downloads/Moodle_VM`).

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
* Launch Moodle in your default browser at:
  👉 **[http://moodle:9000](http://moodle:9000)**

> 💡 If you see “permission denied”, run:
>
> ```bash
> chmod +x autopart-moodle.sh
> ```
>
> and retry.

---

### **4. Access Moodle**

Open your browser (if not already open) and visit:
👉 **[http://moodle:9000](http://moodle:9000)**

**Login Details**

* Username: `moodle`
* Password: `Mdl@1234`

---

## ⚙️ **Part 3 — Setup Guide for Mac (Apple Silicon / Silver Processor)**



<h2> Video Guide - Practice Moodle in VirtualBox (Mac -Silicon)</h2>

<iframe width="560" height="315" src="https://ltube.ac.lk/embed?m=x15bHp0D7" frameborder="0" allowfullscreen></iframe>


### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`) for Apple Silicon (ARM)
  👉 [Download for Apple Silicon (VirtualBox)](https://drive.google.com/file/d/1xD8Uc0pzQrDwEcN6shrW50o8iPsFmoU_/view?usp=sharing)

* Automation Script for Mac User (`.sh`)
  👉 [Download Mac Setup Script](https://drive.google.com/file/d/19kXC7tgRKqfWwHDdo8ZXemetT5-_fHoN/view?usp=sharing)

Save both files in the **same folder** (e.g., `Downloads/Moodle_VM`).

---

### **2. Install VirtualBox**

Download and install the **Apple Silicon (ARM64)** Apple Silicon hosts:
👉 [https://www.virtualbox.org/wiki/](https://download.virtualbox.org/virtualbox/7.2.4/VirtualBox-7.2.4-170995-macOSArm64.dmg)


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
* Launch your browser at 👉 **[http://moodle:9000](http://moodle:9000)**

> 💡 If you see “permission denied”, run:
>
> ```bash
> chmod +x autopart-moodle.sh
> ```
>
> and retry.

---

### **4. Access Moodle**

Once the VM is running:

* Open your browser (if not already open)
* Visit **[http://moodle:9000](http://moodle:9000)**
* **Username:** `moodle`
* **Password:** `Mdl@1234`

---

## ⚙️ **Troubleshooting**

| Issue                           | Possible Fix                                                |
| ------------------------------- | ----------------------------------------------------------- |
| Browser doesn’t open            | Manually visit **[http://moodle:9000](http://moodle:9000)** |
| VM won’t start                  | Ensure VirtualBox is installed correctly                    |
| Path error (Windows)            | Check **System Path** variables                             |
| macOS blocks file               | Go to **System Settings → Privacy & Security → Allow**      |
| “Permission denied” in Terminal | Run `chmod +x autopart-moodle.sh` and retry                        |
| Moodle doesn’t load             | Restart the VM or check network adapter (use NAT)   |

---
