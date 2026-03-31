# Remesh AI Mini

A simplified conversation insights demo inspired by Remesh.

This application models structured conversations, messages, and associated thoughts, along with a multi-level search experience across related entities.

---

## Demo

Watch the demo video:  
https://www.loom.com/share/66ea47628b564988b37bdf0196508248

---

## Features

- Create and manage conversations  
- Add messages within a conversation  
- Attach thoughts to individual messages  

### Search Capabilities

Supports search across:
- Conversation titles  
- Message content  
- Thought content  

Search results are filtered to display only relevant messages instead of entire conversations.

---

## Data Model

- Conversation  
  - Fields: title, start_date  
  - Relationship: One-to-many with messages  

- Message  
  - Fields: text, sent_at  
  - Relationship: Belongs to a conversation, one-to-many with thoughts  

- Thought  
  - Fields: text, sent_at  
  - Relationship: Belongs to a message  

---

## Tech Stack

- Backend: Django 5.2.12  
- Database: SQLite  
- Frontend: HTML, Bootstrap  

---

## Requirements

- Python 3.10 or higher  
- Django 5.2.12  

---

## Local Setup

1. Clone the repository

git clone https://github.com/nehashirodkar/remesh-ai-mini.git  
cd remesh-ai-mini  

2. Create and activate a virtual environment

Windows:

python -m venv venv  
venv\Scripts\activate  

macOS / Linux:

python -m venv venv  
source venv/bin/activate  

3. Install dependencies

pip install -r requirements.txt  

4. Apply database migrations

python manage.py migrate  

5. Run the development server

python manage.py runserver  

6. Open in browser

http://127.0.0.1:8000/

---

## Running Tests

The project includes a test suite covering:

- Model creation  
- Relationships  
- View behavior  
- Search functionality  

Run tests using:

python manage.py test  

---

## Highlights

- Structured relational data modeling across multiple entities  
- Multi-level search implemented using Django ORM with related field filtering  
- Query optimization using prefetch_related  
- Backend test coverage for core functionality and filtering logic  
- Dependency compatibility fixes to ensure smooth local setup  

---

## AI Usage

AI tools were used to assist with:

- Designing Django models and relationships  
- Implementing search functionality across related models  
- Writing and refining test cases  
- Improving documentation and README clarity  

Example prompts:

- Design Django models for conversations, messages, and thoughts  
- Implement search across related Django models  
- Write test cases for Django views and models  
- Improve README structure and clarity  

Challenges:

- Ensuring dependency compatibility (Django vs Python version)  
- Aligning test cases with actual model constraints  
- Implementing correct filtering across related entities  

All AI-assisted outputs were reviewed, modified, and validated locally.

---

## Notes

- Built as part of a take-home assignment  
- Focused on backend architecture, data relationships, and functionality  
- UI design kept minimal as it was not part of evaluation criteria  

