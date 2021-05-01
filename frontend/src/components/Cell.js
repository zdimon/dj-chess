import './Cell.css'; 
import React , { useState, useEffect } from 'react';

function Cell(props) {
  const [activeCell, setActiveCell] = useState(null);
  const doActiveCell = (cell) => {
    if(!cell.figure) {
      props.doActiveCell(cell.id);
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