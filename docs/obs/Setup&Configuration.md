## 2. Initial Setup

### Open OBS Studio:
  * Launch OBS Studio after installation. If it doesn’t open automatically, find and open it manually.
  * The interface should resemble the one shown in the video.

       <img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/OBS.png" style="width:90%">

#### Create a Scene
  * In the "Scenes" section (bottom-left), click the "+" button to create a new scene.
  * Name the scene (e.g., "Guide") and confirm.

      <img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/initial-1.png" style="width:90%">
    
## 3. Configuration
### Configure Settings:
  - In the control section **[1]**, click "Settings" **[2]** in the bottom-right corner.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/control-tab-1.png" style="width:90%;">
    
  - A settings window will pop up; select the "Output" tab.
     - **Output Settings**:
       - Select "**Simple" mode [3]**.
       - Set the **recording path [4]** (where your files will be saved).
       - Choose **"High Quality, Medium File Size" [5]** for recording quality.
       - Select MP4 as the recording format.
       -  **Encoder [6]** (Platform Difference)
          - Choose according to your system:
            ### 🪟 Windows:
                     * NVIDIA GPU → **NVENC (H.264)**
                     * AMD GPU → **AMD Hardware Encoder**
                     * Intel GPU → **QuickSync**
                     * No dedicated GPU → **x264**
                     
            ### 🍎 macOS:
                     
                     * Apple Silicon (M1/M2/M3) → **Apple VT H264 Hardware Encoder**
                     * Intel Mac → **x264**
            
       

       - Click "OK" to save settings.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/output-01.png" style="width:70%;">

  - **Configure Audio Settings**:
       - Navigate to the "Audio" tab and select your microphone under **"Mic/Auxiliary. [7]**"

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/settings-audio-1.png" style="width:70%;">

  - **Configure Video Settings**:
      - In the "Video" tab, set the **resolution (e.g., 1440p or 1080p, based on your monitor) [8]**.
      - Choose the **FPS (60 for smoother recording, 30 is sufficient) [9]**.
      - Click "OK" to save all settings.

 <img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/settings-video-1.png" style="width:70%;">

## 4. Adding Sources

### Select Scene

Ensure your created scene is selected.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/adding-source-1.png" style="width:70%">

---

## Add Screen Capture (Platform Difference)

Click **"+"** in the Sources section.

### 🪟 On Windows:

Select → **Display Capture**

### 🍎 On macOS:

Select → **macOS Screen Capture**
(Older versions may show as *Display Capture*)

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/adding-source-2.png" style="width:60%">

- Select **Create New** and Click  **"OK"** to proceed.
- In the **next window**  select the **capture method:**
- Choose **Display Capture [3]** from the "Method" dropdown to capture the entire screen.
- Leave "Window Capture" or "Application Capture" unselected unless you want to focus on a specific window or application.
- Check "Show cursor" if you want the mouse cursor to be visible in the recording (optional).
- Click **"OK" [4]** to add the screen capture feed.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/adding-source-3.png" style="width:90%">

---















       

- **Add Webcam**:
  - Click the **"+" [2]** button in "Sources" again.
  - Select **"Video Capture Device" [3]** from the dropdown menu and click "OK."

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/video-capture-1.png" style="width:70%">

  - A window will appear with the following options:
    - **Create new  [4]**: Select this option and name the source **(e.g., "Video Capture Device 2")**.
    - **Add Existing**: Use this if you’ve already created a video capture source and want to reuse it (not applicable here since you’re adding a new one).
  
<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/video-capture-2.png" style="width:70%">

  - Ensure "Make source visible" is checked to display the webcam feed immediately.
  - Click **"OK" [5]** to proceed.

  - In the next window , select your webcam from the **"Device" [6]** dropdown **(e.g., "FaceTime HD Camera (Built-in)"** or your connected webcam).
  - Set the **"Preset" to "High" [7]** for better quality (optional adjustment).
  - Leave "Use Buffering" unchecked unless you experience lag (not recommended unless needed).
  - Click **"OK" [8]** to add the webcam feed.

 <img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/video-capture-3.png" style="width:70%">


## 5. Customization

- **Adjust Webcam Position and Size**:
  - In the OBS preview window, use the red dots around the webcam feed to resize or drag it to your preferred position (e.g., bottom-right corner, as adjusted to 777 px width and 45 px height in the example).

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/Adjust-webcam.png" style="width:70%">

- **Adjust Microphone Volume**:
  - Use the audio mixer in OBS to fine-tune your microphone volume as needed.


## 6. Recording

- **Start Recording**:
  - Click "Start Recording" in the bottom-right corner.
  - Minimize OBS Studio to record your screen and webcam simultaneously.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/recording.png" style="width:70%">



- **Stop Recording**:
  - When finished, return to OBS Studio and click "Stop Recording."
  - Locate the recorded file in the file path specified in the output settings.


























    ----



    Good idea 👍 — since **most settings are the same** in both versions, here is a **combined guide** with clear labels only where macOS and Windows are different.

This avoids repeating similar steps and clearly highlights platform differences.

---

# OBS Studio – Complete Setup Guide

### (macOS & Windows – Combined Version)

---

# 2. Initial Setup

## Open OBS Studio

* Launch OBS Studio after installation.
* If it does not open automatically, open it manually.
* The interface should look similar on both macOS and Windows.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/OBS.png" style="width:90%">

---

## ⚠️ Important – macOS Only (First Time Users)

Before adding Screen Capture:

1. Go to **System Settings → Privacy & Security → Screen Recording**
2. Enable permission for **OBS Studio**
3. Restart OBS if required

❗ If not enabled, screen recording may show a black screen.

*(Windows does NOT require this step.)*

---

## Create a Scene

* In the **Scenes** section (bottom-left), click the **"+"**
* Enter a name (e.g., "Guide")
* Click **OK**

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/initial-1.png" style="width:90%">

---

# 3. Configuration

Click **Settings** in the bottom-right corner.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/control-tab-1.png" style="width:90%;">

---

## Output Settings (Same for macOS & Windows)

* Go to **Output** tab
* Select **Simple Mode**
* Set **Recording Path**
* Recording Quality → **High Quality, Medium File Size**
* Recording Format → **MP4**

### Encoder (Platform Difference)

Choose according to your system:

### 🪟 Windows:

* NVIDIA GPU → **NVENC (H.264)**
* AMD GPU → **AMD Hardware Encoder**
* Intel GPU → **QuickSync**
* No dedicated GPU → **x264**

### 🍎 macOS:

* Apple Silicon (M1/M2/M3) → **Apple VT H264 Hardware Encoder**
* Intel Mac → **x264**

Click **OK** to save.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/output-01.png" style="width:70%;">

---

## Audio Settings (Same for Both)

* Go to **Audio Tab**
* Under **Mic/Auxiliary Audio**, select your microphone:

  * Windows example: *Microphone (Realtek Audio)*
  * macOS example: *MacBook Microphone* or external mic

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/settings-audio-1.png" style="width:70%;">

---

## Video Settings (Same for Both)

* Go to **Video Tab**
* Base Resolution → 1920x1080 (Recommended)
* FPS →

  * 30 FPS (Standard)
  * 60 FPS (Smoother recording)

Click **OK**

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/settings-video-1.png" style="width:70%;">

---

# 4. Adding Sources

## Select Scene

Ensure your created scene is selected.

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/adding-source-1.png" style="width:70%">

---

## Add Screen Capture (Platform Difference)

Click **"+"** in the Sources section.

### 🪟 On Windows:

Select → **Display Capture**

### 🍎 On macOS:

Select → **macOS Screen Capture**
(Older versions may show as *Display Capture*)

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/adding-source-2.png" style="width:60%">

* Select **Create New**
* Click **OK**

In the next window:

* Select monitor (if multiple displays)
* Enable **Show Cursor** (optional)
* Click **OK**

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/adding-source-3.png" style="width:90%">

---

## Add Webcam (Same for Both)

* Click **"+"**
* Select **Video Capture Device**
* Click **OK**

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/video-capture-1.png" style="width:70%">

* Select **Create New**
* Click **OK**
* Choose your webcam from **Device dropdown**

Examples:

* Windows → Integrated Camera / Logitech Webcam

* macOS → FaceTime HD Camera (Built-in)

* Preset → High (optional)

* Click **OK**

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/video-capture-3.png" style="width:70%">

---

# 5. Customization (Same for Both)

## Adjust Webcam Position

* Use the red borders to resize
* Drag to preferred position (e.g., bottom-right)

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/Adjust-webcam.png" style="width:70%">

---

## Adjust Microphone Volume

* Use the **Audio Mixer**
* Ensure levels stay in green/yellow (avoid red)

---

# 6. Recording

## Start Recording

* Click **Start Recording**
* Minimize OBS

<img src="https://raw.githubusercontent.com/LEARN-LK/OBS/main/img/recording.png" style="width:70%">

---

## Stop Recording

* Click **Stop Recording**
* Locate the file in your selected recording path

---

# 🔎 Quick Summary of Differences

| Feature               | Windows                 | macOS                                   |
| --------------------- | ----------------------- | --------------------------------------- |
| Screen Source Name    | Display Capture         | macOS Screen Capture                    |
| First-Time Permission | Not required            | Must enable Screen Recording permission |
| Hardware Encoder      | NVENC / AMD / QuickSync | Apple VT H264                           |

---

This version keeps:
✅ Common steps together
✅ Differences clearly marked
✅ Clean and beginner-friendly structure

If you want, I can now:

* Convert this to a **Trainer Script (what to say + what to click)**
* Prepare a **GitHub-ready Markdown version**
* Create a **PDF formatted training manual**
* Prepare a **15-minute demo session plan**



