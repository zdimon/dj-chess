import './Board.css';
import React from 'react';
import Cell from './Cell';



function Board(props) {
  console.log(props);
  return (
    <div className="Board" >
       {props.board.map((el,index) => el.map((e,index) => <Cell cell={e} />)
       )}
    </div>  
  );
}

export default Board;   