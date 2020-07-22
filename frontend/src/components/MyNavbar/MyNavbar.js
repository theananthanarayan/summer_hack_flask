import React, { useState } from 'react';
import { Nav } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import { Navbar } from 'react-bootstrap';
import {Link} from 'react-router-dom';
import './MyNavbar.css';

export default function MyNavbar(props) {  
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  const logOutBtn = (
      <Link to="/logout">
          <Button className="mynavbar-btn" variant="outline-secondary" size="sm">log out</Button>
      </Link>
  )

  return (
    <div>
      <Navbar className="mynavbar" collapseOnSelect bg="light" variant="light">
        <Navbar.Brand href="/">United Pantry</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Nav className="mr-auto">
            {/* <Nav.Link className="mobile-login" href="#features">login</Nav.Link>
            <Nav.Link className="mobile-login" href="#pricing">signup</Nav.Link>
            */}
        </Nav>

        <Nav style={{display: (props.showBtn === "true") ? "" : "none"}}>
          <Link to="/login">
            <Button className="mynavbar-btn" variant="outline-secondary" size="sm">login</Button>
          </Link>
            {/* <Nav.Link eventKey={2} href="#memes">
              Dank memes
            </Nav.Link> */}
          <Link to="/signup">
            <Button className="mynavbar-btn" variant="outline-secondary" size="sm">sign up</Button>
          </Link>
          <Link to="/logout">
            <Button className="mynavbar-btn" variant="outline-secondary" size="sm">log out</Button>
          </Link>
        </Nav>
      </Navbar>
    </div>
  )
}