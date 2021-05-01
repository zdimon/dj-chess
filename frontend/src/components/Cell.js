import './Cell.css'; 
import React , { useState, useEffect } from 'react';

function Cell(props) {
  const [activeCell, setActiveCell] = useState(null);
  const doActiveCell = (cell) => {
    if (props.stage === 'setting') {
      if(!cell.figure) {
        props.doActiveCell(cell.id);
      }
    }

    if (props.stage === 'play') {
      if(cell.figure) {
        props.doActiveCell(cell.id);
      } else {
        props.doMove(cell.id);
      }
    }
    
  }
  //console.log(props.cell);

  return (
    <div 
    onClick={() => doActiveCell(props.cell)} 
    className={`cell bg-${props.cell.color} ${ props.cell.id === props.active_cell? "active-cell" : ""}`} >
      { props.cell.figure ? <img class="chess-figure" src={props.cell.figure.figure.get_image_absolute_url} />: ''}
          
    </div>  
  );
}

export default Cell;