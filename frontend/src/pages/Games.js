import React , { useState, useEffect } from 'react';
import Request from '../Request';
import {config} from '../config';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { Link } from "react-router-dom";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ImageIcon from '@material-ui/icons/Image';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import { Redirect } from 'react-router-dom'; 


import {
  BrowserRouter as Router,
} from "react-router-dom";


function Invite(props) {
  
  const join = (id) => {
    var r = new Request();
    r.get(`chess/add/agressor/${id}`).then((payload) => {
      console.log(payload);
      setBoard(payload.uuid);
      localStorage.setItem('board',payload.uuid);
      setRedirect(true);
    })
  }

  useEffect(() => { 
    var r = new Request();
    r.get('chess/games')
    .then((payload) => { 
      console.log(payload);
      setGames(payload);
    })

  }, [])

  const [games, setGames] = useState([]);
  const [board, setBoard] = useState(null);
  const [redirect, setRedirect] = useState(false);
  
  return (
    <div className="Games" >
        {
         redirect? 
         <Redirect to={`/chess`} />
         :
         ''
       }

      <List className="game-list">
       {
         games.map((el) => 
          (
          <ListItem>
            <ListItemAvatar>
              <Avatar>
                <ImageIcon />
              </Avatar>
              {el.agressor}
            </ListItemAvatar>
            <ListItemText primary={el.id} secondary={el.owner} />
            <ListItemSecondaryAction>
              {
                el.agressor?
                ""
                :
                <Button 
                variant="contained" 
                color="secondary" 
                onClick={() => join(el.id) } >
                    Join
                </Button>
              }

            </ListItemSecondaryAction>
          </ListItem>
          
         ))
       }

      
      </List>
      Games


    </div>
  );
}

export default Invite;
