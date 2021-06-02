import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import axios from 'axios';
import './App.css';

function App() {

  const [setChart, chart] = useState(null)

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/')
      .then(res => {
        console.log(res)
        
      })
      .catch(err => {
        console.log(err)
      })
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <img src="" className="App-logo" alt="logo" />
        <p>
          Weener.
        </p>
      </header>
    </div>
  );
}

export default App;
