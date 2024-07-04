import {React, useContext} from 'react'
import {Link} from 'react-router-dom'
import { AuthCon } from '../context/AuthContext'
import '../App.css'

const Navbar = () => {
  const {logout} = useContext(AuthCon)
  return (
    <div class="sidenav">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/services">Services</Link>
        <Link to="/restaurant">Restaurant</Link>
        <Link to="/menu">Menu</Link>
        <Link to="/menuitem">Menuitem</Link>
        <Link to="/order">Order</Link>
        <Link to="/payment">Payment</Link>
        <Link to="/review">Review</Link>
        <Link to="/promotion">Promotion</Link>
        <Link to="/delivery">Delivery</Link>

        <Link to="/contact">Contact</Link>
        {
            localStorage.getItem('token') ? <Link onClick={logout}>Logout</Link> : <Link to="/login">Login</Link>
        }

      <div class="main">
          {/* <h2>Side Navbar Example</h2>
          <p>This is an example of a side navigation bar.</p> */}
      </div>
  </div>
  )
}

export default Navbar