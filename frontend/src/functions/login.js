import axios from 'axios';

export const login = user => {
    return axios.post("http://127.0.0.1:5000/auth/login", {
        email: user.email,
        password: user.password
    })
    .then(response => {
        localStorage.setItem('usertoken', response.data.usertoken)
    }).catch(error => {
        console.log(error);
    })
}