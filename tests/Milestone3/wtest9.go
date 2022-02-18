package main

import "fmt"

func main() {
	/*Should be tokenized but not parsed*/
	var x int = 5
	if x == 2 {
		x += 1
	} else {
		x += 1
	} else{
		x+=1
	}

}
