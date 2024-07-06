import React, { useEffect, useRef } from 'react';

export function Content({messages}) {
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);
    return (
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
          <div ref={messagesEndRef} />
        </div>
    )
}