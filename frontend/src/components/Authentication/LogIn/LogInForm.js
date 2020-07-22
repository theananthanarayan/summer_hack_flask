import React from 'react';
import {Form} from 'shards-react';
import {FormGroup} from 'shards-react';
import {FormInput} from 'shards-react';
import {FormCheckbox} from 'shards-react';
import {Button} from 'shards-react';
import {useHistory} from 'react-router-dom';

import {login} from '../../../functions/login';

import GoogleLogin from 'react-google-login';

export default function LogInForm() {
    const history = useHistory();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const postForm = () => {
        var form = {
            email: email,
            password: password
        };
        await login(form).then(response => {
            if(!response.error) {
                history.push('/');
            }
        });
    }

    return (
        <Form className="FormContainer" onSubmit={() => postForm()}>
            <div>
                <h1>Log In</h1>
            </div>
            {/* <GoogleLogin
                onClick={() => { console.log('Google button clicked') }}
                />

<div className="fb-login-button" data-width="" data-size="large" data-button-type="continue_with" data-auto-logout-link="false" data-use-continue-as="false"></div> */}
            <div>

                <FormGroup className="formGroup">
                    <label htmlFor="#email">Email</label>
                    <FormInput id="email" placeholder="" onChange={e => setEmail(e.target.value)}/>
                </FormGroup>

                <FormGroup className="formGroup">
                    <label htmlFor="#password">Password</label>
                    <FormInput id="password" placeholder="" onChange={e => setPassword(e.target.value)}/>
                </FormGroup>

                <Button className="auth-btn" theme="success">
                    Log In
                </Button>
            </div>
            
        </Form>
    )
}
