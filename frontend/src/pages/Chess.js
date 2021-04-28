import React , { useState, useEffect } from 'react';
import Request from '../Request';
import Board from '../components/Board';

function Chess() {
  const [board, setBoard] = useState([[]]);
  useEffect(() => { 
    var r = new Request();
    r.get('chess/get/board')
    .then((payload) => {
       setBoard(payload);
    });
  }, [])
  return (
    <div className="Chess" >
       <Board id="board" board={board} />  
    </div> 
  );
}

export default Chess;