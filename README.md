\# remesh.ai mini



A simplified conversation insights demo inspired by remesh.ai.



\---



\## 🚀 Features



\* Create and manage Conversations

\* Add Messages within a Conversation

\* Add Thoughts linked to specific Messages

\* Search functionality across:



&#x20; \* Conversation titles

&#x20; \* Message content

&#x20; \* Thought content

\* Filtered search results (only relevant messages shown instead of full conversation)

\* Clean and responsive UI using Bootstrap



\---



\## 🧠 Data Model



\* \*\*Conversation\*\* → contains multiple Messages

\* \*\*Message\*\* → belongs to a Conversation and can have multiple Thoughts

\* \*\*Thought\*\* → linked to a specific Message



\---



\## 🛠 Tech Stack



\* Django (Backend)

\* SQLite (Database)

\* HTML + Bootstrap (Frontend)



\---



\## ⚙️ How to Run Locally



1\. Clone the repository

2\. Create a virtual environment

3\. Install dependencies:



&#x20;  ```

&#x20;  pip install -r requirements.txt

&#x20;  ```

4\. Run migrations:



&#x20;  ```

&#x20;  python manage.py migrate

&#x20;  ```

5\. Start the development server:



&#x20;  ```

&#x20;  python manage.py runserver

&#x20;  ```

6\. Open in browser:



&#x20;  ```

&#x20;  http://127.0.0.1:8000/

&#x20;  ```



\---



\## 📌 Notes



\* This is a demo project built as part of a take-home assignment

\* Focused on backend relationships, structured data flow, and search functionality

\* UI is designed to be simple, clean, and user-friendly



