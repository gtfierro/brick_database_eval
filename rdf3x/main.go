package main

import (
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
)

func main() {

	http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
		defer r.Body.Close()
		query, err := ioutil.ReadAll(r.Body)
		if err != nil {
			log.Println(err)
			w.WriteHeader(500)
			w.Write([]byte(err.Error()))
			return
		}
		log.Println("query", string(query))
		qfile, err := ioutil.TempFile(".", "q")
		if err != nil {
			log.Println(err)
			w.WriteHeader(500)
			w.Write([]byte(err.Error()))
			return
		}
		_, err = qfile.Write([]byte(query))
		if err != nil {
			log.Println(err)
			w.WriteHeader(500)
			w.Write([]byte(err.Error()))
			return
		}
		cmd := exec.Command("bin/rdf3xquery", "berkeley", qfile.Name())
		output, err := cmd.Output()
		if err != nil {
			log.Println(err)
			w.WriteHeader(500)
			w.Write([]byte(err.Error()))
			return
		}
		w.Write(output)

	})
	log.Fatal(http.ListenAndServe(":8080", nil))
}
