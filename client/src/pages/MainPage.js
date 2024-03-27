import React, { useEffect, useState } from "react";
import { MyButton } from "../components/UI/MyButton.js"
import { useHttp } from "../hooks/http.hook.js"
import { useLocalStorage } from "../hooks/useLocalStorage.hook.js";
import { MySortsList } from "../components/MySortsList.js";
import { MyDataSelection } from "../components/MyDataSelection.js";

export const MainPage = () => {
    const sorts = ["пузырик", "богосорт", "лайнсорт"]
    const [imgString, setImgString] = useState([],"")
    const [infoAboutSorts, setInfoAboutSorts] = useState([], [])
    const {loading, request} = useHttp()
    const [disBtn, setDisBtn] = useState([], {"value" : false})
    const [sortsState, setSortsState] = useState([], ["пузырик", "богосорт", "лайнсорт"])
    const [value, setValue] = useLocalStorage([], "sorts_data")
    const [inputDataType, setInputDataType] = useState([], '')
    const [inputDataSize, setInputDataSize] = useState([], '')
    const dataType = ["default data","bad data for quicksort", "bad data for mergesort"]
    // const ClickButton = async() => {
    //     setDisBtn({"value" : true})
    //     const data = await request("/test", "POST", sortsState)
    //     console.log(data)
    //     setValue([...data])
    //     setSortsState([...data])
    //     setDisBtn({"value" : false})
    // }
    const ClickButton = async() => {
        setDisBtn({"value" : true})
        const data = await request(`/server/get_info_about_sorts/${inputDataType}/${inputDataSize}`, "POST")
        setValue([...data.info_about_sorts])
        setImgString(data.img_in_bytes)
        console.log(data)
        setDisBtn({"value" : false})
    }

    useEffect(()=>{
        setInputDataSize("1000")
        setInputDataType(dataType[0])
    },[])

    return (
        <div style={{display:"flex", justifyContent:"center"}}>  
            <div style={{display:"inline-block", width:"45%", margin:"2%", paddingTop:"1%"}}>
                <MyDataSelection 
                    InputTextFieldLabel="size" 
                    InputTypeLabel="data" 
                    InputSizeLabel="size" 
                    Item={dataType} 
                    setInputDataType={setInputDataType} 
                    setInputDataSize={setInputDataSize}
                />

                <MyButton 
                    disabled = {disBtn.value} 
                    onclk = {ClickButton}  
                    children = "click for Sorting"
                />

                {(imgString.length === 0) ? (
                    <p></p>
                ) : (
                    <MySortsList
                        setSortsState = {setSortsState} 
                        sortsState = {sortsState}
                    />
                )}
            </div>

                {(loading) ? (
                    <p>loading...</p>
                ) : (
                    <p></p>
                )}
                {(imgString.length === 0) ? (
                    <p></p>
                ) : (
                    <div style={{display:"inline-block", width:"45%", margin:"2%"}}>
                        <img alt="" width={"100%"} src={(`data:image/jpg;base64,${imgString}`)} />
                    </div>
                )}


        </div>
    )
}

{/* <MySortsList sortsState={sortsState} setSortsState={setSortsState}/>
<MyButton disabled = {disBtn.value} onclk = {ClickButton}/> */}