import {React, useState, useEffect} from 'react'
import { useNavigate , useLocation} from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance';

const Updatepromotion = () => {
  const navigate = useNavigate()
  const location = useLocation()
  const data = location.state.data

  const [name, setname] = useState(data.name)
  const [description, setdescription] = useState(data.description)
  const [start_date, setstart_date] = useState(data.start_date)
  const [end_date, setend_date] = useState(data.end_date)
  const [discount_percentage, setdiscount_percentage] = useState(data.discount_percentage)
  const [discount_amount, setdiscount_amount] = useState(data.discount_amount)
  const [promo_code, setpromo_code] = useState(data.promo_code)
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

        const payload = {"id":data.id,"name":name ,"description":description,"start_date":start_date,
          "end_date":end_date ,"discount_percentage":discount_percentage , 
          "discount_amount":discount_amount,"promo_code":promo_code, "restaurant":restaurant
         }
        
        const response = await axiosInstance.patch('/restaurent/promotion', payload , {
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (response){
        console.log('Response:', response.data);
        navigate('/promotion', {state: {message: 'Promotion Update!'}})
        }
        // Handle success
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
    };

  return (
    <div class='container' style={{ marginLeft: '200px' }}>
    <h2 class='mt-4'>Add Promotion Here :</h2>
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
    <div class="mb-3">
      <label for="start_date" class="form-label">Start Date</label>
      <input type="start_date" class="form-control" id="start_date" aria-describedby="start_date"  value={start_date}
        onChange= {e => setstart_date(e.target.value)} />
    </div>
    <div class="mb-3">
      <label for="end_date" class="form-label">End Date</label>
      <input type="text" class="form-control" id="end_date" aria-describedby="end_date" value={end_date}
        onChange= {e => setend_date(e.target.value)}/>
    </div>
    <div class="mb-3">
      <label for="discount_percentage" class="form-label">Dis Percentage</label>
      <input type="discount_percentage" class="form-control" id="discount_percentage" aria-describedby="discount_percentage"  value={discount_percentage}
        onChange= {e => setdiscount_percentage(e.target.value)} />
    </div>
    <div class="mb-3">
      <label for="discount_amount" class="form-label">Dis Amount</label>
      <input type="text" class="form-control" id="discount_amount" aria-describedby="discount_amount" value={discount_amount}
        onChange= {e => setdiscount_amount(e.target.value)}/>
    </div>
    <div class="mb-3">
      <label for="promo_code" class="form-label">Promo Code</label>
      <input type="text" class="form-control" id="promo_code" aria-describedby="promo_code" value={promo_code}
        onChange= {e => setpromo_code(e.target.value)}/>
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

export default Updatepromotion