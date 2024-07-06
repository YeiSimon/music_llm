// src/hooks/useChat.js
import { useState } from 'react';

const useChat = () => {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (message) => {
    const newMessages = [...messages, { sender: 'user', text: message }];
    setMessages(newMessages);
    try {
      // Send the message to the backend
      const response = await fetch('http://localhost:8080/sendMessages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sender: 'user', text: message }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const botMessageJson = await response.json();
      const botMessage = {
        sender: 'bot',
        text: botMessageJson.message, // Access the 'message' property from the response
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message to backend:', error);
      // Handle error appropriately, e.g., show an error message to the user
    }
  };

  return {
    messages,
    sendMessage,
  };
};

export default useChat;
