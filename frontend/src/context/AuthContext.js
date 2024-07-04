import React, { createContext, useState, useEffect } from 'react';
import axiosInstance from './AxiosInstance'


export const AuthCon = createContext();


export const AuthContext = ({ children }) => {

  const [token, setToken] = useState(()=> {
    const token = localStorage.getItem('token')
    return token ? JSON.parse(token) : null
  })

  const login = (userToken) => {
    localStorage.setItem('token', JSON.stringify(userToken))
    setToken(userToken);
  };

  const logout = async () => {
    const res = await axiosInstance.post('/user/logout')
    if (res){
      console.log('Logout')
    }
    localStorage.removeItem('token')
    setToken(null);
  };


  // useEffect(()=>{
  //   const storedToken = localStorage.getItem('token')
    
  //   if (storedToken){
  //     setToken(JSON.parse(storedToken))
  //   }
  // }, [token])


  return (
    <AuthCon.Provider value={{ token, login, logout }}>
      {children}
    </AuthCon.Provider>
  );
};

