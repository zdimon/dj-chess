import React from 'react';
import './Cell.css'; 

function Cell(props) {
  return (
    <div className={`cell ${props.cell.color}`} >
      {props.cell.figure}
    </div>
  );
}

export default Cell;