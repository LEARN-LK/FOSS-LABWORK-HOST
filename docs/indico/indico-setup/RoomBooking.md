
# Steps to Use Room Booking for “National Research Conference 2025”

> This guide outlines how to set up and manage room bookings for the **National Research Conference 2025**, including how to add a location, assign permissions to a location manager (e.g., Dr. Silva), add a room, book a room, and optionally link it to the event timetable.

---

## LEARN Admin Tasks

### 1. Navigate to the Event
- Log in to your Indico instance.
- From the homepage or dashboard, find and select the event: **National Research Conference 2025**.

---

### 2. Access the Room Booking Section
1. On the event page, click the **gear icon** or **“Manage event”** to open the **Management Area**.
2. In the left sidebar, scroll down and click **Room bookings**.
3. You’ll see the **Room bookings [1]** tab with options. Click **“Book a room” [2]** to open the Room Booking Dashboard.

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/roombooking-1.png" width="60%">

---

### 3. Open the Room Booking Dashboard
- Once inside the Room Booking interface, click the **Administration [3]** tab in the right-hand sidebar to configure room booking settings.

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/roombookin-2.png" width="60%">

---

### 4. Add a New Location
1. In the left sidebar under **General Settings**, click **Locations [4]**.

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/roombooking-3.png" width="60%">

2. Click the **➕ Add [5]** button in the top-right.
3. In the **Add Location** popup, fill in the details:

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/roombooking-4.png" width="60%">

   - **Name [6]**: `Auditorium`
   - **Room name format [7]**: e.g., `{building}/{floor}-{number}` (e.g., `Auditorium/1-001`)
   - **Map URL template [8]** *(optional)*: e.g., `https://maps.example.com?room={building}/{floor}-{number}`
4. Click **Add** to create the location.

---

### 5. Assign a Location Manager (e.g., Dr. Silva)
1. From the Room Booking dashboard, go to: **Room Booking → Permissions**
2. Click the **+** button under **User [9]** or **Group**.
3. Search for **Dr. Silva** (Conference Manager).
4. Grant Dr. Silva the following rights:
   - **Can manage bookings**
   - **Room manager** *(if required for location approval)*
5. Click **Add** to apply the permissions.

---

## Location Manager Tasks (Performed by Dr. Silva)

### 6. Add Room to the Location

#### i. Open Room Booking Administration
1. Log in to Indico with admin rights.
2. Go to the event: **National Research Conference 2025**.
3. From the left sidebar, select **Room bookings**.
4. On the right sidebar, click the **Administration** tab.

---

#### ii. Open Locations in General Settings
1. In the left sidebar under **General Settings [1]**, click **Locations [2]**.

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/add-room-1.png" width="40%">

2. Find the previously created location: **Auditorium**.
3. Click on **Auditorium [3]** to open its details.

---

#### iii. Add a New Room
1. Inside the **Auditorium** location, click the **Add room [4]** button.

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/add-room-2.png" width="40%">
2. A popup window titled **Add Room** will open with three tabs:
   - **Basic Details**
   - **Location**
   - **Permissions**

---

#### iv. Fill in Basic Room Details
In the **Basic Details [5]** tab, provide:

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/add-room-3.png" width="60%">

- **Where is the key? [7]**: `Reception Desk, Auditorium`
- **Telephone [8]**: `+94 ##########`
- **Capacity [9]**: `200`
- Leave other optional fields blank unless needed.
- Click **Next** or move to the **Location** tab.

---

#### v. Complete the Location Tab [10]
Fill in the required fields as follows:

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/add-room-4.png" width="60%">

- **Name**: `Main Auditorium`
- **Site [11]**: `University of Peradeniya`
- **Building [12]**: `Arts Faculty Building`
- **Floor [13]**: `1`
- **Number [14]**: `001`
- > Example Format: `"Main Auditorium" located on Floor 1 of Arts Faculty Building`
- Click **Next** to go to the **Permissions** tab.

---

#### vi. Set Room Permissions
   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/add-room-5.png" width="60%">

In the **Permissions [15]** tab:
- **Booking Mode**:
  - Select **Public [16]** for open access
    **OR**
  - Select **Restricted [16]** to limit booking to selected users
    - If **Restricted**, check: *Restricted rooms can only be booked by users defined in the room ACL*
    - Click **+ Add [17]** and search for **Dr. Silva**
- Assign Dr. Silva the following permissions **[18]**:
  - **Manager**: Full control of room settings
  - **Moderate**: Approve/reject booking requests
  - **Override**: Book over existing reservations
- Click **Add** to save Dr. Silva's permissions.

---

#### vii. Save the Room
- Review all three tabs for accuracy.
- Click **Save** or **Add Room** to finish.
- The new room (**Main Auditorium [19]**) will now be listed under the **Auditorium** location.

   <img src="https://github.com/LEARN-LK/Indico/blob/main/img/add-room-6.png" width="60%">

---

### 7. Book a Room
1. Return to the **Room Booking dashboard**.
2. click on **list of Rooms** Tab`.

 <img src="https://github.com/LEARN-LK/Indico/blob/main/img/bookroom-1.png" width="60%">
3. Click **Book** next to the room (e.g., `Auditorium/1-001`)

 <img src="https://github.com/LEARN-LK/Indico/blob/main/img/bookroom-2.png" width="60%">
 
4. Fill in the booking form:
   - **Reason**: e.g., *“Conference Session”*
   - Confirm or adjust the selected time/location

 <img src="https://github.com/LEARN-LK/Indico/blob/main/img/bookroom-3.png" width="60%">
 
5. Click **Submit**
   > If room booking moderation is enabled, Dr. Silva will need to approve the request via **Bookings in My Rooms**.

---

### 8. Link Room to Timetable (Optional)
1. Go to the event’s **Management Area → Timetable**
2. Click **Add new session** or edit an existing one.
3. Assign the booked room (e.g., `Auditorium/1-001`) to the session.
4. Save your changes.
   > This allows participants to see room allocations directly from the event schedule.

---

## Notes
- **Required Fields**: All fields marked with (*) must be completed to add the room.
- **Permissions**: LEARN Admins must have appropriate rights to add locations and assign permissions. Dr. Silva’s actions depend on the assigned Location Manager rights.
- **Troubleshooting**:
  - Room not showing? Check if the location is active.
  - Error when saving? Avoid duplicate room names.
  - Booking issues? Ensure moderation settings are configured correctly.
