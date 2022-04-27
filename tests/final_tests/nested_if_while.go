package main

import "fmt"

func main() {
	var x int
	fmt.Scan_int(&x)
	if x > 0 {
		assign x = 7
		if x/3 < 9 {
			i:=0
			for(i<10){
				fmt.Print_int(i)
				i++
			}

		}else{
			if x > 1{
				fmt.Print_int(100)
			}
		}
	} else {
		fmt.Print_int(x + 5)
	}
}