import React, { useState } from 'react';
import api from '../services/api';

export default function WorkoutForm({ userId, onWorkoutAdded }) {
  const [activity, setActivity] = useState('');
  const [duration, setDuration] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userId) return alert('Select a user first');

    try {
      const res = await api.post(`/workouts/${userId}`, {
        activity,
        duration: parseInt(duration, 10),
      });
      setActivity('');
      setDuration('');
      onWorkoutAdded(res.data);
    } catch (err) {
      alert('Failed to add workout');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Activity"
        value={activity}
        onChange={e => setActivity(e.target.value)}
        required
      />
      <input
        type="number"
        placeholder="Duration (min)"
        value={duration}
        onChange={e => setDuration(e.target.value)}
        required
        min="1"
      />
      <button type="submit">Add Workout</button>
    </form>
  );
}
