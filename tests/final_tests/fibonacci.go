package main

import "fmt"

func fibonacci(a int) (int){
	if a == 0 || a == 1 {
		return 1
	}
	return fibonacci(a-1)+ fibonacci(a-2)
}

func main() {
	var a int
	fmt.Scan_int(&a)
	b := fibonacci(a)
	fmt.Print_int(b)
}