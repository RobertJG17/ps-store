import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import axios from 'axios';
import parse from 'html-react-parser'
import './App.css';
import { getCode } from './api';

function App() {

  const [chart, setChart] = useState(null)

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/')
      .then(res => {
        setChart(res.data)
        console.log(chart)
      })
      .catch(err => {
        console.log(err)
      })
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        {chart ?
          <div className="chart">
            {parse(chart)}
          </div>
          :
          <div></div>
        }
        <p>
          Weener.
        </p>
        <button onClick={() => getCode()}>Get code</button>
      </header>
    </div>
  );
}

export default App;




