package main

import "fmt"

var a int = 6

func main(){
    var a0 *****int 
    var a1 ****int
    var a2 ***int
    var a3 **int
    var a4 *int
    
	assign a4=&a
    assign a3=&a4
    assign a2=&a3
    assign a1=&a2 
    assign a0=&a1

    assign *****a0=4
    fmt.Print_int(a)
	assign ****a1 = 19
	fmt.Print_int(*****a0)
	assign ***a2 = 21
	fmt.Print_int(*a4)
	assign *a4 = 373
	fmt.Print_int(**a3)
	assign **a3 = 969
	fmt.Print_int(*(&a))
}