package main

import "fmt"

func Print(s string) {}

func main() {

    if 7%2 == 0 {
        Print("7 is even")
    } else {
        Print("7 is odd")
    }

    if 8%4 == 0 {
        Print("8 is divisible by 4")
    }

    if num := 9; num < 0 {
        Print("Num is negative")
    } else if num < 10 {
        Print("Num has 1 digit")
    } else {
        Print("Num has multiple digits")
    }
}