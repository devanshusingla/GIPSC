package main

import "fmt"

func main() {
	mylabel : 
	// Testing for string literals inside format strings
	// fmt.Println("Hello World! -CS335 Project\n\n\x31 Does this thing even work ''\"MikeTesting\" ``\t--")
	var x int = 5
	x++
	// fmt.Printf("The value of x: %d\n", x)
	_ = "Random String\n\n"
	y := "ABC!!"
	y = y + ("123" + "1212")
	// Iterating over words // ... /**/
	/*
		This will not give any error/* //
		...$$
	*/
	words := []string{"I", " aFfxhzsgnxhjewmhxmjehxmj", "\ta", " student"}
	var sentence string = ""
	var p int = fmt.pre
	fmt.Println()
	for i, word := range words {
		sentence += word
		i += 7
		x = -x/-2 - -(2/-x)
	}
	mp := map[string]int {"Hello" : 5, "World" : 7}
	sen := ""
	for key, val := range mp {
		val += 5
		sen += key
	}
	// Print(sentence)
	// Print("value of x := %d\n", x)
	if 1 > 2 {
		goto mylabel
	}

}
