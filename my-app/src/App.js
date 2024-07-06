import './input.css';
import React, { useState } from 'react';
import Chatbar from './components/chatbar';
import { Inputbar } from './components/input';
import { Headbar } from './components/headbar';
import { Content } from './components/content';
import useChat from './hooks/useChat';
function App() {
  const [isSidebarVisible, setSidebarVisible] = useState(false);
  const { messages, sendMessage } = useChat();

  const toggleSidebar = () => {
    setSidebarVisible(!isSidebarVisible);
  };

  return (
    <div className="flex h-screen">
      <div className={`fixed top-0 left-0 h-full z-40 transform transition-transform duration-300 
          ${isSidebarVisible ? 'translate-x-0' : '-translate-x-full'}`}
        style={{ width: '250px' }}
      >
        <Chatbar />
      </div>
      <div className="flex flex-col flex-grow transition-all duration-300"
        style={{ marginLeft: isSidebarVisible ? '250px' : '0px' }}>
        <Headbar toggleSidebar={toggleSidebar}></Headbar>
        <Content messages={messages} />
        <div className="p-4 ">
          <Inputbar onSendMessage={sendMessage} />
        </div>
      </div>
    </div>
  );
}

export default App;
