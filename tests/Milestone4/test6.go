package main

import "fmt"

func Print(s string) {}

func main() {

	i := "hello"
	// fmt.Print("Write ", i, " as ")
	switch i {
	case "hello":
		Print("hello")
		// fmt.Println("one")
	case "hi":
		Print("hi")
		// fmt.Println("two")
	case "yo":
		Print("yo")
		// fmt.Println("three")
	}
	Print("Hello, 世界")
}
