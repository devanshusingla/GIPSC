package main

func f(a int, b int)(int, int, int, int, int){
	return a+b, a-b, a*b, a/b, a%b 
}

func main() {
	var a,b,c,d,e int;
	a, b, c, d, e = f(2,3);
	__syscall(1, a)
	__syscall(1, b)
	__syscall(1, c)
	__syscall(1, d) 
	__syscall(1, e)
}