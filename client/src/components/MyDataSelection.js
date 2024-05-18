import React from "react"
import { MyAutoComplete } from "../components/UI/MyAutoComplete"
import { MyTextField } from "./UI/MyTextFieldNumber"
export const MyDataSelection = (props) => {
    return(
        <div>
            <MyTextField type="number" name="different values" setInputData={props.setInputDifferentValue} maxValue={props.maxDif}/>
            <MyTextField type="number" name={props.InputTextFieldLabel} setInputData={props.setInputDataSize} maxValue={props.maxValue}/>
        </div>
    )
}