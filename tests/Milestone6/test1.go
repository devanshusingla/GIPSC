package main

func add (a, b int) (int, int) {
	return a+b, a-b
}

func main() {
	y := 6;
	var x *int = &(y);
	y = 2
	// var z int = 5
	z, w := add(7, 11)
}