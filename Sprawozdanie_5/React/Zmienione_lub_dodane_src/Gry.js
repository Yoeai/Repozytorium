import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom';

function Gry() {

    useEffect(() => {
        fetchItems();
    },[]);

    const [id, setIds] = useState([]);

    const fetchItems = async () => {
        const data = await fetch('http://127.0.0.1:8000/Game/')

        const id = await data.json();
        console.log(id);
        setIds(id);
    };

  return (
    <div id="gry">
        {id.map(id => (
            <h2 key={id.id}>
            <Link to={'/Gry/${id.id}'}>{id.tytul}</Link>
            <br></br>
            {id.wydawca}
            <br></br>
            {id.gatunek}
            </h2>
        ))}
    </div>
  );
}

export default Gry;