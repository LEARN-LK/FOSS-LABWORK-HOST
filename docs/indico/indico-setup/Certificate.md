##  J: Customize Certificates and Generate Participation Documents (Indico v3.3.7)

###  **Step-by-Step Instructions**

---

### **Step 1: Access the Certificate Generator**

 **Navigation Path:**
**Management Area → Customize → Documents Template**

1. Go to the event’s **Management Area**.
2. Click on **Customize** in the left-hand menu.
3. Select **Documents Template [1]**.
4. Click **➕ Add New [2]** to create a new document.
5. Choose **Certificate of Attendance (V1) [3]** from the available options.

 <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/certificate-01.png" width="830">

---

### **Step 2: Customize the Template**

You’ll now see several customizable fields. Here's what each field does, with sample content using dynamic parameters.

####  **You can click “Sample Parameters”** to view the list of dynamic tags you can include. These include:
---

### **Customize Each Field (with Examples)**

| Field                        | Description                                     | Example                                                                                                                                    |
| ---------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Document Title [1]**           | Title displayed on top of the certificate.      | `Certificate of Participation`                                                                                                             |
| **Organizer Address [2]**        | Name and address of the organizing institution. | `University of Peradeniya, Faculty of Science, Peradeniya, Sri Lanka`                                                                      |
| **Venue [3]**                    | Physical or virtual venue.                      | `University Senate Hall` or `Zoom Platform (Online)`                                                                                       |
| **Logo [4]**                     | Upload a logo image.                            | *(Click “Upload Logo” and choose your image)*                                                                                              |
| **Certificate Text [5]**         | Main certificate message, using dynamic tags.   | `This is to certify that {name} from {affiliation} has participated in the {event_title} held from {start_date} to {end_date} at {venue}.` |
| **Place of Signature (1st) [6]** | Name and title of signatory 1.                  | `Dr. S.K. Perera\nChairperson – NRC 2025`                                                                                                  |
| **Place of Signature (2nd)** | Name and title of signatory 2.                  | `Prof. N. Jayasena\nDean – Faculty of Science`                                                                                             |
| **Place of Signature (3rd)** | (Optional) Name and title of a third signatory. | `Mr. R. Gunasekara\nConference Secretary`                                                                                                  |

---
<img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/certificatipn-03.png" width="530">


### **Step 3: Save the Template**

* Click **Save** after completing the fields.
* Optionally, use the **Preview** feature to check how the certificate looks with real sample data.

---


##  **Step 4: Generate Certificates for Participants**

 **Location:**
**Management Area → Organization → Registration → NRC 2025 Participant Registration → Registrations List**

---

1. In the **Management Area**, go to the **Organization** tab.

2. Click **Registration [1]**.

3. Under **List of Registration Forms**, locate and click on **NRC 2025 Participant Registration [2]**.
<img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/sent-certificate-1.png" width="530">

4. Click the **Registrations [3]** link to view the list of registered participants.

5. From the **Participants List**, you can:
    - *  Select **all participants  [4]**
    - *  Or select **individual participants** by checking the boxes.

 <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/sent-certificate-2.png" width="530">
 
6\. Click the **Action** dropdown (usually found above the list or in the toolbar).

7\. Choose **Generate Document [5]**.

 <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/sent-certificate-3.png" width="530">

---

###  **Document Generation Window**

A popup window will appear. Now fill in the following fields:

| Field                            | Description                                  | Example                                                                                                                         |
| -------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Document Template**            | Select the saved certificate template.       | `Certificate of Attendance – NRC 2025`                                                                                          |
| **Document Title [6]**               | Title shown on the document.                 | `Certificate of Participation`                                                                                                  |
| **Organizer Address [7]**            | Address of the organizing body.              | `LEARN, 65/5, Galle Road, Colombo 03, Sri Lanka`                                                                                |
| **Venue [8]**                        | Event location.                              | `Zoom Online Platform` or `University Senate Hall`                                                                              |
| **Logo [9]**                         | Upload your organization or conference logo. | *(Click Upload and select file)*                                                                                                |
| **Certificate Text [10]**             | Use dynamic fields for personalization.      | `This certifies that {name} from {affiliation} participated in {event_title}, held from {start_date} to {end_date} at {venue}.` |
| **Place of Signature (1st–3rd) [11]** | Names and titles of signatories.             | `Dr. S.K. Perera\nConference Chair`                                                                                             |

---

###  **Tick the Following Options**

*  **Remember settings [12]** (for future use)
*  **Publish document [13]** (makes it available for participants to download)
*  **Notify registrants via e-mail [14]** (sends the document directly to participant emails)

---

###  **Finalize**

Click the **Publish and Send to Registrants [15]** button.

>  Participants will now receive their customized certificates via email, and they can also download them from their registration page.

---
