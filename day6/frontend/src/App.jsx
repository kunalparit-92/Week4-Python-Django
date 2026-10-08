import { useEffect, useState } from "react"

function App() {
  const [message, setMessage] = useState("Loading...")

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/tasks/")
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("Django API connection failed"))
  }, [])

  const addTask = () => {
    fetch("http://127.0.0.1:8000/api/tasks/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        task: "Learn React with Django",
        status: "pending"
      })
    })
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("POST request failed"))
  }

  return (
    <div>
      <h1>Task Tracker</h1>
      <p>{message}</p>
      <button onClick={addTask}>Add Task</button>
      <p>Task: Learn React with Django</p>
      <p>Status: Pending</p>
    </div>
  )
}

export default App