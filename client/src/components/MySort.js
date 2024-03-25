import React, {useState} from "react";
import { MyTypography } from "./UI/MyTypography"

export const MySort = (props) => {
    const [checked, setChecked] = useState(false);
	
	function handleChange(event) {
		setChecked(!checked) // инвертируем стейт
        let arr = props.sortsState
        console.log(props.sortsState)
        console.log(event.target.name)
        if (!checked){
            props.setSortsState([...arr, event.target.name])
        }
        else{
            props.setSortsState(arr.filter((ar) => ar != event.target.name))
        }
        
	}

    return (
        <li>
            <MyTypography state = {props.state}/>
		    <input type="checkbox" name={props.name} checked={checked} onChange={handleChange} />
        </li>
    )
}