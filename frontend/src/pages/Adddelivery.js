import {React,useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance'


const Adddelivery = () => {
  const navigate = useNavigate()

  const [customer_name, setcustomer_name] = useState('')
  const [customer_address, setcustomer_address] = useState('')
  const [customer_phone, setcustomer_phone] = useState('')
  const [delivery_status, setdelivery_status] = useState('')
  const [delivery_person_name, setdelivery_person_name] = useState('')
  const [delivery_person_contact, setdelivery_person_contact] = useState('')
  const [restaurant_address, setrestaurant_address] = useState('')
  const [restaurant_phone, setrestaurant_phone] = useState('')
  const [total_amount, settotal_amount] = useState('')
  const [payment_status, setpayment_status] = useState('')
  const [order_bill, setorder_bill] = useState('')
  const [restaurant, setrestaurant] = useState('')
  const [orderRecords, setorderRecords] = useState([])
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
 
  // For dropdown list
  const fetchorder = async () =>{
    const res = await axiosInstance.get('/restaurent/order') 
    try{
        if (res){
          setorderRecords(res.data.data.data)
        }
    }
    catch (error){
        console.log('error occured', error)
    }
}
fetchorder();

  }, [])


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {

        const payload = {"customer_name":customer_name , "customer_address":customer_address,
          "customer_phone":customer_phone,"delivery_status":delivery_status , 
          "delivery_person_name":delivery_person_name,"delivery_person_contact":delivery_person_contact,
          "restaurant_address":restaurant_address, "restaurant_phone":restaurant_phone , 
          "total_amount":total_amount,"payment_status":payment_status,"order_bill":order_bill, "restaurant":restaurant
         }
        
        const response = await axiosInstance.post('/restaurent/delivery', payload , {
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (response){
        console.log('Response:', response.data);
        navigate('/delivery', {state: {message: 'Delivery Added!'}})
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
          <label for="customer_name" class="form-label">Customer Name :</label>
          <input type="customer_name" class="form-control" id="customer_name" aria-describedby="customer_name"  value={customer_name}
            onChange= {e => setcustomer_name(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="customer_address" class="form-label">Customer Address :</label>
          <input type="text" class="form-control" id="customer_address" aria-describedby="customer_address" value={customer_address}
            onChange= {e => setcustomer_address(e.target.value)}/>
        </div>
        <div class="mb-3">
          <label for="customer_phone" class="form-label">Customer Contact :</label>
          <input type="customer_phone" class="form-control" id="customer_phone" aria-describedby="customer_phone"  value={customer_phone}
            onChange= {e => setcustomer_phone(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="delivery_status" class="form-label">Delivery Status :</label>
          <input type="text" class="form-control" id="delivery_status" aria-describedby="delivery_status" value={delivery_status}
            onChange= {e => setdelivery_status(e.target.value)}/>
        </div>
        <div class="mb-3">
          <label for="ndelivery_person_nameme" class="form-label">Delivery Person Name :</label>
          <input type="delivery_person_name" class="form-control" id="delivery_person_name" aria-describedby="delivery_person_name"  value={delivery_person_name}
            onChange= {e => setdelivery_person_name(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="delivery_person_contact" class="form-label">Delivery Person Cont :</label>
          <input type="text" class="form-control" id="delivery_person_contact" aria-describedby="delivery_person_contact" value={delivery_person_contact}
            onChange= {e => setdelivery_person_contact(e.target.value)}/>
        </div>
        <div class="mb-3">
          <label for="restaurant_address" class="form-label">Restaurant Address :</label>
          <input type="restaurant_address" class="form-control" id="restaurant_address" aria-describedby="restaurant_address"  value={restaurant_address}
            onChange= {e => setrestaurant_address(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="restaurant_phone" class="form-label">Restaurant Contact :</label>
          <input type="text" class="form-control" id="restaurant_phone" aria-describedby="restaurant_phone" value={restaurant_phone}
            onChange= {e => setrestaurant_phone(e.target.value)}/>
        </div>
        <div class="mb-3">
          <label for="total_amount" class="form-label">Total Amount :</label>
          <input type="total_amount" class="form-control" id="total_amount" aria-describedby="total_amount"  value={total_amount}
            onChange= {e => settotal_amount(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="payment_status" class="form-label">Payment Status :</label>
          <input type="text" class="form-control" id="payment_status" aria-describedby="payment_status" value={payment_status}
            onChange= {e => setpayment_status(e.target.value)}/>
        </div>

        <select class="form-select" aria-label="Default select example" onChange={e => setorder_bill(e.target.value)}>
            <option selected>Select Order Bill</option>

              { orderRecords ?
                orderRecords.map(item => (
                  <option value={item.id} key={item.id}>{item.bill}</option>
                ))
                :
                <option selected>No Records</option>
              }
        </select>
        
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

export default Adddelivery