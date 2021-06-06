import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import axios from "axios";
import parse from "html-react-parser";
import "./App.css";
import { getCode } from "./api";

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
    }
  }, []);

  return (
    <div className="App">
      {console.log(token)},
      <header className="App-header">
        {chart ? <div className="chart">{parse(chart)}</div> : <div></div>}
        <p>Weener.</p>
        <button onClick={() => getCode()}>Get code</button>
        {token["access_token"] ?
          <p>Your azz logged in tho</p>
          :
          <p>Ur azz not logged in tho</p>
        }
      </header>
    </div>
  );
}

export default App;
