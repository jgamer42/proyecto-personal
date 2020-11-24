package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type titular struct {
	id        string
	newsPaper string
	title     string
	link      string
	date      string
}
type allTitular []titular

var titulares = allTitular{
	{
		id:        "grgwg",
		newsPaper: "wqdfwf",
		title:     "fewfew",
		link:      "efewfewf",
		date:      "ewefewf",
	},
}

func index(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "hola mundo")
}

func getTitles(response http.ResponseWriter, request *http.Request) {
	response.Header().Set("Content-Type", "application/json")
	json.NewEncoder(response).Encode(titulares)
}

func main() {
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", index)
	router.HandleFunc("/getTitles", getTitles)
	log.Fatal(http.ListenAndServe(":3000", router))
}
