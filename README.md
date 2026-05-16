# Enhanced Learning Management System (LMS)

A robust, multi-role full-stack Learning Management System designed to bridge the gap between education and accessibility. This platform enables seamless administration of educational courses, interactive student learning, and structured funding opportunities through external sponsors. Built with Python, Django, and the Django REST Framework (DRF).

---

## 🚀 Key Features

The platform is engineered around **four core user roles**, each possessing distinct permissions, workflows, and dashboards:

### 1. Admin Dashboard
* **Full System Control:** Manage all users (Instructors, Students, Sponsors) and monitor global site activity.
* **Content Moderation:** Review and approve newly created courses and track system-wide enrollments.
* **Financial Oversight:** Monitor sponsor fundings, distribution tracking, and system analytics.

### 2. Instructor Suite
* **Course Creation & Management:** Full CRUD operations for building structured courses with categories, tags, and modules.
* **Interactive Assignments:** Create, distribute, and grade student assignment submissions.
* **Student Tracking:** Monitor enrollment numbers and track performance metrics inside individual courses.

### 3. Student Hub
* **Course Enrollment:** Browse, filter, and search available courses by categories or instructors to enroll instantly.
* **Learning Portal:** Access course materials, download resources, and view structured modules.
* **Assignment Submission:** Submit coursework seamlessly and track grading/feedback directly from instructors.
* **Sponsorship Applications:** Apply for financial aid or course funding directly to active sponsors.

### 4. Sponsor Portal
* **Educational Philanthropy:** Browse student funding requests or general course tracks that require financial backing.
* **Direct Funding & Allocation:** Safely allocate funds to individual students or specific course tracks.
* **Impact Tracking:** View detailed dashboards tracking how sponsored funds are utilized and monitor the academic progress of sponsored students.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django Web Framework
* **API Architecture:** Django REST Framework (DRF)
* **API Documentation:** DRF Spectacular (OpenAPI 3 / Swagger UI)
* **Database:** PostgreSQL / MySQL
* **Authentication:** Token-based Authentication

---

## 🏁 Getting Started

### Prerequisites
* Python 3.10+
* Virtual Environment utility (`virtualenv` or built-in `venv`)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/lms_v2.git](https://github.com/your-username/lms_v2.git)
   cd lms_v2
