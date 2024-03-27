import React, {useState, useEffect} from 'react'
import Box from '@mui/material/Box'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select from '@mui/material/Select'

export const MyAutoComplete = (props) => {
    const [value, setValue] = useState([], props.item[0])
    const handleChange = (event) => {
        console.log(props.item)
        setValue(event.target.value)
        props.setInputData(event.target.value)
    };

    return (
        <Box sx={{marginBottom:"1%"}}>
            <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label">{props.InputLabel}</InputLabel>
            <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={value}
                label={props.InputLabel}
                onChange={handleChange}
            >
                {props.item.map((item) =>
                <MenuItem key={item} value={item}>{item}</MenuItem>
                )}
            </Select>
            </FormControl>
        </Box>
    );
}