import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Leaderboard endpoint:', API_URL);
        console.log('Fetched leaderboard:', results);
      });
  }, []);

  return (
    <div className="card shadow p-4">
      <h2 className="mb-4">Leaderboard</h2>
      <table className="table table-striped table-hover">
        <thead className="table-primary">
          <tr>
            <th>Team</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map((l, i) => (
            <tr key={i}>
              <td>{l.team}</td>
              <td>{l.points}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
