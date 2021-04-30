import Request from '../Request';
import React , { useState, useEffect } from 'react';
import './Figures.css';



function Figures(props) {
  const [figures, setFigures] = useState([]);
  const [activeFigure, setActiveFigure] = useState(null);
  

  const doActive = (id) => {
    setActiveFigure(id);
    props.doActiveFigure(id);
    // evt.currentTarget.attributes['data-id'].value
  }
  useEffect(() => { 

    var r = new Request();
    r.get('chess/get/figures') 
    .then((payload) => {
      setFigures(payload);
   })

  },[]);

  return (
    <div className="figures-wrapper" >
           
        {
          figures.map((el) => { 
            return (
              <div className={`figure ${el.id === activeFigure ? "active" : ""}`} onClick={() => doActive(el.id)}> 
                <img data-id={el.id} src={el.figure.get_image_absolute_url} />
              </div>
            )
          })
        }
    </div>   
  );
}

export default Figures;   