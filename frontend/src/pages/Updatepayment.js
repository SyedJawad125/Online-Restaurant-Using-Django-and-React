import {React, useState, useEffect} from 'react'
import { useNavigate , useLocation} from 'react-router-dom'
import axiosInstance from '../context/AxiosInstance';


const Updatepayment = () => {
  

  const navigate = useNavigate()
  const location = useLocation()
  const data = location.state.data

  const [amount, setamount] = useState('')
  const [payment_method, setpayment_method] = useState('')
  const [card_holder_name, setcard_holder_name] = useState('')
  const [card_number, setcard_number] = useState(null)
  const [order_bill, setorder_bill] = useState('')
  const [orderRecords, setorderRecords] = useState([])

  useEffect(()=>{
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

        const payload = {"id": data.id,"amount":amount , "payment_method":payment_method,"card_holder_name":card_holder_name, 
          "card_number":card_number, "order_bill":order_bill}
        
        const response = await axiosInstance.patch('/restaurent/payment', payload , {
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (response){
        console.log('Response:', response.data);
        navigate('/payment', {state: {message: 'Payment Update!'}})
        }
        // Handle success
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
    };

  return (
    <div class='container' style={{ marginLeft: '200px' }}>
        <h2 class='mt-4'>Update Payment Here :</h2>
      <form class='mt-3' onSubmit={handleSubmit}>
        <div class="mb-3">
          <label for="amount" class="form-label">Amount :</label>
          <input type="amount" class="form-control" id="amount" aria-describedby="amount"  value={amount}
            onChange= {e => setamount(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="payment_method" class="form-label">Payment Method :</label>
          <input type="text" class="form-control" id="payment_method" aria-describedby="payment_method" value={payment_method}
            onChange= {e => setpayment_method(e.target.value)}/>
        </div>
        <div class="mb-3">
          <label for="card_holder_name" class="form-label">Card Holder Name :</label>
          <input type="text" class="form-control" id="card_holder_name" aria-describedby="card_holder_name"
           value={card_holder_name} onChange= {e => setcard_holder_name(e.target.value)} />
        </div>
        <div class="mb-3">
          <label for="card_number" class="form-label">Card Number :</label>
          <input type="text" class="form-control" id="card_number" aria-describedby="card_number" value={card_number}
            onChange= {e => setcard_number(e.target.value)} />
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
        
        

        

        <button type="submit" class="btn btn-primary mt-3">Submit</button>
      </form>
    </div>
  )
}

export default Updatepayment