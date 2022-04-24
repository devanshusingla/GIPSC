package fmt

var pre int = 3

func Print_int(a int) {
	__syscall(1, a)
}
func Print_char(a rune) {
	__syscall(11, a)
}
// func Scan_int(a int*){
// 	__syscall()
// }

