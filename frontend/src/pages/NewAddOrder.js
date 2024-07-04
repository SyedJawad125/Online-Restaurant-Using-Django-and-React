import React, {useState} from 'react'
import axiosInstance from '../context/AxiosInstance'


const NewAddOrder = () => {

    const [orderDetails, setOrderDetails] = useState([{ unit_price: '', quantity: '' }]);
    const [formData, setFormData] = useState({
        delivery_address: '',
        status: 'booked',
        restaurant: 2,
        OrderDetail: orderDetails
    });

    const handleInputChange = (e, index) => {
        const { name, value } = e.target;
        const details = [...orderDetails];
        details[index][name] = value;
        setOrderDetails(details);
        setFormData({ ...formData, OrderDetail: details });
    };

    const handleAddDetail = () => {
        setOrderDetails([...orderDetails, { unit_price: '', quantity: '', menuitem: '' }]);
    };

    const handleFormChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axiosInstance.post('/restaurent/order', formData);
            console.log('Order submitted successfully:', response.data);
        } catch (error) {
            console.error('Error submitting order:', error);
        }
    };

    return (
        <div class='container' style={{ marginLeft: '200px' }}>
            <h2>Order Form</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="delivery_address" className="form-label">Delivery Address</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="delivery_address" 
                        name="delivery_address" 
                        value={formData.delivery_address}
                        onChange={handleFormChange}
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="restaurant" className="form-label">Restaurant</label>
                    <input 
                        type="number" 
                        className="form-control" 
                        id="restaurant" 
                        name="restaurant" 
                        value={formData.restaurant}
                        onChange={handleFormChange}
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="status" className="form-label">Status</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="status" 
                        name="status" 
                        value={formData.status}
                        onChange={handleFormChange}
                        required 
                    />
                </div>
                <h4>Order Details</h4>
                {orderDetails.map((detail, index) => (
                    <div key={index} className="mb-3 border p-3">
                        <div className="mb-3">
                            <label className="form-label">Unit Price</label>
                            <input 
                                type="number" 
                                className="form-control" 
                                name="unit_price" 
                                value={detail.unit_price}
                                onChange={(e) => handleInputChange(e, index)}
                                required 
                            />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Quantity</label>
                            <input 
                                type="number" 
                                className="form-control" 
                                name="quantity" 
                                value={detail.quantity}
                                onChange={(e) => handleInputChange(e, index)}
                                required 
                            />
                        </div>
                        {/* <div className="mb-3">
                            <label className="form-label">Menu Item</label>
                            <input 
                                type="number" 
                                className="form-control" 
                                name="menuitem" 
                                value={detail.menuitem}
                                onChange={(e) => handleInputChange(e, index)}
                                required 
                            />
                        </div> */}
                    </div>
                ))}
                <button type="button" className="btn btn-primary" style={{ marginRight: '20px' }} onClick={handleAddDetail}>+</button>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </div>
    );
}

export default NewAddOrder




const OrderForm = () => {
    const [orderDetails, setOrderDetails] = useState([{ unit_price: '', quantity: '', menuitem: '' }]);
    const [formData, setFormData] = useState({
        delivery_address: '',
        status: 'booked',
        restaurant: '',
        OrderDetail: orderDetails
    });

    const handleInputChange = (e, index) => {
        const { name, value } = e.target;
        const details = [...orderDetails];
        details[index][name] = value;
        setOrderDetails(details);
        setFormData({ ...formData, OrderDetail: details });
    };

    const handleAddDetail = () => {
        setOrderDetails([...orderDetails, { unit_price: '', quantity: '', menuitem: '' }]);
    };

    const handleFormChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);
        // Submit the form data to the server or handle it as needed
    };

    return (
        <div className="container mt-5">
            <h2>Order Form</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="delivery_address" className="form-label">Delivery Address</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="delivery_address" 
                        name="delivery_address" 
                        value={formData.delivery_address}
                        onChange={handleFormChange}
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="restaurant" className="form-label">Restaurant</label>
                    <input 
                        type="number" 
                        className="form-control" 
                        id="restaurant" 
                        name="restaurant" 
                        value={formData.restaurant}
                        onChange={handleFormChange}
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="status" className="form-label">Status</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="status" 
                        name="status" 
                        value={formData.status}
                        onChange={handleFormChange}
                        required 
                    />
                </div>
                <h4>Order Details</h4>
                {orderDetails.map((detail, index) => (
                    <div key={index} className="mb-3 border p-3">
                        <div className="mb-3">
                            <label className="form-label">Unit Price</label>
                            <input 
                                type="number" 
                                className="form-control" 
                                name="unit_price" 
                                value={detail.unit_price}
                                onChange={(e) => handleInputChange(e, index)}
                                required 
                            />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Quantity</label>
                            <input 
                                type="number" 
                                className="form-control" 
                                name="quantity" 
                                value={detail.quantity}
                                onChange={(e) => handleInputChange(e, index)}
                                required 
                            />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Menu Item</label>
                            <input 
                                type="number" 
                                className="form-control" 
                                name="menuitem" 
                                value={detail.menuitem}
                                onChange={(e) => handleInputChange(e, index)}
                                required 
                            />
                        </div>
                    </div>
                ))}
                <button type="button" className="btn btn-secondary mb-3" onClick={handleAddDetail}>+</button>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </div>
    );
};


