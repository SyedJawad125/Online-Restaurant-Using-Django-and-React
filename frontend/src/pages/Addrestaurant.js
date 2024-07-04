import {React,useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance'



const Addrestaurant = () => {

    const navigate = useNavigate()

    const [name, setname] = useState('')
    const [address, setaddress] = useState('')
    const [phone_number, setphone_number] = useState('')
    const [email, setemail] = useState('')
    const [website, setwebsite] = useState('')
    const [opening_hours, setopening_hours] = useState('')
    const [closing_hours, setclosing_hours] = useState('')
    const [cuisine_type, setcuisine_type] = useState('')
    // const [deptRecords, setdeptRecords] = useState([])
    // const [salRecords, setsalRecords] = useState([])

    useEffect(()=>{




    }, [])

const handleSubmit = async (e) => {
    e.preventDefault();
    try {

        const payload = {"name":name , "address":address, "phone_number":phone_number , "email":email , 
        "website":website, "opening_hours":opening_hours, "closing_hours":closing_hours, "cuisine_type":cuisine_type}
        
        const response = await axiosInstance.post('/restaurent/restaurant', payload , {
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (response){
        console.log('Response:', response.data);
        navigate('/restaurant', {state: {message: 'Restaurant Added!'}})
        }
        // Handle success
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
    };




  return (
    <div class='container' style={{ marginLeft: '200px' }}>
        <h2 class='mt-4'>Add Restaurant Here :</h2>
      <form class='mt-3' onSubmit={handleSubmit}>
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input type="name" class="form-control" id="name" aria-describedby="name"  value={name}
            onChange= {e => setname(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="address" class="form-label">Address</label>
          <input type="text" class="form-control" id="address" aria-describedby="address" value={address}
            onChange= {e => setaddress(e.target.value)}/>
        </div>
        <div class="mb-3">
          <label for="phone_number" class="form-label">Number</label>
          <input type="text" class="form-control" id="phone_number" aria-describedby="phone_number" value={phone_number}
            onChange= {e => setphone_number(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="text" class="form-control" id="email" aria-describedby="email" value={email}
            onChange= {e => setemail(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="website" class="form-label">Website</label>
          <input type="text" class="form-control" id="website" aria-describedby="website"  value={website}
            onChange= {e => setwebsite(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="opening_hours" class="form-label">Opening Time</label>
          <input type="text" class="form-control" id="opening_hours" aria-describedby="opening_hours" value={opening_hours}
            onChange= {e => setopening_hours(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="closing_hours" class="form-label">Closing Time</label>
          <input type="text" class="form-control" id="closing_hours" aria-describedby="closing_hours" value={closing_hours}
            onChange= {e => setclosing_hours(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="cuisine_type" class="form-label">Cuisine Type</label>
          <input type="text" class="form-control" id="cuisine_type" aria-describedby="cuisine_type"  value={cuisine_type}
            onChange= {e => setcuisine_type(e.target.value)} />
        </div>

        {/* <div class="mb-3">
          <label for="dept_has_position" class="form-label">Dept has Position</label>
          <input type="text" class="form-control" id="dept_has_position" aria-describedby="dept_has_position"  value={dept_has_position}
            onChange= {e => setdept_has_position(e.target.value)} />
        </div> */}
        {/* <div class="mb-3">
          <label for="posi_has_salary" class="form-label">Posi has Salary</label>
          <input type="text" class="form-control" id="posi_has_salary" aria-describedby="posi_has_salary"  value={posi_has_salary}
            onChange= {e => setposi_has_salary(e.target.value)} />
        </div> */}


        {/* <select class="form-select" aria-label="Default select example" onChange={e => setdept_has_position(e.target.value)}>
        <option selected>Select Position</option>

          { deptRecords ?
            deptRecords.map(item => (
              <option value={item.id} key={item.id}>{item.dept_name}</option>
            ))
            :
            <option selected>No Records</option>
          }
        </select>

        <select class="form-select" aria-label="Default select example" onChange={e => setposi_has_salary(e.target.value)}>
        <option selected>Select Salary </option>

          { salRecords ?
            salRecords.map(item => (
              <option value={item.id} key={item.id}>{item.net_salary}</option>
            ))
            :
            <option selected>No Records</option>
          }
        </select> */}
        <button type="submit" class="btn btn-primary mt-3">Submit</button>
      </form>
    </div>
  )
}

export default Addrestaurant