package main

func main() {
	switch x := f(); {
	case x < 0: return -x
	default: return x
	}
}