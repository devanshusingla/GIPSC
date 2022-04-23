package main

func main() {
	var x int = 5
	if x == 5 {
		__syscall(1, 10)
		x = 7
	}

	if x == 7 {
		__syscall(1, 14)
	}
}