import React, { useEffect, useState} from "react";
import { MyButton } from "../components/UI/MyButton.js"
import { useHttp } from "../hooks/http.hook.js"
import { MySortsList } from "../components/MySortsList.js";
import { MyDataSelection } from "../components/MyDataSelection.js";

export const MainPage = () => {
    const [iterforbutton, setIterforbutton] = useState([], {"iter" : ""})
    const [imgString, setImgString] = useState([],"")
    const {loading, request} = useHttp()
    const [disBtn, setDisBtn] = useState([], {"value" : false})
    const [sortsState, setSortsState] = useState([], ["quicksort", "booblesort", "insertsort", "selectsort"])
    const [checkBoxState, setCheckBoxState] = useState([], ["quicksort", "booblesort", "insertsort", "selectsort"])
    const [value, setValue] = useState([], {})
    const [inputDataType, setInputDataType] = useState([], '')
    const [inputDataSize, setInputDataSize] = useState([], '')
    const dataType = ["default data","bad data for quicksort", "bad data for mergesort"]
    
    useEffect(()=>{
        //setSortsState(["quicksort", "booblesort", "insertsort", "selectsort"])
        setSortsState(["quick_sort", "merge_sort", "insertion_sort", "bubble_sort"])
        setInputDataSize("1000")
        setValue({})
        setIterforbutton("")
        console.log("hello from useEffect")
        setInputDataType(dataType[0])
    }, [])

    // const ClickButton  = async() => {
    //     setDisBtn({"value" : true})
    //     const data = await request(`/server/get_info_about_sorts/${inputDataType}/${inputDataSize}`, "POST")
    //     setValue([...data.info_about_sorts])
    //     setImgString(data.img_in_bytes)
    //     console.log(data)
    //     setDisBtn({"value" : false})
    // }


    useEffect(() => {
        console.log("useEffect")
        if (iterforbutton.length !== sortsState.length && iterforbutton.length !== 0){
            ClickButton()
        }
        if (iterforbutton.length === sortsState.length && iterforbutton.length !== 0){
            setIterforbutton("")
        }
        // else if (value.length !== 0 && sortsState[value.length] !== undefined){
        //     ClickButton()
        // }


    }, [value])
    

    const ClickButton = async() => {
        setDisBtn({"value" : true})
        setIterforbutton(iterforbutton + 1)
        console.log(value)
        if (value.bubble_sort !== undefined){
            console.log("!=undefined")
            const data = await request(`/server/get_new_graphs/${sortsState[0]}/${inputDataSize}`, "POST", {})
            setValue(data.info_about_sort)
            setImgString(data.img) 
            setDisBtn({"value" : false})
        }
        else{
            console.log("==undefined")
            const data = await request(`/server/get_new_graphs/${sortsState[iterforbutton.length]}/${inputDataSize}`, "POST", {...value})
            setValue(data.info_about_sort)
            setImgString(data.img) 
            setDisBtn({"value" : false})    
        }
    }


    const ClickCheckBox = async() => {
        setImgString("")
        console.log(checkBoxState)
        // const data = await request('/server/chart_update', "POST", {...value})
        // setImgString(data.img_in_bytes)
    }

    return (
        <>
        {(loading) ? (
            <div style={{display:"flex", justifyContent:"center"}}>
                <img 
                    src={`${process.env.PUBLIC_URL}/loading_ytka.gif`}
                    style={{maxWidth: "33%"}}
                    >
                </img>
            </div>
        ) : (
            <p></p>
        )}
        <div style={{display:"flex", justifyContent:"center"}}>  
            <div style={{display:"inline-block", width:"45%", margin:"2%", paddingTop:"1%"}}>
                <MyDataSelection 
                    InputTextFieldLabel="size" 
                    InputTypeLabel="data" 
                    InputSizeLabel="size" 
                    Item={dataType} 
                    setInputDataType={setInputDataType} 
                    setInputDataSize={setInputDataSize}
                    maxValue = {1000000}
                />

                <MyButton 
                    disabled = {disBtn.value} 
                    onclk = {ClickButton}  
                    children = "click for Sorting"
                />

                {(imgString.length === 0) ? (
                    <p></p>
                ) : (
                    <>
                        <MySortsList
                            ClickCheckBox = {ClickCheckBox}
                            setCheckBoxState = {setCheckBoxState} 
                            checkBoxState = {checkBoxState}
                        />
                    </>
                    
                )}
            </div>

                {(imgString.length === 0) ? (
                    <p></p>
                ) : (
                    <div style={{display:"inline-block", width:"45%", margin:"2%"}}>
                        <img alt="" width={"100%"} src={(`data:image/jpg;base64,${imgString}`)} />
                    </div>
                )}


        </div>
        </>
    )
}

// const ClickButton = async() => {
//     setDisBtn({"value" : true})
//     const data = await request("/test", "POST", sortsState)
//     console.log(data)
//     setValue([...data])
//     setSortsState([...data])
//     setDisBtn({"value" : false})
// }

{/* <MySortsList sortsState={sortsState} setSortsState={setSortsState}/>
<MyButton disabled = {disBtn.value} onclk = {ClickButton}/> */}