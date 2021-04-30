import Request from '../Request';
import React , { useState, useEffect } from 'react';

function Figures() {

  useEffect(() => { 

    var r = new Request();
    r.get('chess/get/figures')
    .then((payload) => {
     console.log(payload);
   })

  },[]);

  return (
    <div className="Figures" >
        Figures
    </div>  
  );
}

export default Figures;   