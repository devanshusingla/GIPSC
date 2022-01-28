package main

import "fmt"

func main() {
	// Testing for string literals inside format strings
	fmt.Println("Hello World! -CS335 Project\n\n\x31 Does this thing even work ''\"MikeTesting\" ``\t--")
	var x int = 5
	x++
	fmt.Printf("The value of x: %d\n", x)
	_ = "Random String\n\n"
	y := "ABC!!"
	y = y + ("123" + "1212")
	// Iterating over words // ... /**/
	/*
		This will not give any error/* //
		...$$
	*/
	words := []string{"I", " a\"m", "\ta", " student"}
	var sentence string = ""
	for _, word := range words {
		sentence += word
		x = x/2 + 2/x
	}
	fmt.Println(sentence)
	fmt.Printf("value of x := %d\n", x)

}
