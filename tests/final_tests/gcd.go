package main

import "fmt"

func __gcd(a, b int) (int) {
	if a == 0 {
		return b 
	}

	if b == 0 {
		return a
	}

	if a > b {
		return __gcd(a%b, b)
	} else {
		return __gcd(a, b%a)
	}
}

func main() {
	var a, b int 
	fmt.Scan_int(&a)
	fmt.Scan_int(&b)
	fmt.Print_int(__gcd(a, b))
}