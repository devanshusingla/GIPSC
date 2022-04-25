package main

import "fmt"


func main() {
	var n int = 5
	var b [5]int
	for i:=0; i<n; i++ {
		fmt.Scan_int(&b[i])
	}
	for i :=0; i < n; i++{
		for j := i+1; j < n; j++ {
			if b[j] < b[i] {
				temp := b[j]
				assign b[j] = b[i]
				assign b[i] = temp
			}
		}

	}
	for i:=0; i<n; i++{
		fmt.Print_int(b[i])
	}
	

}