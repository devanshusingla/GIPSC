package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

func Print(v Vertex) {}

func main() {
	m := map[string]Vertex {"Bell Labs" : Vertex(40.68433, -74.39967)}
	Print(m["Bell Labs"])
	// fmt.Println(m["Bell Labs"])
}
