package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

// Definir la estructura del JSON
type Student struct {
    Name      string `json:"student"`
    Age       int    `json:"age"`
    Faculty   string `json:"faculty"`
    Discipline int   `json:"discipline"`
}

func handler(w http.ResponseWriter, r *http.Request) {
    var student Student

    err := json.NewDecoder(r.Body).Decode(&student)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    // Mostrar el resultado en la pantalla del servidor
    fmt.Fprintf(w, "Student: %s, Age: %d, Faculty: %s, Discipline: %d\n", student.Name, student.Age, student.Faculty, student.Discipline)
}

func main() {
    http.HandleFunc("/submit", handler)
    fmt.Println("Server is running on port 8080...")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
