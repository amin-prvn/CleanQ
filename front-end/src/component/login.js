import React, { useEffect, useState } from "react"
import {useHistory} from "react-router-dom"
import axios from "axios"

export const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");
    const [phone, setPhone] = useState("");
  
    const history = useHistory()

    const emailChange = (e) => {
      setEmail(e.target.value);
    };
  
    const passwordChange = (e) => {
      setPassword(e.target.value);
    };
  
    const nameChange = (e) => {
      setName(e.target.value);
    };
  
    const phoneChange = (e) => {
      setPhone(e.target.value);
    };

    const submit = () => {
        const data = {
            email:email,
            password:password,
            name:name,
            phone:phone
        }
        axios.post("http://localhost:8000/api/v1/patient", data)
        .then(res => {
            localStorage.setItem("token", res.data.token)
            history.push("/clinic")
        })
        .catch(err => {
            console.log(err)
        })
    };
    return (
        <div className="container">
            <h1>
                SignUp
            </h1>
            <div className="form" height='auto'>
                <label htmlFor="club_id">Email</label>
                <input
                    id="club_id"
                    type="email"
                    placeholder="email"
                    value={email}
                    onChange={emailChange}
                />
                <label htmlFor="club_name">Password</label>
                <input
                    id="club_name"
                    type="password"
                    placeholder="password"
                    value={password}
                    onChange={passwordChange}
                />
                <label htmlFor="club_city">Name</label>
                <input
                    id="club_city"
                    type="name"
                    placeholder="name"
                    value={name}
                    onChange={nameChange}
                />
                <label htmlFor="club_email">Phone</label>
                <input
                    id="club_email"
                    type="name"
                    placeholder="phone"
                    value={phone}
                    onChange={phoneChange}
                />
                <button onClick={submit}>Submit</button>
            </div>
        </div>

    )
}