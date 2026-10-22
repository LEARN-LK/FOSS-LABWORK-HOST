## **Using WordPress, Build Your Own Website**  

WordPress is one of the most popular and user-friendly platforms for creating websites, whether for personal projects, businesses, or blogs. This guide will walk you through the step-by-step process of building your own website using WordPress. From planning your design to setting up pages and customizing your site, you'll learn how to create a professional and functional website with ease.

### **Getting Started with Website Design**  

Using WordPress, build your own website. This guide covers how to create a website. First, you should have an idea of the design you want to create. In this guide, I will walk you through building a website based on the attached wireframe. 

<img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/%5Cwireframe.jpeg" alt="image" style="max-width: 100%;width: 600px;">

Here’s a step-by-step guide to creating your website using WordPress based on above wireframe:

### Workshop Materials :- [Download here](https://drive.google.com/drive/folders/1J5aJy9V4vHGXT4jaAsZQL0Re8d-L0OYn?usp=sharing) 

---

# 🌐 Complete Step-by-Step Guide: Building the LEARN Website

## Step 1: Install Theme and Plugins

1. Log in to your WordPress Dashboard (`[yourdomain.com/wp-admin](https://yourdomain.com/wp-admin)`).
2. **Install the Theme:**
* Go to **Appearance → Themes**.
* Locate or search for **Twenty Twenty-Five**, click **Activate**.


3. **Install Required Plugins:**
* Go to **Plugins → Add New Plugin**.
* Search for **Smart Slider 3**, click **Install Now**, and then **Activate**.
* Search for **Contact Form 7**, click **Install Now**, and then **Activate** *(optional, for your contact page)*.



---

## Step 2: Create Pages and Set Static Homepage

1. Go to **Pages → Add New Page**.
2. Create and **Publish** the following four pages:
* **Home**
* **About**
* **Services**
* **Contact Us**


1. Create a **“Home”** Page in WordPress

2. In your WordPress dashboard, go to: **Pages → Add New**

<img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/001-page-add.png" alt="image" style="max-width: 100%;width: 600px;">

3. If a setup pop-up window appears, close it.

<img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/002-close-choose-pattern.png" alt="image" style="max-width: 100%;width: 600px;">

4. In the page title field, type: **Home**

<img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/003-rename-thepage.png" alt="image" style="max-width: 100%;width: 600px;">


5. Click the **Publish button** (top right corner).

6. Once the page is published, click the **WordPress logo / Dashboard link (top-left corner)** to go back to the main Dashboard.

<img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/005-back-todashbaord.png" alt="image" style="max-width: 100%;width: 600px;">


3. Set your homepage:

 - Once the page is published, click the **WordPress logo / Dashboard link (top-left corner)** to go back to the main Dashboard.

<img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/005-back-todashbaord.png" alt="image" style="max-width: 100%;width: 600px;">

 -  Go to **Settings → Reading**, select **"A static page"**, and choose **"Home"**.
  
   <img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/Reading.png" alt="image" style="max-width: 100%;width: 600px;">
  
   <img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/Static.png" alt="image" style="max-width: 100%;width: 600px;">

 -  Click Save

   <img src="https://raw.githubusercontent.com/LEARN-LK/Open-Source-Softwares/main/img/2.1-then-click-save.png" alt="image" style="max-width: 100%;width: 600px;">
---



## Step 3: Build the Global Header (Logo & Navigation)

*Note: In the Twenty Twenty-Five block theme, headers are global elements edited through the Site Editor.*

1. Go to **Appearance → Editor**.
2. Click on **Patterns** (or **Template Parts**), then select **Header**.
3. Click the edit icon.
4. Set up a **Row** or **Group** block with **Space Between** alignment:
* **Left Side:** Add an **Image** block and upload your **LEARN** logo image (with the blue text underneath).
* **Right Side:** Add a **Navigation** block, and add menu links pointing to **About**, **Contact Us**, and **Services**.


5. Click **Save**.

---

## Step 4: Create the Hero Slider

1. Click on **Smart Slider** in your left WordPress dashboard menu.
2. Click **New Project** → **Create a New Project** (Slider type: Simple, Fullwidth).
3. Add a slide and configure it:
* **Background:** Upload the blue interconnected network nodes graphic.
* **Contents:** Add the central circular logo graphic (`LEARN 35 Years of Excellence`), a heading text block reading `Connecting Research & Education Community of Sri Lanka`, and a button widget labeled `Read More`.


4. Click **Save**.
5. Copy the generated **Shortcode** (e.g., `[smartslider3 slider="1"]`).

---

## Step 5: Build the Homepage Content (Using Visual Editor)

1. Go to **Pages → Home** and click **Edit**.
2. Build the page section-by-section using the drag-and-drop **Visual Editor**:

### Section 1: Hero Slider

* Click the **`+` (Add block)** button, search for **Shortcode**, and select it.
* Paste your Smart Slider 3 shortcode inside (e.g., `[smartslider3 slider="1"]`).
* Add a **Spacer** block underneath set to **40px**.

### Section 2: LEARN Intro Section

* Add a **Columns** block and select the **50 / 50** (two equal columns) layout.
* **Left Column:**
* Add a **Heading** block (`H2`), type `LEARN`.
* Add a **Paragraph** block underneath and paste the introductory text (*"Lorem ipsum dolor sit amet..."*).


* **Right Column:**
* Add an **Image** block and upload the **LEARN 35 Years of Excellence** badge graphic.


* Add a **Spacer** block below the columns set to **60px**.

### Section 3: "Our services" Section

* Add a **Heading** block, type `Our services`, and align it to the **Center**.
* Add a **Spacer** block set to **30px**.
* Add a **Columns** block and choose **4 Columns**.
* Set up each of the 4 columns:
* **Column 1 (`eduID`):** Add an **Image** block (upload round eduID image, set width/height to `180px` and style with rounded borders / 100px radius). Add a **Heading** (`H3`) titled `eduID`. Add a **Paragraph** description block.
* **Column 2 (`LIAF`):** Add an **Image** block (upload LIAF standing icon, `180x180px`, rounded). Add a **Heading** (`H3`) titled `LIAF`. Add a **Paragraph** description block.
* **Column 3 (`Video Conferencing`):** Add an **Image** block (upload blue screen icon, `180x180px`, rounded). Add a **Heading** (`H3`) titled `Video Conferencing`. Add a **Paragraph** description block.
* **Column 4 (`eduVPN`):** Add an **Image** block (upload eduVPN shield icon, `180x180px`, rounded). Add a **Heading** (`H3`) titled `eduVPN`. Add a **Paragraph** description block.


* Add a **Spacer** block below the 4 columns set to **60px**.

### Section 4: About Section

* Add a **Columns** block and choose the **50 / 50** layout.
* **Left Column:**
* Add an **Image** block and upload the **3D Wireframe Network Sphere** graphic.


* **Right Column:**
* Add a **Heading** block (`H2`), type `About`.
* Add **Paragraph** blocks underneath containing the organization history and membership details (*"We celebrated our 30th anniversary in 2019..."* and *"LEARN currently has 16 full members..."*).


* Click **Update / Publish** to save your homepage.

---

## Step 6: Build the Global Footer

1. Go back to **Appearance → Editor**.
2. Select **Patterns** (or **Template Parts**) → **Footer** and click **Edit**.
3. Add the following elements centered:
* An **Image** block with the small centered red/pink **LEARN** logo.
* A **Paragraph** block reading: `Proudly powered by WordPress`.
* A **Social Icons** block with links/icons for Facebook, Twitter, and WordPress.


4. Click **Save**.

---

## Step 7: (Optional) Set Up Contact Form Page

1. Go to **Contact → Contact Forms** and copy your form shortcode (e.g., `[contact-form-7 id="..."]`).
2. Go to **Pages → Contact Us**.
3. Add a **Shortcode** block, paste your Contact Form 7 shortcode, and click **Publish**.