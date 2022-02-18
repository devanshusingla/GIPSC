package main
import (
    "fmt"

)

func main(){
    var a int = 2 + 3 + 5 + 7;
	var b int = 2 + 3 - 5 + 7;
	var c int = 2 + 3 * 5 + 7;
	var d int = 2 + 3 / 5 + 7;
	var e int = 2 / 3 / 5 / 7;
	var f int = 2 ^ 3 - 5 * 7;
	var g int = 2 << 3 ^ 5 >> 7;
	var h int = 2 &^ 3 / 5 % 7;
	fmt.Println(a, b, c, d, e, f, g, h)
}
