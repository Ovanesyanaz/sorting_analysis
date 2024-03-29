import React from "react"
import { MyAutoComplete } from "../components/UI/MyAutoComplete"
import { MyTextField } from "./UI/MyTextFieldNumber"
export const MyDataSelection = (props) => {
    return(
        <div>
            <MyAutoComplete InputLabel = {props.InputTypeLabel} item = {props.Item} setInputData = {props.setInputDataType}/>
            <MyTextField type="number" name={props.InputTextFieldLabel} setInputData={props.setInputDataSize} maxValue={props.maxValue}/>
        </div>
    )
}