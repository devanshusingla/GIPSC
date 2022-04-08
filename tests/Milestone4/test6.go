package main

import "fmt"

func Print(s string) {}

func main() {

	i := "hello"
	// fmt.Print("Write ", i, " as ")
	switch i {
	case "hello":
		Print("hello")
		break
		// fmt.Println("one")
	case "hi":
		Print("hi")
		break
		// fmt.Println("two")
	case "yo":
		Print("yo")
		break
		// fmt.Println("three")
	}
	Print("Hello, 世界")
}
