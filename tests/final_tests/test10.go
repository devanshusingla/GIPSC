package main

import "fmt"

func f(a, b int) (int) {
	if a < b {
		return a
	} else {
		return b 
	}
}

func g(a, b int) (int) {
	if a < b {
		return a 
	} else {
		return b
	}
}

func main() {
	var a, b, c int
	fmt.Scan_int(&a)
	fmt.Scan_int(&b)
	fmt.Scan_int(&c)
	minimum := f(1, g(1, 2))
	fmt.Print_int(a)
}