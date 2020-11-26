package main

import (
	"fmt"
	"net/http"
)

func newsFeed(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "hola mundo")
}
