import React, { useEffect, useState } from "react"
import axios from "axios"

export const Table = () => {
    const [data, setData] = useState([{}])
    useEffect(() => {
        axios.get("http://localhost:8000/api/v1/get-clinics")
            .then(res => {
                console.log(res.data)
                setData(res.data)
            })
            .catch(
                err => {
                    console.log(err)
                }
            )

    }, [])
    const reserve = (id) => {
        const data = {
            clinic:id,
            description:"description"
        }
        const header = {
            'Authorization':localStorage.getItem("token"),
            'Content-Type': 'application/json'
        }
        axios.post("http://127.0.0.1:8000/api/v1/reserve", data, {headers:header})
        .then(
            res => {
                alert(`Clinic Reserved for ${res.data.time}`)
            }
        )
    }
    return (
        <div className="container">
            <h1>
                CleanQ
            </h1>
            <div className="row">
                {data.map(
                    row => {
                        return (
                            <div>
                                {Object.keys(row).map(
                                    rowData => {
                                        return (
                                            <p>
                                                {row[rowData]}
                                            </p>
                                        )
                                    }
                                )}
                                <button onClick={() => reserve(row.id)}>
                                    Reserve
                                </button>
                            </div>
                        )
                    }
                )}
            </div>
        </div>
    )
}
