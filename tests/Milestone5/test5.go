package main

import "fmt"

func main() {
	var i, j, n , m int;
	var state string;
	var a [5][6]int;
	a [7][2] = 0;
	z := a[7][1] + a[7][0]
	OuterLoop: for i = 0; i < n; i++ {
		for j = 0; j < m; j++ {
			switch a[i][j] {
			case 2:
				state = "Error"
				break OuterLoop
			case 4:
				state = "Found"
				break OuterLoop
			case 6: 
				continue OuterLoop
			}
		}
	}
	state = state
	const x int = 1
	const y int = 2

	var b [2][2][2]int = [2][2][2]int{{{1, 2}, {3,4}},{{5, 6}, {7,8}}}

	var ar [x][y][x+y]int = [x][y][x+y]int{{{1}}}
}