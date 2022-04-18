package main

import "fmt"

// func df () int {
// 	if( 1 < 2) {
// 		d := 5
// 		if 5 < 7 {
// 			g := 5
// 		}
// 		return 7
// 	}
// }

func x() int {
	e0 := 6
	if ( 2 < 4) {
		e1 := 4
		return 5
	} else {
		e2 := 6
		return 6
	}
}

func dummy() int {
	out:
	s1 := 5
	if (1 < 2) {
		s2 := 5
		if (3 > 4) {
			s3 := 5
			goto out;
		}
		return 5
	} else {
		s4 := 6
		if (5 < 4) {
			s5 := 5
			return 7
		} else {
			s6 := 7
			return 9
		}
		// return 6
	}
}

func main() {
	f := 6
	var t int  = dummy()
	z := dummy()
}