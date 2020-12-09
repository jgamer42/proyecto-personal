package routes

import (
	"context"
	"fmt"
	"log"
	"os"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

//GetAllNews ruta encargada de traer todas las noticias
func GetAllNews() {
	uri := os.Getenv("DB_URI")
	clientOpts := options.Client().ApplyURI(uri)
	client, err := mongo.Connect(context.TODO(), clientOpts)
	if err != nil {
		log.Fatal(err)
	}

	// Check the connections
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Congratulations, you're already connected to MongoDB!")

	collection := client.Database("proyecto").Collection("titulares")
	filter := bson.M{"news_paper": "desde_linux"}
	var post Titular
	err = collection.FindOne(context.TODO(), filter).Decode(&post)
	fmt.Print("prueba ", post.news_paper)
}

type Titular struct {
	date       string `json:date`
	news_paper string `json:news_paper`
	title      string `json:title`
	link       string `json:link`
	_id        string `json:_id`
	sumary     string `json:sumary`
}

func main() {

}
