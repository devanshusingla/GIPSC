package main

func main() {
	var x int = 5;
	var y *int = &x;
	var z **int = &y;
	**z = 20;
	// *y = 10;
	__syscall(1, x***z)
}