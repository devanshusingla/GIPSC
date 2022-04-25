package main

import "fmt"

func arglist(a int, b int, c int, d int, e int, f int, g int, h int) {
	fmt.Print_int(a)
	fmt.Print_int(b)
	fmt.Print_int(c)
	fmt.Print_int(d)
	fmt.Print_int(e)
	fmt.Print_int(f)
	fmt.Print_int(g)
	fmt.Print_int(h)
}

func main() {
	arglist(1, 2, 3, 4, 5, 6, 7, 8)
}