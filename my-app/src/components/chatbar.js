"use client";
import React, { useState } from 'react';
import { Sidebar } from "flowbite-react";

const Chatbar = ({ onNewChat }) => {
  const [chats, setChats] = useState([]);

  const handleNewChat = () => {
    const newChat = { id: chats.length, content: `Chat ${chats.length + 1}` };
    setChats([...chats, newChat]);
  };
  return (
    <Sidebar aria-label="Sidebar with call to action button example">
      <Sidebar.Items>
        <Sidebar.ItemGroup>
          <Sidebar.Item href="#" onClick={handleNewChat}>
            Start with new chat
          </Sidebar.Item>
          {chats.map((chat) => (
            <Sidebar.Item key={chat.id} href="#">
              {chat.content}
            </Sidebar.Item>
          ))}
        </Sidebar.ItemGroup>
      </Sidebar.Items>
      
    </Sidebar>
  );
}
export default Chatbar;