import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Activities endpoint:', API_URL);
        console.log('Fetched activities:', results);
      });
  }, []);

  return (
    <div className="card shadow p-4">
      <h2 className="mb-4">Activities</h2>
      <table className="table table-striped table-hover">
        <thead className="table-primary">
          <tr>
            <th>Type</th>
            <th>User Email</th>
            <th>Duration (min)</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((a, i) => (
            <tr key={i}>
              <td>{a.type}</td>
              <td>{a.user_email}</td>
              <td>{a.duration}</td>
              <td>{a.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
