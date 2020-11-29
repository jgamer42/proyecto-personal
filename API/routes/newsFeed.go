package routes

import (
	"fmt"
	"os"
)

//GetAllNews ruta encargada de traer todas las noticias
func GetAllNews() {
	uri := os.Getenv("DB_URI")
	fmt.Println("hola mundo")
	fmt.Println(uri)
}
