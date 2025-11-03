

# **Practice Moodle in VirtualBox / UTM**

### **Complete Step-by-Step Guide to Run Moodle Preconfigured Virtual Machine**

This guide lets you run a **ready-made Moodle instance** using either **VirtualBox** (Windows/Linux/macOS Intel/AMD) or **UTM** (macOS Apple Silicon M1/M2/M3).
It includes automated setup scripts that start the virtual machine and open Moodle automatically at:

```
http://moodle:9000
```

---

## ⚙️ **Part 1 — For Windows Users (VirtualBox)**

### **1. Download Required Files**

#### 📦 From Google Drive:

* VM Image (`.ova`)
  👉 [Download for Windows (VirtualBox)](https://drive.google.com/file/d/1AUnJanfNOT-sOQ_8J8ihS8WfgQdSTEVR/view?usp=sharing)
* Automation Script (`.bat`)
  👉 [Download Windows Setup Script](https://drive.google.com/file/d/your-windows-bat-link/view?usp=sharing)

Make sure both files are saved in the **same folder** (e.g., `Downloads\Moodle_VM`).

---

### **2. Install VirtualBox**

1. Visit [https://www.virtualbox.org](https://www.virtualbox.org).
2. Download and install VirtualBox (default settings are fine).
3. Restart your computer after installation.

---

### **3. Prepare Windows System**

Before running the script, make sure to temporarily **disable security features** that may block VM imports or local web services:

#### 🛡️ **Disable Windows Defender Protections**

1. Open **Windows Security** → **Virus & threat protection**.
2. Click **Manage settings**.
3. Turn **OFF**:

   * **Real-time protection**
   * **Dev Drive protection**
4. If you use other antivirus software (e.g., Avast, McAfee), **pause real-time protection** temporarily.

> ⚠️ Re-enable protections once Moodle setup is complete.

---

### **4. Run the Setup Script**

1. Right-click the downloaded `.bat` file → **Run as Administrator**.
2. The script will:

   * Add the `127.0.0.1 moodle` entry to your Windows hosts file
   * Import the `.ova` file automatically into VirtualBox
   * Start the Moodle virtual machine
   * Wait until the web server is ready
   * Launch Moodle automatically in your browser at
     `http://moodle:9000`

---

### **5. Login to Moodle**

In the browser, log in using:

* **Username:** `moodle`
* **Password:** `Mdl@1234`

---

### **6. Troubleshooting (Windows)**

#### 🔹 *Environment Variable / PATH Issue*

If the script shows an error like **“VBoxManage.exe not found”**, check your PATH:

1. Open **System Properties → Advanced → Environment Variables**.
2. In **System Variables**, find `Path`.
3. Click **Edit** → **New** → add:

   ```
   C:\Program Files\Oracle\VirtualBox\
   ```
4. Click **OK**, then reopen Command Prompt and try again.

#### 🔹 *Network Access*

Make sure your VirtualBox network adapter is set to **Bridged Adapter** or **NAT** (default).
If Moodle doesn’t load, try restarting the VM.

---



## Part - 2 🍎 Setup Guide for Mac (Apple Silicon / Silver Processor)

### Step 1 – Install VirtualBox

Download and install the **Apple Silicon (arm64)** test build:
👉 [https://www.virtualbox.org/wiki/Testbuilds](https://www.virtualbox.org/wiki/Testbuilds)

> Look for **“macOS / arm64 (Apple Silicon)”** under **Development Snapshots**.

After installation:

* Open **System Settings → Privacy & Security**
* If macOS blocks VirtualBox, click **Allow**

---

### Step 2 – Run the `.sh` File to Start VM and Browser

1. Open **Terminal**
2. Drag the provided `.sh` file into the Terminal window
3. Press **Enter**

The script will automatically:

* Import the OVA file
* Start the Virtual Machine
* Launch your default browser at 👉 **[http://moodle:9000](http://moodle:9000)**

> 💡 If you get “permission denied”, run:
>
> ```bash
> chmod +x yourfile.sh
> ```
>
> then retry.

---

### Step 3 - Access Moodle

Once the VM is running:

* Open your browser (if not already open)
* Visit **[http://moodle:9000](http://moodle:9000)**
* Log in using the credentials provided in your setup notes

---

## ⚙️ . Troubleshooting

| Issue                | Possible Fix                                                |
| -------------------- | ----------------------------------------------------------- |
| Browser doesn’t open | Manually visit **[http://moodle:9000](http://moodle:9000)** |
| VM won’t start       | Ensure VirtualBox is installed properly                     |
| Path error (Windows) | Check **System Path** variables                             |
| macOS blocks file    | Go to **System Settings → Privacy & Security → Allow**      |

---

