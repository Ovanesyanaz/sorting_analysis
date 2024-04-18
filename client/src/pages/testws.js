import { MyButton } from "../components/UI/MyButton"
import {request, loading} from "../hooks/http.hook"
import io from 'socket.io-client'
export const TestWs = () => {
    const clickButton = async() => {
        const socket = io("<wss://127.0.0.1:5000>")
        socket.on("echo", (data) => {
            console.log(data)
        })
    }
    return (
        <>
            <MyButton onClick={clickButton}>
                click
            </MyButton>
        </>
    )
}