import {React, useEffect, useState} from 'react'
import {Link, useNavigate, useLocation} from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axiosInstance from '../context/AxiosInstance';
import '../App.css'


const Restaurant = () => {

    const navigate = useNavigate()
    const location = useLocation()

    const [records, setRecords] = useState([])
    const [data, setData] = useState([])
    const [flag, setFlag] = useState(false)

    useEffect(()=>{
      if (location.state && location.state.message){
          toast.success(location.state.message)
          navigate('/restaurant', {state: ''})
        }
        else if (flag == true){
          toast.success('Restaurant deleted')
          setFlag(false)
        }

      const receiveData = async () =>{
          const res = await axiosInstance.get('/restaurent/restaurant')
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
            const res = await axiosInstance.delete(`/restaurent/restaurant?id=${id}`)
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
        navigate('/update/Updaterestaurant', {state: {data: item}})
    }



  return (
    <div class='container' style={{ marginLeft: '200px' }} >
        <h2 class='mt-4'>List Of Restaurant We deals Here!</h2>

        <Link type="submit" class="btn btn-primary mt-3" to='/add/Addrestaurant'>Add Restaurant</Link>
        
        <br/><br/>

        {data ? <p>Total: {data.count}</p> : <p>Total: 0</p>}

        <div class="row">
            
            { records ? 
            records.map(item => (
                <div class="card" style={{width: "18rem"}}>
                <div class="card-body">
                    <h5 class="card-title">Name : {item.name}</h5>
                    <h5 class="card-title">City : {item.address}</h5>
                    <h5 class="card-title">Number : {item.phone_number}</h5>
                    <h5 class="card-title">Email : {item.email}</h5>
                    <h5 class="card-title">Website : {item.website}</h5>
                    <h5 class="card-title">Opening Time : {item.opening_hours}</h5>
                    <h5 class="card-title">Closing Time : {item.closing_hours}</h5>
                    <h5 class="card-title">Cuisine Type : {item.cuisine_type}</h5>


                    
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

export default Restaurant