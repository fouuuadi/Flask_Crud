import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './components/pages/Home/Home';
import About from './components/pages/About/About';
import NotFound from './components/pages/Error/NotFound';

const App = () => {
  return (
    <div>
      <nav className="bg-gray-800 p-4">
        <ul className="flex space-x-4 justify-center">
          <li>
            <Link to="/" className="text-white">Home</Link>
          </li>
          <li>
            <Link to="/about" className="text-white">About</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/*" element={<NotFound />} />
      </Routes>
    </div>
  );
};

export default App;
