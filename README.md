# Remesh AI Mini

A simplified conversation insights application inspired by Remesh.

This project models structured conversations, messages, and associated thoughts, along with a multi-level search experience across related entities. The focus is on backend architecture, relational data modeling, and efficient querying.

---

## 🌐 Live Application

https://your-render-url.onrender.com

---

## 🎥 Demo

Watch the demo video:
https://www.loom.com/share/66ea47628b564988b37bdf0196508248

---

## 🚀 Features

* Create and manage conversations
* Add messages within a conversation
* Attach thoughts to individual messages

### 🔍 Search Capabilities

Supports search across:

* Conversation titles
* Message content
* Thought content

Search results are filtered to display only relevant messages instead of entire conversations.

---

## 🧱 Data Model

* **Conversation**

  * Fields: `title`, `start_date`
  * Relationship: One-to-many with messages

* **Message**

  * Fields: `text`, `sent_at`
  * Relationship: Belongs to a conversation, one-to-many with thoughts

* **Thought**

  * Fields: `text`, `sent_at`
  * Relationship: Belongs to a message

---

## 🛠️ Tech Stack

* Backend: Django 5.2.12
* Database:

  * SQLite (local development)
  * PostgreSQL (production on Render)
* Frontend: HTML, Bootstrap

---

## ⚙️ Requirements

* Python 3.10 or higher
* pip

---

## 🔧 Environment Setup

Create a `.env` file in the project root (same level as `manage.py`) with the following:

```
DEBUG=True
SECRET_KEY=django-insecure-local-key
ALLOWED_HOSTS=127.0.0.1,localhost
```

If you are not using a `.env` file, ensure these values are set in your environment.

---

## 💻 Local Setup

1. **Clone the repository**

```
git clone https://github.com/nehashirodkar/remesh-ai-mini.git
cd remesh-ai-mini
```

2. **Create and activate a virtual environment**

**Windows:**

```
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Apply database migrations**

```
python manage.py migrate
```

5. **Run the development server**

```
python manage.py runserver
```

6. **Open in browser**

```
http://127.0.0.1:8000/
```

---

## 🗄️ Database Note

* Local development uses **SQLite**
* Production (Render) uses **PostgreSQL**

When running locally, a new SQLite database will be created.
Data from the deployed application will not be available locally.

---

## 🧪 Running Tests

The project includes a test suite covering:

* Model creation
* Relationships
* View behavior
* Search functionality

Run tests using:

```
python manage.py test
```

---

## ✨ Highlights

* Structured relational data modeling across multiple entities
* Multi-level search implemented using Django ORM with related field filtering
* Query optimization using `prefetch_related`
* Backend test coverage for core functionality and filtering logic
* Designed with deployment compatibility (local + production environments)

---

## 🤖 AI Usage

AI tools were used to assist with:

* Designing Django models and relationships
* Implementing search functionality across related models
* Writing and refining test cases
* Improving documentation

All outputs were reviewed, modified, and validated locally.

---

## ⚠️ Troubleshooting

If you encounter issues while running locally:

* Ensure virtual environment is activated
* Run `pip install -r requirements.txt` again
* Run `python manage.py migrate` before starting server

### Common Errors

* `ModuleNotFoundError` → reinstall dependencies
* `DisallowedHost` → ensure `ALLOWED_HOSTS` includes localhost
* `ImproperlyConfigured` → check `.env` file

---

## 📝 Notes

* Built as part of a take-home assignment
* Focused on backend architecture, data relationships, and functionality
* UI kept minimal as it was not part of evaluation criteria

