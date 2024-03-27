import React from "react"
import { MySort } from "./MySort"
export const MySortsList = (props) => {
    const sorts = ["пузырик", "богосорт", "лайнсорт"]
    return (
        <menu style={{padding:"0", listStyle:"none"}}>
            {sorts.map((sort) =>
                <MySort 
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