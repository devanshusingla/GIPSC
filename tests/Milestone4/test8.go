package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

func Print(v Vertex) {}

func main() {
	m := map[string]Vertex {"Bell Labs" : Vertex(40.68433, -74.39967)}
	a := Vertex(69.012312, 69.696969)
	c := 4
	Print(m["Bell Labs"])
	// fmt.Println(m["Bell Labs"])
}
