
## B. Category Creation and Manager Assignment

(*Performed by LEARN Indico Admin*)

###  Purpose:

To organize conferences by university and faculty/department structure, the LEARN Indico Admin creates a hierarchy of categories and assigns local organizers or university representatives as **Category Managers** at the department level. Additionally, a **Location Manager** is assigned to oversee room booking and management within the category.

---

###  Step-by-Step Instructions

#### Step 1: Create the Top-Level University Category

1. Visit the **Indico homepage**: `https://wsindico.learn.ac.lk/`

2. Click the ** pencil icon** (top-right) to access the **Category Management** area. <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/category-01.png" width="730">

3. On the homepage or relevant parent category, click **➕ Create subcategory**. <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/category-06.png" width="730">

4. Fill in the form:

   * **Title**: `University of Peradeniya`
   * **Description**: "Official category for events organized by University of Peradeniya"

     <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/category-02.png" width="730">

5. Click **Save**.

---

#### Step 2: Create Faculty and Department Subcategories

1. Inside the **University of Peradeniya** category, again click **➕ Create subcategory**.

2. Enter:

   * **Title**: `Faculty of Computing`
   * **Description**: e.g., “Events under Faculty of Computing”

3. Click **Save**.

4. Now within the **Faculty of Computing**, click **➕ Create subcategory** again.

5. Enter:

   * **Title**: `Department of Computer Science`
   * **Description**: “Events and workshops organized by the Department of Computer Science”

6. Click **Save**.

---

#### Step 3: Assign a Category Manager (e.g., for Department of Computer Science)

1. Navigate to **Department of Computer Science** category.

2. Click the **⚙️ gear icon** (top-right).

3. In the sidebar, go to **Protection**. <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/Category-03.png" width="730">

4. Under **Category Protection > Permissions**, click **Add User**. <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/category-07.png" width="430">

5. Search by name or email (e.g., `Dr. Silva`) – user must have an Indico account. <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/category-04.png" width="730">

6. Assign them the role of **Manager**. <img src="https://raw.githubusercontent.com/LEARN-LK/Indico/main/img/category-05.png" width="330">

7. Click **Save**.

---


#### Step 4: Assign a Location Manager (e.g., for Department of Computer Science)

1. Navigate to the **Department of Computer Science** category.
2. Click the **⚙️ gear icon** (top-right) to access category settings.
3. In the sidebar, go to **Room Booking** (if available) or return to the event management area and access **Room Booking → Permissions** under the category context.
4. Under **Permissions** or **Room Booking Permissions**, click **Add User**.
5. Search for a user (e.g., `Mohan Bandara`) – ensure they have an Indico account.
6. Assign the role of **Location Manager** with the following permissions:
   - **Manage**: Full control over room settings and bookings.
   - **Moderate**: Ability to approve or reject room booking requests.
   - **Override**: Permission to override existing bookings if needed.
7. Click **Save** to apply the changes.
8. Verify the assignment by checking the **Room Booking** dashboard, where Mohan Bandara should now manage rooms like "Main Auditorium" under the category.


---


### Updated Example Scenario

- **LEARN Indico Admin**:
  - Creates top-level category: **University of Peradeniya**
  - Adds subcategory: **Faculty of Computing**
  - Adds sub-subcategory: **Department of Computer Science**
  - Assigns **Dr. Silva** (UoP IT Coordinator) as the **Category Manager** for the Department of Computer Science.
  - Assigns **Mohan Bandara** as the **Location Manager** for room booking within the Department of Computer Science.

- **Dr. Silva can now**:
  - Create and manage all events under the Department of Computer Science category.
  - Enable abstract submission, registration, and room booking.
  - Assign editors, reviewers, and conference managers.

- **Mohan Bandara can now**:
  - Manage room bookings (e.g., "Main Auditorium") for events under the Department of Computer Science.
  - Approve or reject booking requests and resolve conflicts using override permissions.
  - Ensure room availability aligns with the conference schedule (8 Sep - 13 Sep 2025).
