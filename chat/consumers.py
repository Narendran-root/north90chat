import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User
from channels.db import database_sync_to_async  # ✅ Import this

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.other_username = self.scope["url_route"]["kwargs"]["username"]

        if self.user.is_authenticated:
            self.room_group_name = self.get_room_name(self.user.username, self.other_username)

            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data.get("message")
        sender = self.scope["user"]

        receiver = await self.get_user(self.other_username)  # ✅ Use async method

        if receiver:
            # ✅ Save message asynchronously
            await self.save_message(sender, receiver, message_content)

            # ✅ Broadcast message
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message_content,
                    "sender": sender.username,
                    "receiver": receiver.username,
                },
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    def get_room_name(self, user1, user2):
        return f"chat_{'_'.join(sorted([user1, user2]))}"

    @database_sync_to_async  # ✅ Async wrapper for ORM call
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @database_sync_to_async  # ✅ Async wrapper for ORM call
    def save_message(self, sender, receiver, content):
        return Message.objects.create(sender=sender, receiver=receiver, content=content)
