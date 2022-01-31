package main

import "fmt"
func main(){
	var a float64 = 0x0.1p-2
	var b float64 = 0X_1FFFP-16
	var c float32 = 0.15e+0_2
	var d float32 = 072.40
	
	var c1 complex64 = complex(c,d)
	var c2 complex128 = complex(a,b)

	var c3 complex128 = 0o123i

	fmt.Printf("Adding complex numbers %T, %T and %T\n", c1, c2, c3)
<<<<<<< HEAD
	
=======
>>>>>>> yatharth
	var sum = complex128(c1) + c2 + c3
	fmt.Printf("Sum: %T\n", sum)
}