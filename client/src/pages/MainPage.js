import React, { useState } from "react";
import { MyButton } from "../components/MyButton.js"
import { MyTypography } from "../components/MyTypography.js"
import { useHttp } from "../hooks/http.hook.js"

export const MainPage = () => {
    const sorts = ["пузырик", "богосорт", "лайнсорт"]

    const [imgString, setImgString] = useState([{}])
    const {loading, request} = useHttp()
    const [disBtn, setDisBtn] = useState([], {"value" : false})

    const ClickButton = async() => {
        setDisBtn({"value" : true})
        const data = await request("/get_image", "POST")
        console.log(data)
        setImgString(data)
        setDisBtn({"value" : false})
    }
    return (
        <>  
        </>
    )
}