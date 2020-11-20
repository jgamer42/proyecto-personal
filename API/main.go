package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
	"log"
	"encoding/json"
)


type titular struct{
	id string 
	news_paper string 
	title string 
	link string 
	date string 
}

type allTitular []titular

var titulares = allTitular{
	{	
		id:"grgwg",
		news_paper:"wqdfwf",
		title:"fewfew",
		link:"efewfewf",
		date:"ewefewf",
	},
}

func index(response http.ResponseWriter, request *http.Request){
	fmt.Fprintf(response,"hola mundo")
}

func getTitles(response http.ResponseWriter , request *http.Request){
	json.NewEncoder(response).Encode(titulares)
}

func main(){
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/",index)
	router.HandleFunc("/getTitles",getTitles)
	log.Fatal(http.ListenAndServe(":3000",router))
}