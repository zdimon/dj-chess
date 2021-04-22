import React , { useState, useEffect } from 'react';

import Request from '../Request';


function Chess() {
  useEffect(() => { 
    console.log('sssssss');
    var r = new Request();
    r.get('/static/db.json')
    .then((payload) => {
      console.log(payload);
    });
  }, [])
  return (
    <div className="Chess" >
       <h1>Chess</h1>
    </div>
  );
}

export default Chess;