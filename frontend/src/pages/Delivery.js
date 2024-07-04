import {React, useEffect, useState} from 'react'
import {Link, useNavigate, useLocation} from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axiosInstance from '../context/AxiosInstance';
import '../App.css'



const Delivery = () => {
 
  const navigate = useNavigate()
  const location = useLocation()

  const [records, setRecords] = useState([])
  const [data, setData] = useState([])
  const [flag, setFlag] = useState(false)
    
  useEffect(()=>{
    if (location.state && location.state.message){
        toast.success(location.state.message)
        navigate('/delivery', {state: ''})
      }
      else if (flag == true){
        toast.success('Delivery deleted')
        setFlag(false)
      }
  
    const receiveData = async () =>{
        const res = await axiosInstance.get('/restaurent/delivery')
        try{
            if (res){
                setRecords(res.data.data.data)
                setData(res.data)
            }
        }
        catch (error){
            console.log('error occured', error)
        }
    }
    receiveData();
  },   [flag, location.state])
  
  
  const deleteRecord = async (id) => {
  try{
      const res = await axiosInstance.delete(`/restaurent/delivery?id=${id}`)
      if(res){
          console.log('Delete Successfully')
          setFlag(true)
      }
  }
  catch(error){
      console.log(error)
  }
  }
  
  const updateRecord = async (item) => {
    navigate('/update/Updatedelivery', {state: {data: item}})
    }

  return (
    <div class='container' style={{ marginLeft: '200px' }} >
        <h2 class='mt-4'>List Of Payment</h2>

        <Link type="submit" class="btn btn-primary mt-3" to='/add/Adddelivery'>Add Delivery</Link>
        
        <br/><br/>

        {data ? <p>Total: {data.count}</p> : <p>Total: 0</p>}

        <div class="row">
            
            { records ? 
            records.map(item => (
                <div class="card" style={{width: "18rem"}}>
                <div class="card-body">
                    
                    <h5 class="card-title">Cust Name : {item.customer_name}</h5>
                    <h5 class="card-title">Cust Address : {item.customer_address}</h5>
                    <h5 class="card-title">Cust Contact : {item.customer_phone}</h5>
                    <h5 class="card-title">Del Status : {item.delivery_status}</h5>
                    <h5 class="card-title">Del Person Name : {item.delivery_person_name}</h5>
                    <h5 class="card-title">Del Person Cont : {item.delivery_person_contact}</h5>
                    <h5 class="card-title">Rest Address : {item.restaurant_address}</h5>
                    <h5 class="card-title">Rest Contact : {item.restaurant_phone}</h5>
                    <h5 class="card-title">Total Amount : {item.total_amount}</h5>
                    <h5 class="card-title">Payment Status : {item.payment_status}</h5>
                    <h5 class="card-title">Order Bill : {item.order_bill?.bill}</h5>
                    <h5 class="card-title">Rest Name : {item.restaurant_name}</h5>
                    
                    {/* <h5 class="card-context">{item.created_by_name}</h5> */}
                    <button class='btn btn-danger'onClick={()=> deleteRecord(item.id)}>Delete</button>
                    <button class='btn btn-primary mx-2' onClick={()=> updateRecord(item)}>Update</button>
                </div>
                </div>

    )) : 
    <p>Loading....</p>
    }
        </div>  
        <ToastContainer/>
    </div>
      )
}

export default Delivery

