package main

import "fmt"

func Print(s string) {}

func main() {

	i := "hello"
	// fmt.Print("Write ", i, " as ")
	switch i {
	case "hello":
		Print("world")
		break
		// fmt.Println("one")
	case "hi":
		Print("hello")
		break
		// fmt.Println("two")
	case "yo":
		Print("man")
		break
		// fmt.Println("three")
	default:
		Print("Sdf")
		x := 8
		break
	}
	Print("Hello, 世界")
}
