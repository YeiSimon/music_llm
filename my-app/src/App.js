import './input.css';
import React from 'react';
import Chatbar from './components/chatbar';
import { Inputbar } from './components/input';
import { Headbar } from './components/headbar';
import { useState } from 'react';
function App() {
  const [isSidebarVisible, setSidebarVisible] = useState(false);
  const [messages, setMessages] = useState([]);

    const toggleSidebar = () => {
      setSidebarVisible(!isSidebarVisible);
      console.log("chatbar clicked");
    };
    const handleSendMessage = (message) => {
      const newMessages = [...messages, { sender: 'user', text: message }];
    setMessages(newMessages);

    setTimeout(() => {
      const botMessage = { sender: 'bot', text: 'This is a bot response.' };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    }, 1000);
    };

  return (
    <div className="flex h-screen">
      <div
  className={`fixed top-0 left-0 h-full z-40 transform transition-transform duration-300 ${
    isSidebarVisible ? 'translate-x-0' : '-translate-x-full'
  }`}
  style={{ width: '250px' }}
>
  <Chatbar />
</div>

      <div className="flex flex-col flex-grow transition-all duration-300"
      style={{ marginLeft: isSidebarVisible ? '250px' : '0px' }}>
        <Headbar toggleSidebar={toggleSidebar}></Headbar>
        <div className="flex-grow p-4 overflow-y-auto">
          {/* Main content area */}
          <h1 className="text-3xl font-bold">Welcome for musLLM</h1>
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`mt-2 p-2 rounded max-w-md ${
                msg.sender === 'user' ? 'ml-auto bg-gray-200 text-right' : 'mr-auto bg-blue-200 text-left'
              }`}
            >
              {msg.text}
            </div>
          ))}
        </div>
        <div className="p-4 ">
          <Inputbar onSendMessage={handleSendMessage}/>
        </div>
      </div>
    </div>
  );
}

export default App;
