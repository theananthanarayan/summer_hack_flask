import React from 'react';
import {useState} from 'react';
import {Form} from 'shards-react';
import {FormGroup} from 'shards-react';
import {FormInput} from 'shards-react';
import {FormCheckbox} from 'shards-react';
import {Button} from 'shards-react';
import {useHistory} from 'react-router-dom';

import GoogleLogin from 'react-google-login';

import {register} from '../../../functions/register'

import '../FormContainer.css';
import './SignUpForm.css';

export default function SignUpForm() {
    const history = useHistory();

    const [termsAgreement, setTermsAgreement] = useState(false);
    const toggleTermsAgreement =()=> setTermsAgreement(!termsAgreement);

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [phone, setPhone] = useState("");
    const [password, setPassword] = useState("");

    const postForm = async () => {
        var form = {
            username: username,
            email: email,
            firstname: firstname,
            lastname: lastname,
            phone: phone,
            password: password
        };
        await register(form).then(response => {
            if(!response.error) {
                history.push('/');
            }
        });
    }
    return (
        <Form className="FormContainer" onSubmit={() => {postForm();}}>
            <div>
                <h1>Sign Up</h1>
            </div>

            <div>

                <div className="flex-container">
                    <FormGroup className="formGroup">
                        <label htmlFor="#firstname">First Name</label>
                        <FormInput type="text" id="firstname" placeholder="" onChange={e => setFirstname(e.target.value)}/>
                    </FormGroup>
                    <FormGroup className="formGroup">
                        <label htmlFor="#lastname">Last Name</label>
                        <FormInput type="text" id="lastname" placeholder="" onChange={e => setLastname(e.target.value)}/>
                    </FormGroup>
                </div>
                
                <FormGroup className="formGroup">
                    <label htmlFor="#username">Username</label>
                    <FormInput type="text" id="username" placeholder="" onChange={e => setUsername(e.target.value)}/>
                </FormGroup>

                <FormGroup className="formGroup">
                    <label htmlFor="#email">Email</label>
                    <FormInput type="email" id="email" placeholder="" onChange={e => setEmail(e.target.value)}/>
                </FormGroup>

                <FormGroup className="formGroup">
                    <label htmlFor="#phone">Phone Number</label>
                    <FormInput type="tel" id="phone" placeholder="" onChange={e => setPhone(e.target.value)}/>
                </FormGroup>

                <FormGroup className="formGroup">
                    <label htmlFor="#password">Password</label>
                    <FormInput type="password" id="password" placeholder="" onChange={e => {setPassword(e.target.value)}}/>
                </FormGroup>

                <FormCheckbox className="formGroup" checked={termsAgreement} onChange={toggleTermsAgreement}>
                    I have read and agree to the Terms and Conditions and Privacy Policy
                </FormCheckbox>

                <Button className="auth-btn" theme="success" type="submit">
                    Sign Up
                </Button>
            </div>
            
        </Form>
    )
}
