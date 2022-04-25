package main

import "fmt"

func f(b *int){
	*b = 20;
}

func main() {
	var a int = 2;
	f(&a);
	fmt.Print_int(a);
	fmt.Print_char(rune(97))
	var b int
	fmt.Scan_int(&b) 
	fmt.Print_int(b)
}