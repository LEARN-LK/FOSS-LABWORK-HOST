
### 🔹 **Step 4: Add Users and Assign Roles in DSpace**

---

<!-- #### 🧭 **Step 4.1: Add Users (E-People) to the System** [1]

Before assigning roles, you must first create user accounts.

1. Go to the **Admin Toolbar**
2. Click **Access Control** → **People**
<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/Admin-dashboard-Epeople-01.png" alt="image" style="max-width: 100%;width: 200px;">
   
3. Click **Add E-Person** [2]
<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/add-Epeople.png?raw=true" style="max-width: 100%;width: 600px;">

For each user, fill in:

* **Email**: e.g., `student123@uni.edu`
* **First Name** / **Last Name**: e.g., `Student / One`
* **Password**: Set a default or temporary password
* Click **Create** [3]



  <img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/Add-Epeople-subimitter.png?raw=true" alt="image" style="max-width: 100%;width: 450px;">
  

Repeat this for all the users you want to assign roles to, such as:

* `student123@uni.edu`
* `prof.reviewer@uni.edu`
* `editor.cs@uni.edu`
* `finaleditors.cs@uni.edu`

---    -->

#### 🧭 **Step 4.1: Assign Roles to Users**

Navigate to:
**Communities & Collections → Faculty of Science → Computer Science → Final Year Projects 2024**

1. On the right side, click the **Edit button (pencil icon) [4]** for the **Final Year Projects 2024** collection.
<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/eAR1-Editrole.png" alt="image" style="max-width: 100%;width: 450px;">   

2. Click on **Assign Roles**
<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/eAR2-Assignrole.png" alt="image" style="max-width: 100%;width: 450px;">   

---

### 👤 **Submitter** (e.g., `student123@uni.edu`)

1. In the **Submitters** section, click **Create** [6]
   
<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/submitter-add-01.png" alt="image" style="max-width: 100%;width: 450px;">
    
2. Click on the generated group (e.g., `COLLECTION_..._SUBMIT`) [7]

<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/submitter-add-02.png" alt="image" style="max-width: 100%;width: 450px;">

   
3. Click **Add E-Person**[5]
4. Search for the email (e.g., `student123@uni.edu`)

   * If not found, go back and add the E-Person first (Step 4.1)
5. Select the user → Click **Add** [8]

<img src="https://raw.githubusercontent.com/LEARN-LK/DSpace/main/imgs/submitter-add-03.png" alt="image" style="max-width: 100%;width: 450px;">
   
6. Click **Save Changes**

---

### 👤 **Reviewer** (e.g., `prof.reviewer@uni.edu`)

1. Switch to the **Workflow** tab
2. Under the **Review Step**, click **Create**
3. Click the group (e.g., `COLLECTION_..._REVIEW`)
4. Click **Add E-Person**
5. Search for `prof.reviewer@uni.edu` → Select → Add → Save

---

### 👤 **Editor** (e.g., `editor.cs@uni.edu`)

1. Go back to **Assign Roles**
2. Under the **Curators** section, click **Create**
3. Click the group (e.g., `COLLECTION_..._CURATE`)
4. Click **Add E-Person**
5. Search for `editor.cs@uni.edu` → Select → Add → Save

---

### 👤 **Final Editor** (e.g., `finaleditors.cs@uni.edu`)

You can treat **Final Editors** as an extended curator group or create a **new custom group** for post-review metadata editing:

**Option A** – Add to Curators:

* Add `finaleditors.cs@uni.edu` to the **Curators** group (same as above)

**Option B** – Create a custom group:

1. Go to **Access Control → Groups**
2. Click **Create Group** → Name it `FinalEditors_2024`
3. Add `finaleditors.cs@uni.edu` as a member
4. Assign this group specific permissions (if needed) via **Authorization → Resource Policies**

---

