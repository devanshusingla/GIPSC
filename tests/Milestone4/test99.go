package main

import "fmt"

func main() {
	var i, j, n , m int;
	var state string;
	var a [5][6]int;
	OuterLoop:
	for i = 0; i < n; i++ {
		for j = 0; j < m; j++ {
			switch a[i][j] {
			case 2:
				state = "Error"
				break OuterLoop
			case 4:
				state = "Found"
				break OuterLoop
			}
		}
	}
	fmt.Println(state)
}