import unittest
import requests
import json
from bson import ObjectId

class BackendTestCase(unittest.TestCase):
    BASE_URL = "http://localhost:8080"  # 修改为你的Go服务的实际地址

    def setUp(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    def test_create_user(self):
        url = f"{self.BASE_URL}/users"
        payload = {
            "googleId": "testGoogleID",
            "email": "test@example.com",
            "name": "Test User",
            "avatarUrl": "http://example.com/avatar.jpg"
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.user_id = data["id"]

    def test_get_user(self):
        self.test_create_user()  # Ensure user is created first
        url = f"{self.BASE_URL}/users/{self.user_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["email"], "test@example.com")
        self.assertEqual(data["name"], "Test User")

    def test_create_conversation(self):
        self.test_create_user()  # Ensure user is created first
        url = f"{self.BASE_URL}/conversations"
        payload = {
            "userId": self.user_id,
            "status": "active"
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.conversation_id = data["id"]

    def test_get_conversation(self):
        self.test_create_conversation()  # Ensure conversation is created first
        url = f"{self.BASE_URL}/conversations/{self.conversation_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["userId"], self.user_id)
        self.assertEqual(data["status"], "active")

    def test_create_message(self):
        self.test_create_conversation()  # Ensure conversation is created first
        url = f"{self.BASE_URL}/messages"
        payload = {
            "conversationId": self.conversation_id,
            "sender": "user",
            "content": "Hello, this is a test message."
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.message_id = data["id"]

    def test_get_message(self):
        self.test_create_message()  # Ensure message is created first
        url = f"{self.BASE_URL}/messages/{self.message_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["conversationId"], self.conversation_id)
        self.assertEqual(data["sender"], "user")
        self.assertEqual(data["content"], "Hello, this is a test message.")

if __name__ == '__main__':
    unittest.main()
