package main

import "fmt"

type point struct {
	x int
	y int
	e int
	fg int
	o int
}

func ars(v []point){
	(v[0]).x = 6
}

func ar(v point, x int) {
	v.y = 40
}

func main() {
	var s string = "sdfsdfd"
	var aa rune = 'a'
	var t int  = 5
	var r int = -t
	var d point = point(4, 5,6 ,2 ,6)
	x := 2
	z := 3
	y := z
	ar(point(4, 5,6 ,2 ,6), x + y)
	var arr []point = []point{d}
	ars(arr)
}
