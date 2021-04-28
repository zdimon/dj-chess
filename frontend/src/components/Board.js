import './Board.css';
import React from 'react';
import Cell from './Cell';
import io from 'socket.io-client'
import {config} from '../config';


function Board(props) {
  console.log(props);
  var socket = io(`${config.backendURL}`)
  console.log(socket);
  return (
    <div className="Board" >
       {props.board.map((el,index) => el.map((e,index) => <Cell cell={e} />)
       )}
    </div>  
  );
}

export default Board;   