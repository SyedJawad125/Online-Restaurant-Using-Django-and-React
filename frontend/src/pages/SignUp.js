import {React,useState} from 'react'
import { useNavigate } from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance'
import '../App.css'

const SignUp = () => {
    

    const navigate = useNavigate()
    const [first_name, setfirst_name] = useState('')
    const [last_name, setlast_name] = useState('')
    const [username, setusername] = useState('')
    const [email, setemail] = useState('')
    const [phone, setphone] = useState('')
    const [password, setpassword] = useState('')

    const [name, setName] = useState('')

  console.log('name', name)


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {

      const payload = {"first_name":first_name , "last_name":last_name, "username":username , "email":email , "phone":phone, "password":password}
      const response = await axiosInstance.post('/user/register', payload );
      
      if (response){
        console.log('Response:', response.data);
      // toast.success("You Have Registered");

      navigate('/login', {state: {message: 'You Have Registered'}})
    //   setName('')
      }
      // Handle success
    } catch (error) {
      console.error('Error:', error);
      // Handle error
    }
  };

  return (
    <div class="px-4 py-5 px-md-3 text-center text-lg-start" style={{backgroundColor: "hsl(0, 0%, 96%)" }}>
    <div class="container" style={{ marginLeft: '200px' }}>
      <div class="row gx-lg-5 align-items-center" onSubmit={handleSubmit}>
        <div class="col-lg-6 mb-5 mb-lg-0 " >
          <h3 class="my-7 display-5 fw-bold ls-tight" style={{ margin: '40px' }}>
            The HRM System <br />
            <span class="text-primary">offer Best Performance </span>
          </h3>
          <p style={{ margin: '50px' }}>
          A Human Resource Management System (HRMS) is a comprehensive software 
          suite designed to streamline and automate various HR processes within 
          an organization. It encompasses functionalities like recruitment, onboarding,
          payroll, performance management, employee attendance, benefits administration,
          and compliance with labor laws. 
          </p>
        </div>

        <div class="col-lg-6 mb-5 mb-lg-0" >
          <div class="card" style={{ marginRight: "150px"}} >
            <div class="card-body py-4 px-md-5">
              <form>
                <div class="row">
                  <div class="col-md-6 mb-4">
                    <div data-mdb-input-init class="form-outline">
                      <input type="text" id="form3Example1" class="form-control" value={first_name}
                                     onChange= {e => setfirst_name(e.target.value)} />
                      <label class="form-label" for="form3Example1">First name</label>
                    </div>
                  </div>
                  <div class="col-md-6 mb-4">
                    <div data-mdb-input-init class="form-outline">
                      <input type="text" id="form3Example2" class="form-control" value={last_name}
                                    onChange= {e => setlast_name(e.target.value)}  />
                      <label class="form-label" for="form3Example2">Last name</label>
                    </div>
                  </div>
                </div>
                <div data-mdb-input-init class="form-outline mb-4">
                  <input type="name" id="form3Example3" class="form-control" value={username}
                                    onChange= {e => setusername(e.target.value)} />
                  <label class="form-label" for="form3Example3">User Name</label>
                </div>
                <div data-mdb-input-init class="form-outline mb-4">
                  <input type="email" id="form3Example3" class="form-control" value={email}
                                    onChange= {e => setemail(e.target.value)} />
                  <label class="form-label" for="form3Example3">Email address</label>
                </div>
                <div data-mdb-input-init class="form-outline mb-4">
                  <input type="text" id="form3Example3" class="form-control" value={phone}
                                    onChange= {e => setphone(e.target.value)} />
                  <label class="form-label" for="form3Example3">Phone Number</label>
                </div>
                <div data-mdb-input-init class="form-outline mb-4">
                  <input type="password" id="form3Example4" class="form-control" value={password}
                                    onChange= {e => setpassword(e.target.value)} />
                  <label class="form-label" for="form3Example4">Password</label>
                </div>


                <button type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4">
                  Sign up
                </button>

              
                {/* <div class="text-center">
                  <p>or sign up with:</p>
                  <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-facebook-f"></i>
                  </button>

                  <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-google"></i>
                  </button>

                  <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-twitter"></i>
                  </button>

                  <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-github"></i>
                  </button>
                </div> */}
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  )
}

export default SignUp