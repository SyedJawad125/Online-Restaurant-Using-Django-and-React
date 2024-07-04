import {React, useState, useContext} from 'react'
import { useNavigate, useLocation  } from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { AuthCon } from '../context/AuthContext';
import '../App.css'

const Login = () => {
    const location = useLocation()
    const navigate = useNavigate()
    const { login } = useContext(AuthCon);
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [flag, setFlag] = useState(false)

    // ReactToastify
    if (location.state && location.state.message){
      toast.success(location.state.message)
      navigate('/login', {state: ''})
    }
    else if (flag == true){
      toast.success('Not Registered')
      setFlag(false)
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
          const payload = {"username":username, "password":password}
          const response = await axiosInstance.post('/user/login', payload , {
            headers: {
              'Content-Type': 'application/json'
            }
          });
          if (response.status===200){
            login(response.data.data.token)
            navigate('/', {state: {message: 'Logged In!'}})
          }
        } catch (error) {
            // toast.error("invalid Username or Password")
            console.error('Error:', error);
        }
      };

    const Signupfunction = () => {
        navigate('/SignUp' )
    }

  return (
    <div class="container" style={{ marginLeft: '200px' }}>
    <div class="row justify-content-center">
        <div class="col-md-5">
            <div class="card mt-5">
                <div class="card-header">
                    <h3 class="text-center">Login</h3>
                </div>
                <div class="card-body" >
                    <form onSubmit={handleSubmit}>
                        <div class="mb-3">
                            <label for="username" class="form-label">User Name</label>
                            <input type="text" class="form-control" id="username" aria-describedby="emailHelp" required value={username}
                              onChange= {e => setUsername(e.target.value)}/>
                            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" class="form-control" id="password" required  value={password}
                              onChange= {e => setPassword(e.target.value)} />
                        </div>
                        {/* <div class="mb-3 form-check">
                            <input type="checkbox" class="form-check-input" id="rememberMe" />
                            <label class="form-check-label" for="rememberMe">Remember me</label>
                        </div> */}
                        <button type="submit" class="btn btn-primary w-100">Login</button>
                        <div class="call-to-action">
                        {/* <button  type="submit" class="btn btn-danger w-20 mt-4 marginLeft: 80px"onClick={()=> updateRecord()} >SignUp</button> */}
                        <button  type="submit" class="right-button" onClick={Signupfunction} >SignUp</button>
                        </div>
                    </form>
                </div>
                <div class="card-footer text-center">
                    <small>&copy; 2024 HRMS</small>
                </div>
            </div>
        </div>
    </div>
    <ToastContainer/>
</div>
  )
}

export default Login