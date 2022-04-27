package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan_int(&a) 
	fmt.Scan_int(&b)
	c := 2*a + 1
	d := 2*a + 2
	e := 2*a + 3
	f := 2*a + 4
	switch b {
		case c:
			fmt.Print_char('a')
		case d:
			fmt.Print_char('b') 
		case e:
			fmt.Print_char('c')
		case f:
			fmt.Print_char('d')
	}
}