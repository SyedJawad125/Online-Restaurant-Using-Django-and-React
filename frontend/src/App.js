// import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Services from './pages/Services';
import About from './pages/About';
import Restaurant from './pages/Restaurant';
import Addrestaurant from './pages/Addrestaurant';
import Updaterestaurant from './pages/Updaterestaurant';
import Menu from './pages/Menu';
import Addmenu from './pages/Addmenu';
import Updatemenu from './pages/Updatemenu';
import Menuitem from './pages/Menuitem';
import Addmenuitem from './pages/Addmenuitem';
import Updatemenuitem from './pages/Updatemenuitem';
import Order from './pages/Order';
// import Addorder from './pages/Addorder';
import NewAddOrder from './pages/NewAddOrder';
import Updateorder from './pages/Updateorder';
import Payment from './pages/Payment';
import Addpayment from'./pages/Addpayment';
import Updatepayment from './pages/Updatepayment';
import Review from './pages/Review';
import Addreview from './pages/Addreview';
import Updatereview from './pages/Updatereview';
import Promotion from './pages/Promotion';
import Addpromotion from './pages/Addpromotion';
import Updatepromotion from './pages/Updatepromotion';
import Delivery from './pages/Delivery';
import Adddelivery from './pages/Adddelivery';
import Updatedelivery from './pages/Updatedelivery';
import Contact from './pages/Contact';
import Login from './pages/Login';
import SignUp from './pages/SignUp';
import {Routes, Route} from 'react-router-dom'
import ProtectedRoute from './context/ProtectedRoute'



function App() {
  return (
    <div>
      {localStorage.getItem('token') ? <Navbar/> : <p></p>}
      {/* <Navbar/> */}
      <Routes>
        <Route path='/login' element={<Login/>} />
        <Route path='/SignUp' element={<SignUp/>}  />
        <Route element={<ProtectedRoute />}>
            <Route path='/' element={<Home/>}  />
            <Route path='/services' element={<Services/>}  />
            <Route path='/about' element={<About/>}  />
            <Route path='/restaurant' element={<Restaurant/>}  />
            <Route path='/add/Addrestaurant' element={<Addrestaurant/>}  />
            <Route path='/update/Updaterestaurant' element={<Updaterestaurant/>}  />
            <Route path='/menu' element={<Menu/>}  />
            <Route path='/add/Addmenu' element={<Addmenu/>}  />
            <Route path='/update/Updatemenu' element={<Updatemenu/>}  />
            <Route path='/menuitem' element={<Menuitem/>}  />
            <Route path='/add/Addmenuitem' element={<Addmenuitem/>}  />
            <Route path='/update/Updatemenuitem' element={<Updatemenuitem/>}  />
            <Route path='/order' element={<Order/>}  />
            <Route path='/add/NewAddorder' element={<NewAddOrder/>}  />
            <Route path='/update/Updateorder' element={<Updateorder/>}  />
            <Route path='/payment' element={<Payment/>}  />
            <Route path='/add/Addpayment' element={<Addpayment/>}  />
            <Route path='/update/Updatepayment' element={<Updatepayment/>}  />
            <Route path='/review' element={<Review/>}  />
            <Route path='/add/Addreview' element={<Addreview/>}  />
            <Route path='/update/Updatereview' element={<Updatereview/>}  />
            <Route path='/promotion' element={<Promotion/>}  />
            <Route path='/add/Addpromotion' element={<Addpromotion/>}  />
            <Route path='/update/Updatepromotion' element={<Updatepromotion/>}  />
            <Route path='/delivery' element={<Delivery/>}  />
            <Route path='/add/Adddelivery' element={<Adddelivery/>}  />
            <Route path='/update/Updatedelivery' element={<Updatedelivery/>}  />
            <Route path='/contact' element={<Contact/>}  />
            {/* <Route path='/' element={<Home/>}  />
            <Route path='/' element={<Home/>}  /> */}


        </Route>
        
      </Routes>
    </div>
  );
}

export default App;
