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

    <div class="container contact-form" style={{ marginLeft: '200px' }}>
    <div class="contact-image">
      <img src="https://image.ibb.co/kUagtU/rocket_contact.png" alt="rocket_contact"/>
    </div>
    <form method="post" onSubmit={handleSubmit}>
      <h3>Drop Us a Message</h3>
      <div class="row">
        <div class="col-md-6">
          <div class="form-group">
            <input type="text" name="name" class="form-control" placeholder="Your Name *" value={name}
                  onChange= {e => setname(e.target.value)} />
          </div>
          <div class="form-group">
            <input type="text" name="name" class="form-control" placeholder="Your country *" value={country}
            onChange= {e => setcountry(e.target.value)} />
          </div>         
          <div class="form-group">
            <input type="text" name="phone" class="form-control" placeholder="Your Phone Number *" value={phone_number}
                  onChange= {e => setphone_number(e.target.value)}/>
          </div>
          <div class="form-group">
            <input type="email" name="email" class="form-control" placeholder="Your Email *"  value={email}
                  onChange= {e => setemail(e.target.value)} />
          </div>
          <div class="form-group">
          <select class="form-control" aria-label="Default select example" onChange={e => setrestaurant(e.target.value)}>
            <option selected>Select Restaurant</option>

              { restaurantRecords ?
                restaurantRecords.map(item => (
                  <option value={item.id} key={item.id}>{item.name}</option>
                ))
                :
                <option selected>No Records</option>
              }
          </select>
          </div>
          <div class="form-group">
            <input type="submit" name="btnSubmit" class="btnContact" value="Send Message" />
          </div>
        </div>
        <div class="col-md-6">
          <div class="form-group">
            <textarea name="message" class="form-control" placeholder="Your Message *" style={{ width: '100%', height: '275px' }}
            value={subject} onChange= {e => setsubject(e.target.value)} ></textarea>
          </div>
        </div>
      </div>
    </form>
  </div>





    // <div class='container' style={{ marginLeft: '200px' }}  >
    //     <h2 class='mt-3'>Contact Us</h2>
    //     <form action="action_page.php"  onSubmit={handleSubmit}>

    //       <label for="name" class='mt-3'>Name</label>
    //       <input type="text" id="name" name="name" placeholder="Your name.." value={name}
    //         onChange= {e => setname(e.target.value)} />

    //       <label for="country">Country</label>
    //       <input type="text" id="country" name="country" placeholder="Your country name.."  value={country}
    //         onChange= {e => setcountry(e.target.value)} />

    //       <label for="phone_number">Phone Number</label>
    //       <input type="text" id="phone_number" name="phone_number" placeholder="Your phone number.."  value={phone_number}
    //         onChange= {e => setphone_number(e.target.value)}/>

    //       <label for="email">Email</label>
    //       <input type="text" id="email" name="email" placeholder="Your email.." value={email}
    //         onChange= {e => setemail(e.target.value)} />

    //       <select class="form-select" aria-label="Default select example" onChange={e => setrestaurant(e.target.value)}>
    //         <option selected>Select Restaurant</option>

    //           { restaurantRecords ?
    //             restaurantRecords.map(item => (
    //               <option value={item.id} key={item.id}>{item.name}</option>
    //             ))
    //             :
    //             <option selected>No Records</option>
    //           }
    //       </select>

    //       <label for="subject">Subject</label>
    //       <textarea id="subject" name="subject" placeholder="Write something.."  value={subject}
    //         onChange= {e => setsubject(e.target.value)} style={ {height: '150px'} }></textarea>

    //       {/* <input type="submit" value="Submit" /> */}
    //       <button type="submit" class="btn btn-primary mt-3">Submit</button>

    //     </form>
    //   </div>4

    //
  )
}

export default Contact



