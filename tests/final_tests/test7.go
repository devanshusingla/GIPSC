package main

import "fmt"

func f(i int) (int) {
	var x int = 4
	return 2*i 
}

func main() {
	var a int
	fmt.Scan_int(&a)
	for i := 0; i <= a; i++ {
		x := f(i)
		for j := 0; j <= 2*a; j++ {
			
			if j == 5 {
				continue 
			}

			fmt.Print_int(j)
			
			if j == 7 {
				break
			}
			 
		}

		if x == 4 {
			continue 
		} else {
			if x == 6 {
				break
			}
		}

		fmt.Print_int(x)
	}
}