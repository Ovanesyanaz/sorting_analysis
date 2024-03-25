import React, { useState } from "react";
import { MyButton } from "../components/UI/MyButton.js"
import { useHttp } from "../hooks/http.hook.js"
import { MySortsList } from "../components/MySortsList.js";

export const MainPage = () => {
    const sorts = ["пузырик", "богосорт", "лайнсорт"]
    const {loading, request} = useHttp()
    const [disBtn, setDisBtn] = useState([], {"value" : false})
    const [sortsState, setSortsState] = useState([], ["пузырик", "богосорт", "лайнсорт"])

    const ClickButton = async() => {
        setDisBtn({"value" : true})
        const data = await request("/test", "POST", sortsState)
        console.log(data)
        setSortsState([...data])
        setDisBtn({"value" : false})
    }

    return (
        <>  
            <MySortsList sortsState={sortsState} setSortsState={setSortsState}/>
            <MyButton dissabled = {disBtn} onclk = {ClickButton}/>
        </>
    )
}