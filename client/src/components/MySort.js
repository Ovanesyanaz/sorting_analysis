import React, {useState} from "react"
import { MyTypography } from "./UI/MyTypography"

export const MySort = (props) => {
    const [checked, setChecked] = useState((props.sortsState.filter((ar) => ar === props.name)).length !== 0);
	
	async function handleChange(event) {
		setChecked(!checked)
        if (!checked){
            props.setSortsState([...props.sortsState, event.target.name])
        }
        else{
            props.setSortsState(props.sortsState.filter((ar) => ar !== event.target.name))
        }
        await props.ClickCheckBox()
        console.log(checked)
        console.log(props.sortsState)
        setChecked(checked)
	}

    return (
        <li style={{display:"flex"}}>
            <MyTypography state = {props.state}/>
		    <input 
            style={{margin:"1%"}} 
            type="checkbox" 
            name={props.name} 
            checked={checked} 
            onChange={handleChange} 
            />
        </li>
    )
}