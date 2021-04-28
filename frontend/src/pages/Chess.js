import React , { useState, useEffect } from 'react';
import Request from '../Request';
import Board from '../components/Board';
import io from 'socket.io-client'
import {config} from '../config';


function Chess() {
  const [board, setBoard] = useState([[]]);
  useEffect(() => { 
    var r = new Request();
    r.get('chess/get/board')
    .then((payload) => {
       setBoard(payload);
    });
    var socket = io(`${config.socketURL}`)
    socket.on('messages', (message) => {
      console.log(message);
    }
    )
  }, [])
  return (
    <div className="Chess" >
       <Board id="board" board={board} />  
    </div> 
  );
}

export default Chess;