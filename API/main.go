package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

type Task struct {
	ID      int    `json:ID`
	Name    string `json:Name`
	Content string `json:Content`
}

type AllTasks []Task

var tareas = AllTasks{
	{
		ID:      1,
		Name:    "tarea 1",
		Content: "lorem",
	},
}

func indexRoute(response http.ResponseWriter, request *http.Request) {
	response.WriteHeader(http.StatusAccepted)
	fmt.Fprintf(response, "bienvenido")
}
func createTask(response http.ResponseWriter, request *http.Request) {
	var tarea Task
	data, err := ioutil.ReadAll(request.Body)
	if err != nil {
		fmt.Fprintf(response, "algo salio mal")
		log.Fatal("algo salio mal")
	} else {
		json.Unmarshal(data, &tarea)
		tarea.ID = len(tareas) + 1
	}
	tareas = append(tareas, tarea)
	response.Header().Set("Content-Type", "application/json")
	response.WriteHeader(http.StatusCreated)
	json.NewEncoder(response).Encode(tarea)
}

func getTask(response http.ResponseWriter, request *http.Request) {
	json.NewEncoder(response).Encode(tareas)
}

func getOneTask(response http.ResponseWriter, request *http.Request) {
	vars := mux.Vars(request)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		fmt.Fprintf(response, "dato no valido")
	} else {
		for _, tarea := range tareas {
			if tarea.ID == id {
				response.Header().Set("Content-Type", "application/json")
				response.WriteHeader(http.StatusOK)
				json.NewEncoder(response).Encode(tarea)
			} else {
				response.WriteHeader(http.StatusNotFound)
				fmt.Fprintf(response, "tarea no encontrada")
			}
		}
	}

}
func main() {
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", indexRoute).Methods("GET")
	router.HandleFunc("/tareas", getTask).Methods("GET")
	router.HandleFunc("/create", createTask).Methods("POST")
	router.HandleFunc("/get/{id}", getOneTask).Methods("GET")
	log.Fatal(http.ListenAndServe(":3000", router))

}
