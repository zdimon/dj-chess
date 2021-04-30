import React from 'react';
import './Cell.css'; 

function Cell(props) {
  return (
    <div className={`cell bg-${props.cell.color}`} >
      { props.cell.figure ? <img class="chess-figure" src={`/static/images/${props.cell.figure}.svg`} />: ''}
          
    </div>  
  );
}

export default Cell;