import React from "react"
import { MainPage } from "./pages/MainPage"
import { TestTwoPage } from "./pages/TestTwoPage"
function App() {
    
    return (
        <div>
            <MainPage/>
        </div>
    )
}
export default App;

// useEffect(() => {
//     fetch('/get_image')
//     .then(response => response.json())
//     .then(dataa => {
//         setImgString(dataa)
//         console.log(dataa.img_in_bytes)
//     })
// }, [])
