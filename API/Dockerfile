FROM golang
WORKDIR /api
COPY . .
RUN go get -u github.com/gorilla/mux
RUN go build main.go
CMD [ "./main" ]
