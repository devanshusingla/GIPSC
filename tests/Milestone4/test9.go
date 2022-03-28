package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i         // point to i
	// fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	// fmt.Println(i)  // see the new value of i

	q := &p         // point to j
	*p = **q / *p   // divide j through the pointer
	
	r := &q
	s := ***r / **q
	// fmt.Println(j) // see the new value of j
}
