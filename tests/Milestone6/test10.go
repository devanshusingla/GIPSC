package main

func f(a int)(int){
	if a == 0 || a == 1 {
		return 1
	}
	return f(a-2) + f(a-1) 
}

func main() {
	x := f(5)
	__syscall(1, x)
}