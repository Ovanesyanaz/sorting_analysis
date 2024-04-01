import React from "react"
import { MySort } from "./MySort"
export const MySortsList = (props) => {
    console.log(props.sortsState, "props.sortsState")
    const sorts = props.sortsState
    return (
        <menu style={{padding:"0", listStyle:"none"}}>
            {sorts.map((sort) =>
                <MySort 
                    ClickCheckBox = {props.ClickCheckBox}
                    key={sort.toString()} 
                    state={sort} 
                    name={sort} 
                    setSortsState = {props.setSortsState} 
                    sortsState = {props.sortsState} 
                />
            )}
        </menu>
    )
}