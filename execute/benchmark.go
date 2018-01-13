package main

import (
	"flag"
	"fmt"
	"time"
)

var database = flag.String("db", "hoddb", "Choose database: hoddb, fuseki, allegro, blaze, rdflib, virtuoso")
var query = flag.String("q", "vavenum", "Choose query: vavenum, tempsensor, ahuchildren, spatialmapping, sensorsinrooms, greybox")

func getDatabase(name string) SPARQLEndpoint {
	switch name {
	case "hoddb":
		return newHod()
	case "fuseki":
		return newFuseki()
	case "allegro":
		return newAlegro()
	case "blaze":
		return newBlaze()
	case "rdflib":
		return newRDFlib()
	case "virtuoso":
		return newVirtuoso()
	}
	return newHod()
}

var RUNS = 100

func main() {
	flag.Parse()
	var TIMES = make([]time.Duration, RUNS)

	//h := newHod("http://localhost:47808/api/query")
	//h := newFuseki("http://localhost:3031/berkeley/query")
	//db := newBlaze()
	db := getDatabase(*database)
	db.Init()

	for i := 0; i < RUNS; i++ {
		TIMES[i] = db.DoQuery(SPARQLQUERIES[*query])
		fmt.Println(TIMES[i].Nanoseconds())
	}
}

type SPARQLEndpoint interface {
	Init()
	DoQuery(query string) (reqtime time.Duration)
}
