# UBL Operations & Compliance Tracker (Internal MIS)

An automated internal Management Information System (MIS) dashboard designed for United Bank Limited (UBL) branch operations. This system streamlines the logging of new account files, tracks core compliance benchmarks (Biometric, CNIC, and Source of Income), and dynamically computes verification statuses through a secure server-side infrastructure.

---

## 🚀 Core Features

- **Dynamic Account Logging:** Seamless registration interface capturing applicant details, operational branches, and distinct account categories.
- **Automated Compliance Engine:** Server-side logic automatically computes file status (`Approved`, `Pending`, or `Compliance Hold`) based on mandatory verification parameters.
- **Live Operation Stream:** Asynchronous updates using Fetch API to synchronize the frontend interface with the centralized database state without page reloads.
- **State Mutation Controls:** Internal action toggles allowing banking officers to manually transition compliance streams (`Clear` / `Hold`) upon verification.
- **Corporate Branding:** Styled meticulously matching standard corporate visual identity guidelines of United Bank Limited.

---

## 🛠️ System Architecture & Tech Stack

- **Frontend:** HTML5, CSS3 (CSS Variables, Responsive Grid Layout), Vanilla JavaScript (Asynchronous Fetch API).
- **Backend:** Python, Flask Web Framework (WSGI Server Routing, RESTful APIs, JSON Serialization).
- **Cross-Origin Support:** Flask-CORS integration ensuring standardized security validation communication layers.

---

## 📁 Repository Directory Structure

text
ubl_compliance_tracker/
│
├── app.py                   
├── requirements.txt         
├── templates/
│   └── index.html          
└── README.md              


## ⚡ Setup & Local Execution Instructions
Follow these chronological commands to initialize and run the web application locally:
### 1. Prerequisite Verification
Ensure that Python 3.8+ and pip are fully configured on your local machine operating system variables.
### 2. Environment Installation
Open your terminal/command prompt inside the root directory and execute the following deployment script:
bash
pip install -r requirements.txt


### 3. Initialize the WSGI Server
Launch the backend microservice engine by triggering the main runtime configuration file:
bash
python app.py


### 4. Access the Application Dashboard
Once the local development network channel establishes running states, open your web browser and target the designated local interface port:
text
[http://127.0.0.1:5003](http://127.0.0.1:5003)


## 🌐 Active REST API Endpoints Reference
| HTTP Method | API Endroute Route | Operational Functionality |
|---|---|---|
| GET | / | Serves the main client-side user interface dashboard template. |
| GET | /api/records | Fetches the comprehensive list of active operational file records. |
| POST | /api/register-log | Processes incoming log payloads and computes compliance states. |
| POST | /api/update-status | Mutates existing entity verification statuses across index arrays. |
## 👥 Branch Collaboration & Contributors
 * **Zainab Sarfraz** - Lead Developer & Software Architecture Designer
 * **Saqib (saqibutm)** - Assigned Code Contributor & Operational Reviewer
*Disclaimer: This repository serves strictly as an academic prototype developed during the UBL Internship Program tenure to simulate operational performance standardization protocols.*
