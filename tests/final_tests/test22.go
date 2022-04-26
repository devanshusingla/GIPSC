package main

import "fmt" 

func main() {
	var a int
	fmt.Scan_int(&a)
	
	n, m := 5, 3

	OuterLoop: for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if a == 2 {
				state := 0
				fmt.Print_int(state)
				break OuterLoop
			} else {
				if a == 4 {
					state := 1
					fmt.Print_int(state)
					break OuterLoop
				} else {
					state := 2
					fmt.Print_int(state)
					continue OuterLoop
				}
			}
		}
	}
}