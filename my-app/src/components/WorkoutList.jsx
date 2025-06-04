import React from 'react';

export default function WorkoutList({ workouts }) {
  if (!workouts.length) return <p>No workouts yet.</p>;

  return (
    <ul>
      {workouts.map(w => (
        <li key={w.id}>
          {w.activity} - {w.duration} min - {new Date(w.date).toLocaleDateString()}
        </li>
      ))}
    </ul>
  );
}
