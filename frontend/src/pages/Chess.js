import React , { useState, useEffect } from 'react';
import Request from '../Request';
import Board from '../components/Board';
import io from 'socket.io-client'
import {config} from '../config';
import Button from '@material-ui/core/Button';
import Figures from '../components/Figures';
import './Chess.css'
import Grid from '@material-ui/core/Grid';
import Snackbar from '@material-ui/core/Snackbar';



function Chess() {
  const [is_active_board, setIsActiveBoard] = useState(false);
  const [board, setBoard] = useState([]);
  const [link, setLink] = useState('');
  const [openSnack, setOpenSnack] = useState(false);
  const [snackMessage, setSnackMessage] = useState('');
  const [activeCell, setActiveCell] = useState(null);
  const [activeFigure, setActiveFigure] = useState(null);
  const [figures, setFigures] = useState([]);
  const [stage, setStage] = useState('setting');
  


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
       setStage(payload.stage);
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

    socket.on('update_stage', (payload) => {
      setStage(payload.stage);
      setOpenSnack(true);
      setSnackMessage('Game started. Good luck!')
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
         console.log(payload);
         if(payload.status === 0) {
         setActiveCell(null);
         setActiveFigure(null);
         setBoard(payload.payload.cells);
         getFigures(); 
         } else {
           setOpenSnack(true);
           setSnackMessage(payload.message);
         }
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

  const handleCloseSnackbar = () => {
    setOpenSnack(false);
  }

  const handleMove = (id) => {
    console.log('Moving!!!!');
    console.log(activeCell);
    console.log(id);
    const data = {
      from: activeCell,
      to: id,
      board: localStorage.getItem('board')
    }
    var r = new Request();
    r.post('chess/move/figure',data) 
    .then((payload) => {
      console.log(payload);
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
            <p>
              Link: {link}
            </p>
            <p>
              Stage: {stage}
            </p>
           </Grid>
           <Grid item xs={8}>
            <Board 
            doActiveCell={handleActiveCell}
            doMove={handleMove}
            id="board" 
            stage={stage}
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
      <Snackbar
        anchorOrigin={{
          vertical: 'center',
          horizontal: 'center',
        }}
        open={openSnack}
        autoHideDuration={3000}
        onClose={handleCloseSnackbar}
        message={snackMessage}
      />
    </div> 
  );
}

export default Chess;