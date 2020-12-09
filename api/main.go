package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"

	b "./routes"
	"github.com/gorilla/mux"
)

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
		return
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

func deleteTask(response http.ResponseWriter, request *http.Request) {
	vars := mux.Vars(request)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		fmt.Fprintf(response, "dato no valido")
		return
	} else {
		for i, tarea := range tareas {
			if tarea.ID == id {
				response.Header().Set("Content-Type", "application/json")
				response.WriteHeader(http.StatusAccepted)
				tareas = append(tareas[:i], tareas[i+1:]...)
				fmt.Fprintf(response, "eliminado %v", id)
				return
			}
		}
		response.Header().Set("Content-Type", "application/json")
		response.WriteHeader(http.StatusAccepted)
		fmt.Fprintf(response, "tarea no encontrada")
	}
}
func main() {
	/*router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", indexRoute).Methods("GET")
	router.HandleFunc("/tareas", getTask).Methods("GET")
	router.HandleFunc("/create", createTask).Methods("POST")
	router.HandleFunc("/get/{id}", getOneTask).Methods("GET")
	router.HandleFunc("/delete/{id}", deleteTask).Methods("DELETE")
	log.Fatal(http.ListenAndServe(":3000", router))*/
	b.GetAllNews()
}
