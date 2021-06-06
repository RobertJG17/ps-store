import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import axios from "axios";
import parse from "html-react-parser";
import "./App.css";
import Player from "./components/player";
import { getCode, getCurrentPlaybackState } from "./api";

function App() {
  const [chart, setChart] = useState(null);
  const [token, setToken] = useState({});

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/")
      .then((res) => {
        setChart(res.data);
        console.log(chart);
      })
      .catch((err) => {
        console.log(err);
    });

    let search = window.location.search;
    let params = new URLSearchParams(search);

    if (params) {
      setToken({
        access_token: params.get("token"),
        refresh_token: params.get("refresh_token"),
        expires_in: params.get("expires_in"),
      });
      localStorage.setItem("token", params.get("token"));
      localStorage.setItem("refresh_token", params.get("refresh_token"));
      localStorage.setItem("expires_in", params.get("expires_in"));
    }
  }, []);

  return (
    <div className="App">
      {console.log(token)},
      <header className="App-header">
        {/* {chart ? <div className="chart">{parse(chart)}</div> : <div></div>} */}
        <h1>Weener.</h1>
        {localStorage.getItem("token") && localStorage.getItem("token") !== "null" ?
          <div>
            <button onClick={() => (localStorage.removeItem("token"), window.location.href = "http://localhost:3000/")}>Log Out</button>
            <Player/>
          </div>
          :
          <div>
            <p>Ur azz not logged in tho</p>
            <button onClick={() => getCode()}>Login</button>
          </div>
        }
      </header> 
    </div>
  );
}

export default App;
