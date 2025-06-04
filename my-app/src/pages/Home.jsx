import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div>
      <h1>Welcome to Fitness Tracker</h1>
      <Link to="/dashboard">Go to Dashboard</Link>
    </div>
  );
}
