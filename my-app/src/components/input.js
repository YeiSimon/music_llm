"use client";
import { useState } from "react";
import { Textarea } from "flowbite-react";

export function Inputbar({ onSendMessage }) {
    const [input, setInput] = useState('');
    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault(); // Prevents the default action of the enter key
          if (input.trim()) {
            onSendMessage(input);
            setInput('');
          }
        }
      };
    return (
      <div className="flex justify-center items-center w-full">
        <div className="rounded-lg w-full max-w-3xl p-2 bg-gray-100 border-t border-gray-300 flex items-center space-x-2">
          <div className="flex-grow">
            <label htmlFor="comment" className="sr-only">Comment</label>
            <Textarea 
              id="comment" 
              placeholder="Leave a comment..." 
              required 
              rows={4} 
              className="w-full h-12 overflow-auto resize-none"
              value={input}
              onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            />
          </div>
          <button
            type="button"
            className="inline-flex items-center rounded bg-blue-500 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-lg transition duration-150 ease-in-out hover:bg-blue-600 focus:bg-blue-600 focus:outline-none active:bg-blue-700"
            onClick={() => {
                if (input.trim()) {
                  onSendMessage(input);
                  setInput('');
                }
              }}
          >
            Send
          </button>
        </div>
      </div>
    );
  }