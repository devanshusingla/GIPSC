package main

import "fmt"

func main() {
	i := 0
	for i < 14 {
		assign i = i + 1
		if i < 5 {
			continue
		}
		fmt.Print_int(i)
		if i > 8 {
			break
		}
	}
}