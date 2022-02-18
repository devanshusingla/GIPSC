package main

import "fmt"

func main() {
	var num int = 1

	for num < 10 {
		if num%2 == 0 {
			num++
			goto labeljump
		}
		fmt.Println("\n Num has value set to %d", num)
		num++
	}

labeljump:
	fmt.Println("\nFinal value of num is %d", num)
}