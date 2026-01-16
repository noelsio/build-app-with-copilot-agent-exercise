import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Workouts endpoint:', API_URL);
        console.log('Fetched workouts:', results);
      });
  }, []);

  return (
    <div className="card shadow p-4">
      <h2 className="mb-4">Workouts</h2>
      <table className="table table-striped table-hover">
        <thead className="table-primary">
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Difficulty</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((w, i) => (
            <tr key={i}>
              <td>{w.name}</td>
              <td>{w.description}</td>
              <td>{w.difficulty}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;
