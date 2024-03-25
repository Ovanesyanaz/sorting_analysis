import React, {useState} from "react";

export const MyCheckBox = (props) => {
	const [checked, setChecked] = useState(true);
	
	function handleChange(event) {
		setChecked(!checked); // инвертируем стейт
		getName(event)
	}

	function getName(event) {
		console.log(event.target.name)
	}
	
	return (
        <span>
		    <input type="checkbox" name={props.name} checked={checked} onChange={handleChange} />
	    </span>
    )
}