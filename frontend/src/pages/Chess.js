import React , { useState, useEffect } from 'react';
import Request from '../Request';
import Board from '../components/Board';
import io from 'socket.io-client'
import {config} from '../config';
import Button from '@material-ui/core/Button';

import './Chess.css'

function Chess() {
  const [is_active_board, setIsActiveBoard] = useState(false);
  const [board, setBoard] = useState([]);
  const [link, setLink] = useState('');

  const doCreate = () => {
     var r = new Request();
     r.get('chess/create/board')
     .then((payload) => {
      setBoard(payload.cells);
      setIsActiveBoard(true);
      localStorage.setItem('board',payload.uuid);
      setLink(`${config.siteURL}board/${payload.uuid}`);
    })

  }

  useEffect(() => { 
    // var r = new Request();
    // r.get('chess/get/board')
    // .then((payload) => {
    //    setBoard(payload);
    // });
    if(localStorage.getItem('board')){
      var r = new Request();
      r.get(`chess/get/board/${localStorage.getItem('board')}`)
      .then((payload) => {
       setBoard(payload.cells);
       setIsActiveBoard(true);
     })
    }
    var socket = io(`${config.socketURL}`)
    socket.on('messages', (message) => {
      console.log(message);
    });

    socket.on('connect', () => {
        socket.emit(
          'login',
        {
          login: localStorage.getItem('login')
        });
    });

    socket.on('update_online_user', (payload) => {
        console.log(payload);
    });


  }, [])
  return (
    <div className="Chess" >
       {
         is_active_board?
         <>
          <p className="link">{link}</p>
          <Board id="board" board={board} />
         </>
         :
         <div className="create-game-div">
         <Button 
         variant="contained" 
         color="primary" 
         onClick={doCreate}
         >
           Create a new game board.
         </Button>
         </div>
       }
         
    </div> 
  );
}

export default Chess;