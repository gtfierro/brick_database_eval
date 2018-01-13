package main

import (
	"github.com/parnurzeal/gorequest"
	"log"
	"os/exec"
	"strings"
	"time"
)

type hoddb struct {
	url string
	req *gorequest.SuperAgent
}

func newHod() *hoddb {
	return &hoddb{}
}

func (h *hoddb) Init() {
	h.url = "http://localhost:47808/api/query"
	//cmd := exec.Command("/bin/bash", "-c", "docker pull gtfierro/paperhod ; docker kill paperhod ; docker rm paperhod ; docker run -d --name paperhod -p47808:47808 gtfierro/paperhod")
	cmd := exec.Command("/bin/bash", "-c", "docker kill paperhod ; docker rm paperhod ; docker run -d --name paperhod -p47808:47808 gtfierro/paperhod")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(string(out), err)
	}
	h.req = gorequest.New()
	time.Sleep(10 * time.Second)
}

func (h *hoddb) DoQuery(query string) (reqtime time.Duration) {
	var newparts []string
	parts := strings.Split(query, "\n")
	for _, part := range parts {
		if !strings.Contains(part, "PREFIX") {
			newparts = append(newparts, part)
		}
	}
	query = strings.Join(newparts, "\n") + ";"

	t1 := time.Now()
	_, _, errs := h.req.Post(h.url).Type("text").Send(query).End()
	t := time.Since(t1)
	if len(errs) > 0 {
		log.Println(errs)
	}
	return t
}

type fuseki struct {
	url string
	req *gorequest.SuperAgent
}

func newFuseki() *fuseki {
	return &fuseki{}
}

func (f *fuseki) Init() {
	f.url = "http://localhost:3031/berkeley/query"
	//cmd := exec.Command("/bin/bash", "-c", "docker pull gtfierro/fuseki ; docker kill fuseki ; docker rm fuseki ; docker run -d --name fuseki -p3031:3030 gtfierro/fuseki")
	cmd := exec.Command("/bin/bash", "-c", "docker kill fuseki ; docker rm fuseki ; docker run -d --name fuseki -p3031:3030 gtfierro/fuseki")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(string(out), err)
	}
	f.req = gorequest.New()
	time.Sleep(20 * time.Second)
}

func (f *fuseki) DoQuery(query string) (reqtime time.Duration) {
	t1 := time.Now()
	_, _, errs := f.req.Post(f.url).Param("query", query).End()
	t := time.Since(t1)
	if len(errs) > 0 {
		log.Println(errs)
	}
	return t
}

type alegro struct {
	url string
	q   map[string]interface{}
	req *gorequest.SuperAgent
}

func newAlegro() *alegro {
	return &alegro{
		q: make(map[string]interface{}),
	}
}

func (a *alegro) Init() {
	a.url = "http://localhost:10035/repositories/berkeley/sparql"
	//cmd := exec.Command("/bin/bash", "-c", "docker pull gtfierro/alegrograph ; docker kill alegrograph ; docker rm alegrograph ; docker run -d --name alegrograph -p10035:10035 gtfierro/alegrograph")
	cmd := exec.Command("/bin/bash", "-c", "docker kill alegrograph ; docker rm alegrograph ; docker run -d --name alegrograph -p10035:10035 gtfierro/alegrograph")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(string(out), err)
	}
	a.req = gorequest.New()
	time.Sleep(10 * time.Second)
}

func (a *alegro) DoQuery(query string) (reqtime time.Duration) {
	a.q["query"] = query
	t1 := time.Now()
	_, _, errs := a.req.Post(a.url).SetBasicAuth("root", "asdfasdf").Param("query", query).End()
	t := time.Since(t1)
	if len(errs) > 0 {
		log.Println(errs)
	}
	return t
}

type blaze struct {
	url string
	req *gorequest.SuperAgent
}

func newBlaze() *blaze {
	return &blaze{}
}

func (b *blaze) Init() {
	b.url = "http://localhost:9998/blazegraph/sparql"
	//cmd := exec.Command("/bin/bash", "-c", "docker pull gtfierro/blazegraph ; docker kill blazegraph ; docker rm blazegraph ; docker run -d --name blazegraph -p9998:9998 gtfierro/blazegraph")
	cmd := exec.Command("/bin/bash", "-c", "docker kill blazegraph ; docker rm blazegraph ; docker run -d --name blazegraph -p9998:9998 gtfierro/blazegraph")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(string(out), err)
	}
	b.req = gorequest.New()
	time.Sleep(10 * time.Second)
}

func (b *blaze) DoQuery(query string) (reqtime time.Duration) {
	t1 := time.Now()
	_, _, errs := b.req.Post(b.url).Param("query", query).End()
	t := time.Since(t1)
	if len(errs) > 0 {
		log.Println(errs)
	}
	return t
}

type rdflib struct {
	url string
	q   map[string]interface{}
	req *gorequest.SuperAgent
}

func newRDFlib() *rdflib {
	return &rdflib{
		q: make(map[string]interface{}),
	}
}

func (r *rdflib) Init() {
	r.url = "http://localhost:8082/query"
	//cmd := exec.Command("/bin/bash", "-c", "docker pull gtfierro/rdflib ; docker kill rdflib ; docker rm rdflib ; docker run -d --name rdflib -p8082:8081 gtfierro/rdflib")
	cmd := exec.Command("/bin/bash", "-c", "docker kill rdflib ; docker rm rdflib ; docker run -d --name rdflib -p8082:8081 gtfierro/rdflib")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(string(out), err)
	}
	r.req = gorequest.New()
	time.Sleep(10 * time.Second)
}

func (r *rdflib) DoQuery(query string) (reqtime time.Duration) {
	r.q["query"] = query
	t1 := time.Now()
	_, _, errs := r.req.Post(r.url).Send(r.q).End()
	t := time.Since(t1)
	if len(errs) > 0 {
		log.Println(errs)
	}
	return t
}

type virtuoso struct {
	url string
	req *gorequest.SuperAgent
}

func newVirtuoso() *virtuoso {
	return &virtuoso{}
}

func (v *virtuoso) Init() {
	v.url = "http://localhost:8890/sparql"
	//cmd := exec.Command("/bin/bash", "-c", "docker pull gtfierro/virtuoso ; docker kill virtuoso ; docker rm virtuoso ; docker run -d --name virtuoso -p8890:8890 gtfierro/virtuoso")
	cmd := exec.Command("/bin/bash", "-c", "docker kill virtuoso ; docker rm virtuoso ; docker run -d --name virtuoso -p8890:8890 gtfierro/virtuoso")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(string(out), err)
	}
	v.req = gorequest.New()
	time.Sleep(10 * time.Second)
}

func (v *virtuoso) DoQuery(query string) (reqtime time.Duration) {
	t1 := time.Now()
	_, _, errs := v.req.Post(v.url).Param("query", query).End()
	t := time.Since(t1)
	if len(errs) > 0 {
		log.Println(errs)
	}
	return t
}
