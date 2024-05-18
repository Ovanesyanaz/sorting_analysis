import React, { useEffect, useState} from "react";
import { MyButton } from "../components/UI/MyButton.js"
import { useHttp } from "../hooks/http.hook.js"
import { MySortsList } from "../components/MySortsList.js";
import { MyDataSelection } from "../components/MyDataSelection.js";
import { TextAboutSortingPage } from "./TextAboutSortingPage.js";
import { io } from "socket.io-client"
let socket;

export const MainPage = () => {
    const [iterforbutton, setIterforbutton] = useState([], {"iter" : ""})
    const [imgString, setImgString] = useState([],"")
    const [isOpenInfoPage, setIsOpenInfoPage] = useState([], false)
    const [amount, setAmount] = useState([], 0)
    const {loading, request} = useHttp()
    const [disBtn, setDisBtn] = useState([], false)
    const [sortsState, setSortsState] = useState([], ["quicksort", "booblesort", "insertsort", "selectsort"])
    const [checkBoxState, setCheckBoxState] = useState([], ["quicksort", "booblesort", "insertsort", "selectsort"])
    const [value, setValue] = useState([], {})
    const [inputDataType, setInputDataType] = useState([], '')
    const [inputDifferentValue, setInputDifferentValue] = useState([], '')
    const [inputDataSize, setInputDataSize] = useState([], '')
    const dataType = ["default data","bad data for quicksort", "bad data for mergesort"]

    useEffect(() => {
        setIsOpenInfoPage(false)
        setAmount(0)
        setSortsState(["quick_sort", "merge_sort", "insertion_sort", "bubble_sort"])
        setCheckBoxState(["quick_sort", "merge_sort", "insertion_sort", "bubble_sort"])
        setInputDataSize("1000")
        setInputDifferentValue("100")
        setDisBtn(false)
        setValue({})
        setIterforbutton("")
        console.log("hello from useEffect")
        setInputDataType(dataType[0])
    }, [])

    useEffect(() => {
        socket = io();

        socket.on("chat", (data) => {
            console.log(data)
            if (data.isEnd){
                setDisBtn(false)
            }
            setValue(data.info_about_sort)
            setImgString(data.img)
        })
        return (() => {
            socket.disconnect()
        })

    }, [])

    const get_old_graphs = async() => {
        let b = new Set(checkBoxState)
        let a = [...new Set(sortsState.filter(x => b.has(x)))]
        const data = await request(`/server/get_old_graphs/${inputDataSize}`, "POST", {value, a})
        setImgString(data.img)
    }

    useEffect(() =>{
        if (imgString.length !== 0){
            get_old_graphs()
        }
    }, [checkBoxState])


    // useEffect(() => {
    //     console.log("useEffect")
    //     if (iterforbutton.length !== sortsState.length && iterforbutton.length !== 0){
    //         ClickButton()
    //     }
    //     if (iterforbutton.length === sortsState.length && iterforbutton.length !== 0){
    //         setIterforbutton("")
    //     }


    // }, [value])


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

    const getWS = () => {
        setDisBtn(true)
        socket.emit("chat", {dataSize: inputDataSize, sorts:checkBoxState, dataDifValue: inputDifferentValue})
    }

    const ClickCheckBox = async() => {
        console.log(checkBoxState)
    }

    const ChangeOpen = () => {
        setIsOpenInfoPage(!isOpenInfoPage)
        setImgString("")
    }

    return (
        <div style={{display:"flex", justifyContent:"center"}}>  
            {(!isOpenInfoPage) ? (
            <div style={{display:"inline-block", width:"45%", margin:"2%", paddingTop:"1%"}}>
            {/* {(imgString.length === 0) ? (
                <p></p>
            ) : (
                <div style={{display:"inline-block", width:"45%", margin:"2%", marginTop:"0%"}}>
                    <img alt="" width={"100%"} src={(`data:image/jpg;base64,${imgString}`)} />
                </div>
            )} */}
            <MyDataSelection 

                InputTextFieldLabel="size" 
                InputTypeLabel="data" 
                InputSizeLabel="size" 
                Item={dataType} 
                setInputDifferentValue={setInputDifferentValue}
                maxDif={10000}
                setInputDataType={setInputDataType}
                setInputDataSize={setInputDataSize}
                maxValue = {100000}
            />

            <MyButton
                disabled = {disBtn}
                onclk = {getWS}
                children = "click for Sorting"
            />


            <MyButton
                disabled = {disBtn}
                onclk = {ChangeOpen}
                children = "click for get info about sorting"
            />

            <MySortsList
                style={{}}
                ClickCheckBox = {ClickCheckBox}
                setCheckBoxState = {setCheckBoxState} 
                checkBoxState = {checkBoxState}
                sortsState = {sortsState}
            />
        </div>
                ) : (
                    <div>
                        <TextAboutSortingPage btnFunc = {ChangeOpen}>

                        </TextAboutSortingPage>
                    </div>
                )}
        
        {(imgString.length === 0) ? (
                <p></p>
            ) : (
                <div style={{display:"inline-block", width:"45%", margin:"2%", marginTop:"0%"}}>
                    <img alt="" width={"100%"} src={(`data:image/jpg;base64,${imgString}`)} />
                </div>
            )}
        </div>
    )
}
