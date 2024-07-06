export function Headbar({ toggleSidebar }) {
    
return(
    <div className="p-4 bg-blue-500 text-white">
        <button 
            className="ml-4 p-2 bg-white text-blue-500 rounded"
            onClick={toggleSidebar}
          >Toggle Sidebar</button>
        </div>
)
}