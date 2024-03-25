import React, { useState } from "react";
import { MyButton } from "../components/MyButton.js"
import { useHttp } from "../hooks/http.hook.js"

export const TestTwoPage = () => {
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
            <p>загрузка Богдана Деева</p>
            <p>клинки на кнопку</p>
            <MyButton onclk = {ClickButton} disabled = {disBtn.value}/>
            {(loading) ? (
                <p>loading...</p>
            ) : (
                <p></p>
            )}
            {(typeof imgString.img_in_bytes === 'undefined') ? (
                <p></p>
            ) : (
                <img alt="" src={(`data:image/jpg;base64,${imgString.img_in_bytes}`)} />
            )}
        </>
    )
}