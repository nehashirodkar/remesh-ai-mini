# remesh.ai mini

A simplified conversation insights demo inspired by remesh.ai.
This project models structured conversations, messages, and associated thoughts, along with an efficient search experience.

---

## Demo Video

Watch the demo here: https://www.loom.com/share/66ea47628b564988b37bdf0196508248

---

## 🚀 Features

* Create and manage conversations
* Add messages within a conversation
* Attach thoughts to individual messages
* Search across:

  * Conversation titles
  * Message content
  * Thought content
* Filtered search results (displays only relevant messages instead of full conversations)
* Clean and responsive UI using Bootstrap

---

## 🧠 Data Model

* **Conversation** → contains multiple messages
* **Message** → belongs to a conversation and can have multiple thoughts
* **Thought** → linked to a specific message

---

## 🛠 Tech Stack

* **Backend:** Django
* **Database:** SQLite
* **Frontend:** HTML, Bootstrap

---

## ⚙️ How to Run Locally

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Run migrations:

   ```
   python manage.py migrate
   ```
5. Start the development server:

   ```
   python manage.py runserver
   ```
6. Open in browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## ✨ Highlights

* Designed relational data flow across multiple entities (Conversation → Message → Thought)
* Implemented multi-level search with filtering for better usability
* Focused on clean UI and structured backend logic

---

## 📌 Notes

* Built as part of a take-home assignment
* Emphasis on backend design, data relationships, and usability

