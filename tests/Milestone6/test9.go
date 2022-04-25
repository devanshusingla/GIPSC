package main

import "fmt"

func f(b *int){
	*b = 20;
}

func main() {
	// var a int = 2
	// fmt.Print_int(a)
	// var b rune = 'a'
	// fmt.Print_char(b)
	var a int = 2;
	f(&a);
	fmt.Print_int(a);


}