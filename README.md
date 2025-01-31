# north90chat

# Chat Application

## Introduction
This is a real-time chat application built using **Python, Django, Django Channels, Daphne, HTML, CSS, and JavaScript**. The application allows users to sign up, log in, and engage in real-time conversations. The frontend ensures responsiveness and usability, while Django handles authentication and message storage.

---

## Features

### Frontend Development
1. **Responsive Webpage**
   - Fixed navbar that does not move when scrolling.
   - Three sections below the navbar:
     - **Left menu** (collapsible)
     - **Main content area**
     - **Right-side panel**
   - A footer at the bottom.
   


---

### Django Backend Development
1. **User Authentication:**
   - Users can sign up and log in securely.
   
2. **User List Display:**
   - All registered users are displayed in a collapsible left menu.
   
3. **Real-Time Chat Functionality:**
   - Users can initiate a chat by selecting another user from the menu.
   - Messages are stored in the database for future retrieval.
   - Old messages are displayed in the chat interface.
   - **Django Channels and Daphne** handle WebSocket-based real-time communication.
 

---

## Installation & Setup

### Prerequisites
- Python 3.x
- Django
- Django Channels
- Daphne
- SQLite or PostgreSQL
- HTML, CSS, and JavaScript

### Installation Steps
#### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd <project-folder>
