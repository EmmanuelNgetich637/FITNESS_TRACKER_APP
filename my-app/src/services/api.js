import axios from 'axios';

const api = axios.create({
    baseUrl: 'http://localhost:5000', //Flask backend URL
});

export default api;
