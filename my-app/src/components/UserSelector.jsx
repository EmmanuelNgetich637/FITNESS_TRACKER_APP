import React, { useEffect, useState } from 'react';
import api from '../services/api';

const UserSelector = ({ onSelectUser }) => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    api.get('/users')
      .then(res => setUsers(res.data))
      .catch(err => console.error("Failed to fetch users:", err));
  }, []);

  return (
    <select onChange={e => onSelectUser(e.target.value)}>
      <option value="">Select User</option>
      {users.map(user => (
        <option key={user.id} value={user.id}>{user.username}</option>
      ))}
    </select>
  );
};

export default UserSelector;
