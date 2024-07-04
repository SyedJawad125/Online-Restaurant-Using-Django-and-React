import {React, useEffect, useState} from 'react'
import {Link, useNavigate, useLocation} from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axiosInstance from '../context/AxiosInstance';
import '../App.css'

const Menu = () => {

  const navigate = useNavigate()
  const location = useLocation()

  const [records, setRecords] = useState([])
  const [data, setData] = useState([])
  const [flag, setFlag] = useState(false)

  useEffect(()=>{
    if (location.state && location.state.message){
        toast.success(location.state.message)
        navigate('/menu', {state: ''})
      }
      else if (flag == true){
        toast.success('Menu deleted')
        setFlag(false)
      }

    const receiveData = async () =>{
        const res = await axiosInstance.get('/restaurent/menu')
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
      const res = await axiosInstance.delete(`/restaurent/menu?id=${id}`)
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
  navigate('/update/Updatemenu', {state: {data: item}})
}


  return (
    <div class='container' style={{ marginLeft: '200px' }} >
        <h2 class='mt-4'>List Of Menu</h2>

        <Link type="submit" class="btn btn-primary mt-3" to='/add/Addmenu'>Add Menu</Link>
        
        <br/><br/>

        {data ? <p>Total: {data.count}</p> : <p>Total: 0</p>}

        <div class="row">
            
            { records ? 
            records.map(item => (
                <div class="card" style={{width: "18rem"}}>
                <div class="card-body">
                    <h5 class="card-title">Name : {item.name}</h5>
                    <h5 class="card-title">Details : {item.description}</h5>
                    <h5 class="card-title">Restaurant : {item.restaurant_name}</h5>

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

export default Menu