import './Cell.css'; 
import React , { useState, useEffect } from 'react';

function Cell(props) {
  const [activeCell, setActiveCell] = useState(null);
  const doActiveCell = (id) => {
    props.doActiveCell(id);
  }


  return (
    <div 
    onClick={() => doActiveCell(props.cell.id)} 
    className={`cell bg-${props.cell.color} ${ props.cell.id === props.active_cell? "active-cell" : ""}`} >
      { props.cell.figure ? <img class="chess-figure" src={`/static/images/${props.cell.figure}.svg`} />: ''}
          
    </div>  
  );
}

export default Cell;