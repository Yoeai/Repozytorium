import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom';

function Shop() {

    useEffect(() => {
        fetchItems();
    },[]);

    const [id, setIds] = useState([]);

    const fetchItems = async () => {
        const data = await fetch(
            'https://fakestoreapi.com/products')

        const id = await data.json();
        console.log(id);
        setIds(id);
    };

  return (
    <div>
        {id.map(id => (
            <h2 key={id.id}>
            {id.category}
            <br></br>
            <Link to={'/shop/${id.id}'}>{id.title}</Link>
            <br></br>
            <img src={id.image} alt=""/>
            <br></br>
            {id.price} $
            <hr></hr>
            </h2>
        ))}
    </div>
  );
}

export default Shop;
