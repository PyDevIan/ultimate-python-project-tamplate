import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-600 via-pink-500 to-red-500 text-white flex flex-col items-center justify-center p-8">
      <h1 className="text-4xl font-bold mb-4 drop-shadow-lg">
        🚀 Tailwind is Live!
      </h1>
      <p className="text-lg mb-6">
        If you see this styled page, Tailwind’s working like a charm 🔥
      </p>
      <button className="px-6 py-3 bg-white text-purple-700 rounded-lg shadow hover:bg-purple-100 transition duration-300">
        Click Me
      </button>
    </div>
  );
}

export default App;
