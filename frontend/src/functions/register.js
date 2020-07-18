import axios from 'axios';

export const register = user => {
    return axios.post("auth/register", {
        username: user.username,
        password: user.password,
        firstname: user.firstname,
        lastname: user.lastname,
        item: user.item,
        explanation: user.explanation,
        radius: user.radius
    })
    .then(response => {
        console.log(response);
    }).catch(error => {
        console.log(error);
    })
}