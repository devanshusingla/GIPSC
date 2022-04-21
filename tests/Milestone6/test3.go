package main

func inc(x int) (int, int) {
	x = x + 6
	var z int=5
	return z, x+3
}


func main() {
	z,a := inc(5)
	y := 6;
	var x *int = &(y);
	y = 2
	*(&y) = 4
	// &y = x
	var g *int = &y;
	//&(*(&(y))) = &y
	*(&(*(g))) = 7

	var p int = 2
	var a1 int = 5
	var a2 *int = &a1
	var a3 **int = &a2
	var a4 ***int = &a3
	var r ****int = &a4
	***r = &p
	// &(***r) = &a2
}