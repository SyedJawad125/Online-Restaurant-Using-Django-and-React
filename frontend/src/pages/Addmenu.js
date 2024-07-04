import {React,useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance'


const Addmenu = () => {

  const navigate = useNavigate()

  const [name, setname] = useState('')
  const [description, setdescription] = useState('')
  const [restaurant, setrestaurant] = useState('')
  const [restaurantRecords, setrestaurantRecords] = useState([])


  useEffect(()=>{
    // For dropdown list
    const fetchPostion = async () =>{
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
  fetchPostion();
 

  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {

        const payload = {"name":name , "description":description,"restaurant":restaurant }
        
        const response = await axiosInstance.post('/restaurent/menu', payload , {
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (response){
        console.log('Response:', response.data);
        navigate('/menu', {state: {message: 'Menu Added!'}})
        }
        // Handle success
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
    };

  return (
    <div class='container' style={{ marginLeft: '200px' }}>
        <h2 class='mt-4'>Add Menu Here :</h2>
      <form class='mt-3' onSubmit={handleSubmit}>
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input type="name" class="form-control" id="name" aria-describedby="name"  value={name}
            onChange= {e => setname(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="description" class="form-label">Description</label>
          <input type="text" class="form-control" id="description" aria-describedby="description" value={description}
            onChange= {e => setdescription(e.target.value)}/>
        </div>

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

        <button type="submit" class="btn btn-primary mt-3">Submit</button>
      </form>
    </div>
  )
}

export default Addmenu