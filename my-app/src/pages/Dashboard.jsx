import React, { useState, useEffect } from 'react';
import UserSelector from '../components/UserSelector';
import WorkoutForm from '../components/WorkoutForm';
import WorkoutList from '../components/WorkoutList';
import api from '../services/api';

export default function Dashboard() {
    const [selectedUser, setSelectedUser] = useState('');
    const [workouts, setWorkouts] = useState([]);

    useEffect(() => {
        if (!selectedUser) {
            setWorkouts([]);
            return;
        }

        api.get(`/workouts/${selectedUser}`)
            .then(res => setWorkouts(res.data))
            .catch(console.error);
    }, [selectedUser]);

    const addWorkout = (newWorkout) => {
        setWorkouts(prev => [...prev, newWorkout]); // Fixed typo: netWorkout ➝ newWorkout
    };

    return (
        <div>
            <h1>Dashboard</h1>
            <UserSelector onSelectUser={setSelectedUser} />
            <WorkoutForm userId={selectedUser} onWorkoutAdded={addWorkout} />
            <WorkoutList workouts={workouts} />
        </div>
    );
}
