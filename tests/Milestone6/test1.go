package main

func add (a, b int) (int, int) {
	return a+b, a-b
}

func main() {
	y := 6;
	var x *int = &(y);
	y = 2
	*x, y = add(7, 11)
}