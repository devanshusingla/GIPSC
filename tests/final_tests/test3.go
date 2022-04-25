package main

<<<<<<< HEAD
import "fmt"

func mult_return(a int, b int) (int, int, int, int, int){
	return a+b, a-b, a%b, a/b, a*b
}

func main() {
	var a, b,c,d,e int
	fmt.Scan_int(&a)
	fmt.Print_int(&b)
	assign a,b,c,d,e = mult_return(a, b)
	fmt.Print_int(a)
	fmt.Print_int(b)
	fmt.Print_int(c)
	fmt.Print_int(d)
	fmt.Print_int(e)
=======
func f(a int, b int)(int, int, int, int, int){
	return a+b, a-b, a*b, a/b, a%b 
}

func main() {
	var a,b,c,d,e int;
	assign a, b, c, d, e = f(2,3);
	__syscall(1, a)
	__syscall(1, b)
	__syscall(1, c)
	__syscall(1, d) 
	__syscall(1, e)
>>>>>>> 31a3fe9b3cf2015271f281243439faac71dd7ab7
}