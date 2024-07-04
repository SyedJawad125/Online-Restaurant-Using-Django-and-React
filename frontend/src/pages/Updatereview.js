import {React, useState, useEffect} from 'react'
import { useNavigate , useLocation} from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance';


const Updatereview = () => {

  const navigate = useNavigate()
  const location = useLocation()
  const data = location.state.data

  const [rating, setrating] = useState(data.rating)
  const [comment, setcomment] = useState(data.comment)
  const [restaurant, setrestaurant] = useState(data.restaurant)
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

      const payload = {"id": data.id, "rating":rating , "comment":comment, "restaurant":restaurant}
      
      const response = await axiosInstance.patch('/restaurent/review', payload , {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      if (response){
        console.log('Response:', response.data);
        navigate('/review', {state: {message: 'Review Update!'}})
      }
      // Handle success
    } catch (error) {
      console.error('Error:', error);
      // Handle error
    }
  };

  return (
    <div class='container' style={{ marginLeft: '200px' }}>
        <h2 class='mt-4'>Update Review Here :</h2>
      <form class='mt-3' onSubmit={handleSubmit}>
        <div class="mb-3">
          <label for="rating" class="form-label">Rating</label>
          <input type="rating" class="form-control" id="rating" aria-describedby="rating"  value={rating}
            onChange= {e => setrating(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="comment" class="form-label">Comment</label>
          <input type="text" class="form-control" id="comment" aria-describedby="comment" value={comment}
            onChange= {e => setcomment(e.target.value)}/>
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

export default Updatereview