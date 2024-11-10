### PDF Viewer with Flask and Socket.IO

---

## Overview

This project is a **PDF Viewer Web Application** built using **Flask** and **Socket.IO**. It allows an admin to upload a PDF file and share it with viewers in real time. The viewers can see the PDF document, navigate through pages, and adjust zoom levels. The application also provides synchronization between the admin and the viewers using WebSockets, ensuring that any page changes made by the admin are reflected for all viewers.

---

## Technologies Used

- **Flask**: A lightweight Python web framework used to handle routing, file uploads, and server-side processing.
- **Socket.IO**: A WebSocket library for real-time, bidirectional communication between clients and servers.
- **HTML, CSS, JavaScript**: Frontend technologies used to create the user interface.
- **PDF.js**: A popular JavaScript library for rendering PDF files in the browser.

---

## Features

1. **Admin Functionality**: 
    - Upload a PDF file.
    - Share a unique link with viewers.
    - Control the PDF navigation, which reflects on the viewers' screens.

2. **Viewer Functionality**:
    - View the PDF file uploaded by the admin.
    - Adjust the zoom level using "Zoom In" and "Zoom Out" buttons.

3. **Real-Time Synchronization**:
    - Any page changes made by the admin are automatically updated on all viewers' screens using WebSockets.

---

## Folder Structure

```
project-root/
├── app.py
├── templates/
│   ├── admin.html
│   └── viewer.html
├── uploads/
│   └── (Uploaded PDF files will be saved here)
└── requirements.txt
```

---


### 1. Run the Application
```bash
python app.py
```

### 2. Access the Application
- Open your web browser and navigate to:
  - **Admin Dashboard**: `http://localhost:5000/`
  - **Viewer Link**: `http://localhost:5000/viewer/<unique_id>`

The `<unique_id>` is generated when a PDF is uploaded by the admin.

---

## How to Use

### Admin Instructions:
1. Go to the admin dashboard (`http://localhost:5000/`).
2. Upload a PDF file using the file input.
3. Share the unique viewer link (e.g., `http://localhost:5000/viewer/<unique_id>`) with viewers.
4. Use the controls to change the page. The viewers will see the page changes in real time.

### Viewer Instructions:
1. Open the link provided by the admin.
2. Use the controls to navigate the document and adjust the zoom level.

---
