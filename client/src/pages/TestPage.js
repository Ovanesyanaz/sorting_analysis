import React, { useState } from "react";
import { MyButton } from "../components/UI/MyButton.js"
import { MyTextField} from "../components/UI/MyTextField.js"
import { useHttp } from "../hooks/http.hook.js"

export const TestPage = () => {
    const {request} = useHttp()
    const [numbers, setNumbers] = useState([], ["0", "0"])
    const [amount, setAmount] = useState([], "")
    const ChangeFirst = (event) => {
        setNumbers([event.target.value, numbers[1]])
        console.log(numbers)
    }
    const ChangeSecond = (event) => {
        setNumbers([numbers[0], event.target.value])
        console.log(numbers)
    }
    const ClickButton = async() => {
        try{
            const answ = await request("/test", "POST", numbers)
            setAmount(answ.answ)
            console.log("data from server ", answ)
        }
        catch(e){
            console.log(e.message)
        }

    }
    return (
        <>  
            <MyTextField onChange = {ChangeFirst} value = {numbers[0]}/>
            <MyTextField onChange = {ChangeSecond} value = {numbers[1]}/>
            <MyButton onclk = {ClickButton}/>
            {(typeof amount === "") ? (
            <p></p>
            ):(
            <p>{amount}</p>

            )}
        </>
    )
}