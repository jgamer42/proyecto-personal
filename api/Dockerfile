FROM golang
WORKDIR /api
COPY . .
RUN go get -u github.com/gorilla/mux
RUN go get go.mongodb.org/mongo-driver/mongo
RUN go build main.go
CMD [ "./main" ]
