package main

// import "fmt"

type Address struct {
	name    string
	street  string
	city    string
	state   string
	Pincode int
}

func main() {
	// var a = Address{"Akshay", "PremNagar", "Dehradun", "Uttarakhand", 252636}
	var a Address
	a.name = "Akshat"
	var x *Address = &a
	(*x).city = "Kanpur"
}
