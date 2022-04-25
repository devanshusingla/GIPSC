package main

func f()(float32, int){
	return 2.0, 4
}

func g() float32 {
	return 6.43
}

func main() {
	z, a := f()
	z += 1.0
	// a *= 5
	// z /= g()
	__syscall(2, z)
	if z >= 4.0 {
		__syscall(1, 5)
	} else {
		__syscall(1, 4)
	}
}