import React, {useState} from 'react';
import TextField from '@mui/material/TextField';

export const MyTextField = (props) => {
  const [value, setValue] = useState([], '')
  const handleChange = (event) => {
      console.log(parseInt(event.target.value), (parseInt(event.target.value) <= props.maxValue), props.maxValue)
      if (
      !isNaN(event.target.value) 
      && (!event.target.value.endsWith(".")) 
      && (!event.target.value.endsWith(" "))
      && (parseInt(event.target.value) <= props.maxValue || event.target.value === ""))
        {
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