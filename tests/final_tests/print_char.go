package main

import "fmt"

var a int

func main() {
	fmt.Scan_int(&a)
	if a <= 10 {
		if a <= 5 {
			fmt.Print_char('5')
		} else {
			fmt.Print_char('7')
		}
	} else {
		fmt.Print_char('-')
	}
}