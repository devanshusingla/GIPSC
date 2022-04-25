package main

import "fmt"

func pointer_check(a *int) {
	assign *a = *a+1
}


func main() {
	var a int
	fmt.Scan_int(&a)
	var b *int = &a
	pointer_check(a)
	fmt.Print_int(a)
	var c **int = &b
	/*Square*/ 
	fmt.Print_int(*b***c)
	/*Cube*/ 
	fmt.Print_int(*b***c*a)

}