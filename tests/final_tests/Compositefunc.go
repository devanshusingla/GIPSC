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
	minimum := f(a, g(b, c))
	fmt.Print_int(minimum)
}