package main

// import "fmt"

func ar(v *int) {
	*v = 40
}

func main() {
	var z [5]int = [5]int{1, 2, 4, 5, 5}
	ar(&(z[0]))
}
