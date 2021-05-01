import React , { useState, useEffect } from 'react';
import Request from '../Request';
import Board from '../components/Board';
import io from 'socket.io-client'
import {config} from '../config';
import Button from '@material-ui/core/Button';
import Figures from '../components/Figures';
import './Chess.css'
import Grid from '@material-ui/core/Grid';

function Chess() {
  const [is_active_board, setIsActiveBoard] = useState(false);
  const [board, setBoard] = useState([]);
  const [link, setLink] = useState('');

  const [activeCell, setActiveCell] = useState(null);
  const [activeFigure, setActiveFigure] = useState(null);
  const [figures, setFigures] = useState([]);
  


  const doCreate = () => {
     var r = new Request();
     r.get('chess/create/board')
     .then((payload) => {
      setBoard(payload.cells);
      setIsActiveBoard(true);
      localStorage.setItem('board',payload.uuid);
      setLink(`${config.siteURL}board/${payload.uuid}`);
      getFigures();
    })

  }

  useEffect(() => { 

    if(localStorage.getItem('board')){
      var r = new Request();
      r.get(`chess/get/board/${localStorage.getItem('board')}`)
      .then((payload) => {
       setBoard(payload.cells);
       setIsActiveBoard(true);
       setLink(`${config.siteURL}board/${payload.uuid}`);
     })
    }
    var socket = io(`${config.socketURL}`,{
      transports: ["websocket"]
    })
    socket.on('messages', (message) => {
      console.log(message);
    });

    socket.on('connect', () => {
        socket.emit(
          'login',
        {
          login: localStorage.getItem('login'),
          sid: socket.sid
        });
    });

    socket.on('update_online_user', (payload) => {
        console.log(payload);
    });

    socket.on('update_board', (payload) => {
      setBoard(payload.cells);
    });



  }, [])


  useEffect(() => { 
    checkMoving();
    getFigures();
  },[activeFigure, activeCell])

  const checkMoving = () => {
    if (activeCell && activeFigure) {
      const data = {
        figure: activeFigure,
        cell: activeCell,
        uuid: localStorage.getItem('board')
      }
      var r = new Request();
      r.post('chess/set/figure',data)
      .then((payload) => {
         setActiveCell(null);
         setActiveFigure(null);
         setBoard(payload.cells);
         getFigures();
     })      
    }
  }

  const handleActiveCell = (id) => {
    setActiveCell(id);
  }
  const handleActiveFigure = (id) => {
    setActiveFigure(id);
  }

  const getFigures = () => {
    var r = new Request();
    r.get('chess/get/figures') 
    .then((payload) => {
      setFigures(payload);
   })
  }

  return (
    <div className="Chess" >
       {
         is_active_board?
         <Grid container>
           <Grid item xs={4}>
            <Figures 
            figures={figures}
            doActiveFigure={handleActiveFigure} />
            {link}
           </Grid>
           <Grid item xs={8}>
            <Board 
            doActiveCell={handleActiveCell}
            id="board" 
            board={board} />
           </Grid>
         </Grid>
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