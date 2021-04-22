import React , { useState, useEffect } from 'react';
import Request from '../Request';
import Board from '../components/Board';

function Chess() {
  const [board, setBoard] = useState();
  useEffect(() => { 
    var r = new Request();
    r.get('/static/db.json')
    .then((payload) => {
       setBoard(payload);
    });
  }, [])
  return (
    <div className="Chess" >
       <h1>Chess</h1>
       <Board />  
    </div>
  );
}

export default Chess;