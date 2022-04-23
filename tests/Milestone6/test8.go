package main

func f(i int) (int) {
	var x int = 4
	return i + 1
}

func main() {
	var a int = __syscall(5)
	var c int = a + 1
	for i := 0; i <= c; i++ {
		x := f(i)
		if x == 5 {
			continue 
		}
		
		if x == 7 {
			continue
		}

		__syscall(1, x)
	}
}