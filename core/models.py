from django.db import models


class Conversation(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()

    def __str__(self):
        return self.title


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    text = models.TextField()
    sent_at = models.DateTimeField()

    def __str__(self):
        return f"{self.conversation.title} - {self.text[:30]}"


class Thought(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='thoughts'
    )
    text = models.TextField()
    sent_at = models.DateTimeField()

    def __str__(self):
        return f"Thought on message {self.message.id}"
