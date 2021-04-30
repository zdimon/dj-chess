import './Board.css';
import React from 'react';
import Cell from './Cell';



function Board(props) {
  console.log(props);

  return (
    <div className="Board" >
       {
         props.board? 
         props.board.map((el,index) => <Cell cell={el} />)
         :
         <></>
      }       
    </div>  
  );
}

export default Board;   