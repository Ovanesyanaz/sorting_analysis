import React, {useState} from "react"
import { MyTypography } from "./UI/MyTypography"

export const MySort = (props) => {
    console.log(props.name)
    const [checked, setChecked] = useState((props.checkBoxState.filter((ar) => ar === props.name)).length !== 0);
	
	async function handleChange(event) {
		setChecked(!checked)
        if (!checked){
            props.setCheckBoxState([...props.checkBoxState, event.target.name])
        }
        else{
            props.setCheckBoxState(props.checkBoxState.filter((ar) => ar !== event.target.name))
        }
        await props.ClickCheckBox()
        console.log(checked)
        console.log(props.checkBoxState)
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