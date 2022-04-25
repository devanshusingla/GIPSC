package fmt

var pre int = 3

func Print_int(a int) {
	__syscall(1, a)
}

func Print_char(a rune) {
	__syscall(11, a)
}

func Print_string(a string) {
	__syscall(4, a)
}

func Scan_int(a *int) {
	assign *a = __syscall(5)
}

func Scan_char(a *rune) {
	assign *a = __syscall(12)
}

func Scan_string(a *string) {
	assign *a = __syscall(8)
}

