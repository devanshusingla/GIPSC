package main

import "fmt"

func main() {
	if (2 < 3) {
		fmt.Println("Hello")
		if (4 < 5) {
			// do something
			if (5 < 6) {
				// do another thing
			}
		} else if (6 > 9) {
			// don;t stop
		} else {
			if (5 > 0) {
				// enjoy
			}
		}
	} else {
		if (5 > 9) {
			// don't reach here
		}
		// nothing more to do
	}
}