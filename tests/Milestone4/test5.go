package main

import "fmt"



func main() { 
	a := 5
	if a < 5 {
		goto mylabel
	}
	if a > 5 {
		var b int  = 7
	}
	// fmt.Println("Hello World", a)
	mylabel:
	a += 7
	if a > 20 {
		goto mylabel2
	}
	goto mylabel
	mylabel2:;
	// a = 5
	// fmt.Println(a)
}