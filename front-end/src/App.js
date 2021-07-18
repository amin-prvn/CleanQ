import React, { useEffect, useState } from "react"
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom"
import { Table } from "./component/table"
import { Login } from "./component/login"
import './App.css';

function App() {
  const [token, setToken] = useState(null)
  useEffect(
    () => {
      setToken(localStorage.getItem("token"))
    }, []
  )
  return (
    <Router>
      <header>
        <a href="http://localhost:8000/admin">Admin Panel</a>
        <a href="https://github.com/amin-prvn/CleanQ">About Us</a>
      </header>
      <Switch>
        <Route path="/" exact>
          {token !== null ? <Redirect to="/clinic" /> : <Login />}
        </Route>
        <Route path="/clinic" exact>
          <Table />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
