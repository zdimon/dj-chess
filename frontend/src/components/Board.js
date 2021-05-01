import './Board.css';
import Cell from './Cell';
import React , { useState, useEffect } from 'react';

function Board(props) {
  const [activeCell, setActiveCell] = useState(null);
  const handelActiveCell = (id) => {
    setActiveCell(id);
    props.doActiveCell(id);
  }

  const handelMove = (id) => {
    props.doMove(id); 
  }

  return (
    <div className="Board" >
       {
         props.board? 
         props.board.map((el,index) => <Cell
         stage={props.stage}
         active_cell={activeCell} 
         doActiveCell={handelActiveCell}
         doMove={handelMove}
         cell={el} />)
         :
         <></>
      }       
    </div>  
  );
}

export default Board;   