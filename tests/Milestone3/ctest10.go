package main

import "fmt"

func demo(a, b int, c float32) string {
	return "sdfdf"
}
type Address struct {
	name    string
	street  string
	city    string
	state   string
	Pincode int
}

func hello() Address {
	return Address("n", "s", "c", "st", 13244)
}

func main() {
	var a Address = Address("Akshay", "PremNagar", "Dehradun", "Uttarakhand", 252636)
	
	// var a Address
	// a.name = "Akshat"
	// var x *Address = &a
	// (*x).city = "Kanpur"
}
