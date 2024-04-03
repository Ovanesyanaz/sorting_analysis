import React from "react"
import { MySort } from "./MySort"
export const MySortsList = (props) => {
    const sorts = props.checkBoxState
    return (
        <menu style={{padding:"0", listStyle:"none"}}>
            {sorts.map((sort) =>
                <MySort 
                    ClickCheckBox = {props.ClickCheckBox}
                    key={sort.toString()} 
                    state={sort} 
                    name={sort} 
                    setCheckBoxState = {props.setCheckBoxState} 
                    checkBoxState = {props.checkBoxState} 
                />
            )}
        </menu>
    )
}