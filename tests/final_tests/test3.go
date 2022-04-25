package main

import "fmt"

func mult_return(a int, b int) (int, int, int, int, int){
	return a+b, a-b, a%b, a/b, a*b
}

func main() {
	var a, b,c,d,e int
	fmt.Scan_int(&a)
	fmt.Scan_int(&b)
	assign a,b,c,d,e = mult_return(a, b)
	fmt.Print_int(a)
	fmt.Print_int(b)
	fmt.Print_int(c)
	fmt.Print_int(d)
	fmt.Print_int(e)
}