import React, {useState} from 'react';
import TextField from '@mui/material/TextField';

export const MyTextField = (props) => {
  const [value, setValue] = useState([], '')
  const handleChange = (event) => {
      if (!isNaN(event.target.value) && (!event.target.value.endsWith(".")) && (!event.target.value.endsWith(" "))){
        setValue(event.target.value)
        props.setInputData(event.target.value)
      }
  };
  return (
        <TextField
              sx={{ minWidth: "100%", maxWidth: "100%", marginBottom: "1%"}}
              label={props.name}
              placeholder='1000'
              value={value} 
              onChange={handleChange}
        />
  );
}