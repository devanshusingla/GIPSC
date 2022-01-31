/***************************************************
			Sample go program for testing Runes ♛
***************************************************/
package main

import (
	"fmt"
)

// main function
func main() {

	slc := []rune{'x', '本', '\a', '\t', '\057', '\x32', '\u56ff', '\U000130B8', '\U0001f437'}
	for i, value := range slc{
		fmt.Printf("\nSymbol: %c, Unicode value: %U, index: %d", value, value, i);
	}
}