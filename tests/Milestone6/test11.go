package main

func main() {
	var x int = 5
	if x == 5 {
		__syscall(1, 10)
		x = 7
	}

	if x == 7 {
		__syscall(1, 14)
		x = 9  
	}
	
	if x == 3 || x == 3*3 {
		__syscall(1, 90)
		x = 40
	}

	if x == 40 && x == 90 {
		__syscall(1, 45) 
	} else {
		__syscall(1, 100)
	}
}