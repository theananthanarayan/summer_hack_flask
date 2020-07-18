import axios from 'axios';

export const login = user => {
    return axios.post("auth/login", {
        email: user.email,
        password: user.password
    })
    .then(response => {
        localStorage.setItem('usertoken', response.data.usertoken)
    }).catch(error => {
        console.log(error);
    })
}