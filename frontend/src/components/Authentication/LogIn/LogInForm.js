import React from 'react';
import {Form} from 'shards-react';
import {FormGroup} from 'shards-react';
import {FormInput} from 'shards-react';
import {FormCheckbox} from 'shards-react';
import {Button} from 'shards-react';

import GoogleLogin from 'react-google-login';

export default function LogInForm() {
    return (
        <Form className="FormContainer">
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
                    <FormInput id="email" placeholder=""/>
                </FormGroup>

                <FormGroup className="formGroup">
                    <label htmlFor="#password">Password</label>
                    <FormInput id="password" placeholder=""/>
                </FormGroup>

                <Button className="auth-btn" theme="success">
                    Log In
                </Button>
            </div>
            
        </Form>
    )
}
