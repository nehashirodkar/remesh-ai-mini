remesh.ai mini- A simplified conversation insights demo inspired by remesh.ai.







🚀 Features



1\. Create and manage Conversations

2\. Add Messages within a Conversation

3\. Add Thoughts linked to specific Messages

4\. Search functionality across:
	- Conversation titles
	- Message content
	- Thought content

5\. Filtered search results (only relevant messages shown instead of full conversation)

6\. Clean and responsive UI using Bootstrap







🧠 Data Model



1\. Conversation → contains multiple Messages

2\. Message → belongs to a Conversation and can have multiple Thoughts

3\. Thought → linked to a specific Message







🛠 Tech Stack



1\. Django (Backend)

2\. SQLite (Database)

3\. HTML + Bootstrap (Frontend)







⚙️ How to Run Locally



1\. Clone the repository

2\. Create a virtual environment

3\. Install dependencies:
	pip install -r requirements.txt



4\. Run migrations:

&#x20;  	python manage.py migrate

&#x20; 

5\. Start the development server:

&#x20;  	python manage.py runserver



6\. Open in browser:

&#x20;  	http://127.0.0.1:8000/

