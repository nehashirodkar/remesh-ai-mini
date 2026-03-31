from datetime import date, datetime
from django.test import TestCase
from django.urls import reverse
from .models import Conversation, Message, Thought


class ConversationModelTest(TestCase):
    def test_create_conversation(self):
        conversation = Conversation.objects.create(
            title="Test Conversation",
            start_date=date.today()
        )
        self.assertEqual(conversation.title, "Test Conversation")
        self.assertEqual(conversation.start_date, date.today())


class MessageModelTest(TestCase):
    def setUp(self):
        self.conversation = Conversation.objects.create(
            title="Test Conversation",
            start_date=date.today()
        )

    def test_create_message(self):
        message = Message.objects.create(
            conversation=self.conversation,
            text="Hello world",
            sent_at=datetime.now()
        )
        self.assertEqual(message.text, "Hello world")
        self.assertEqual(message.conversation, self.conversation)


class ThoughtModelTest(TestCase):
    def setUp(self):
        self.conversation = Conversation.objects.create(
            title="Test Conversation",
            start_date=date.today()
        )
        self.message = Message.objects.create(
            conversation=self.conversation,
            text="Hello world",
            sent_at=datetime.now()
        )

    def test_create_thought(self):
        thought = Thought.objects.create(
            message=self.message,
            text="This is a thought",
            sent_at=datetime.now()
        )
        self.assertEqual(thought.text, "This is a thought")
        self.assertEqual(thought.message, self.message)


class RelationshipTests(TestCase):
    def setUp(self):
        self.conversation = Conversation.objects.create(
            title="Relationship Test Conversation",
            start_date=date.today()
        )
        self.message = Message.objects.create(
            conversation=self.conversation,
            text="Relationship test message",
            sent_at=datetime.now()
        )

    def test_conversation_has_messages(self):
        Message.objects.create(
            conversation=self.conversation,
            text="Second message",
            sent_at=datetime.now()
        )
        self.assertEqual(self.conversation.messages.count(), 2)

    def test_message_has_thoughts(self):
        Thought.objects.create(
            message=self.message,
            text="First thought",
            sent_at=datetime.now()
        )
        Thought.objects.create(
            message=self.message,
            text="Second thought",
            sent_at=datetime.now()
        )
        self.assertEqual(self.message.thoughts.count(), 2)


class ViewTests(TestCase):
    def setUp(self):
        self.conversation = Conversation.objects.create(
            title="Project Alpha",
            start_date=date.today()
        )
        self.message1 = Message.objects.create(
            conversation=self.conversation,
            text="First message content",
            sent_at=datetime.now()
        )
        self.message2 = Message.objects.create(
            conversation=self.conversation,
            text="Second message content",
            sent_at=datetime.now()
        )
        self.thought1 = Thought.objects.create(
            message=self.message1,
            text="Interesting first thought",
            sent_at=datetime.now()
        )
        self.thought2 = Thought.objects.create(
            message=self.message2,
            text="Another second thought",
            sent_at=datetime.now()
        )

    def test_conversation_list_view_loads(self):
        response = self.client.get(reverse("conversation_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Alpha")

    def test_conversation_search_by_title(self):
        response = self.client.get(reverse("conversation_list"), {"q": "Alpha"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Alpha")

    def test_conversation_search_by_message_text(self):
        response = self.client.get(reverse("conversation_list"), {"q": "First"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Alpha")

    def test_conversation_search_by_thought_text(self):
        response = self.client.get(reverse("conversation_list"), {"q": "Interesting"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Alpha")

    def test_conversation_detail_view_loads(self):
        response = self.client.get(
            reverse("conversation_detail", args=[self.conversation.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First message content")
        self.assertContains(response, "Second message content")

    def test_conversation_detail_filtered_by_message_query(self):
        response = self.client.get(
            reverse("conversation_detail", args=[self.conversation.id]),
            {"message_q": "First"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First message content")
        self.assertNotContains(response, "Second message content")

    def test_conversation_detail_filtered_by_thought_query(self):
        response = self.client.get(
            reverse("conversation_detail", args=[self.conversation.id]),
            {"message_q": "Interesting"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First message content")
        self.assertNotContains(response, "Second message content")
