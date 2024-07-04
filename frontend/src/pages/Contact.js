import {React,useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance'

const Contact = () => {


  const navigate = useNavigate()

  const [name, setname] = useState('')
  const [country, setcountry] = useState('')
  const [phone_number, setphone_number] = useState('')
  const [email, setemail] = useState('')
  const [subject, setsubject] = useState('')
  const [restaurant, setrestaurant] = useState('')

  const [restaurantRecords, setrestaurantRecords] = useState([])


  useEffect(()=>{
    // For dropdown list
    const fetchrestaurant = async () =>{
      const res = await axiosInstance.get('/restaurent/restaurant') 
      try{
          if (res){
            setrestaurantRecords(res.data.data.data)
          }
      }
      catch (error){
          console.log('error occured', error)
      }
  }
  fetchrestaurant();
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {

        const payload = {"name":name , "country":country,"phone_number":phone_number, 
          "email":email, "subject":subject, "restaurant":restaurant}
        
        const response = await axiosInstance.post('/restaurent/contact', payload , {
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (response){
        console.log('Response:', response.data);
        navigate('/contact', {state: {message: 'contact Added!'}})
        }
        // Handle success
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
    };
  return (
    <div class='container' style={{ marginLeft: '200px' }}  >
        <h2 class='mt-3'>Contact Us</h2>
        <form action="action_page.php"  onSubmit={handleSubmit}>

          <label for="name" class='mt-3'>Name</label>
          <input type="text" id="name" name="name" placeholder="Your name.." value={name}
            onChange= {e => setname(e.target.value)} />

          <label for="country">Country</label>
          <input type="text" id="country" name="country" placeholder="Your country name.."  value={country}
            onChange= {e => setcountry(e.target.value)} />

          <label for="phone_number">Phone Number</label>
          <input type="text" id="phone_number" name="phone_number" placeholder="Your phone number.."  value={phone_number}
            onChange= {e => setphone_number(e.target.value)}/>

          <label for="email">Email</label>
          <input type="text" id="email" name="email" placeholder="Your email.." value={email}
            onChange= {e => setemail(e.target.value)} />

          <select class="form-select" aria-label="Default select example" onChange={e => setrestaurant(e.target.value)}>
            <option selected>Select Restaurant</option>

              { restaurantRecords ?
                restaurantRecords.map(item => (
                  <option value={item.id} key={item.id}>{item.name}</option>
                ))
                :
                <option selected>No Records</option>
              }
          </select>

          {/* <label for="country">Country</label>
          <select id="country" name="country">
            <option value="australia">Australia</option>
            <option value="canada">Canada</option>
            <option value="usa">USA</option>
          </select> */}

          <label for="subject">Subject</label>
          <textarea id="subject" name="subject" placeholder="Write something.."  value={subject}
            onChange= {e => setsubject(e.target.value)} style={ {height: '150px'} }></textarea>

          {/* <input type="submit" value="Submit" /> */}
          <button type="submit" class="btn btn-primary mt-3">Submit</button>

        </form>
      </div>
  )
}

export default Contact



{/* <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header text-center">
                        <h3>Contact Us</h3>
                    </div>
                    <div class="card-body">
                        <form>
                            <div class="form-group">
                                <label for="name">Name</label>
                                <input type="text" class="form-control" id="name" placeholder="Your Name"/>
                            </div>
                            <div class="form-group">
                                <label for="email">Email</label>
                                <input type="email" class="form-control" id="email" placeholder="Your Email"/>
                            </div>
                            <div class="form-group">
                                <label for="phone">Phone</label>
                                <input type="text" class="form-control" id="phone" placeholder="Your Phone Number"/>
                            </div>
                            <div class="form-group">
                                <label for="message">Message</label>
                                <textarea class="form-control" id="message" rows="5" placeholder="Your Message"></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary btn-block">Send Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div> */}