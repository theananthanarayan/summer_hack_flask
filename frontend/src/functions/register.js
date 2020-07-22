import axios from 'axios';

export const register = user => {
    console.log(user);
    return axios.post("http://127.0.0.1:5000/auth/register", {
        username: user.username,
        password: user.password,
        firstname: user.firstname,
        lastname: user.lastname,
        email: user.email,
        phone: user.phone,
        location: 12.2,

    })
    .then(response => {
        console.log(response);
    }).catch(error => {
        console.log(error);
    })
}