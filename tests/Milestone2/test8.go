package main
import (
    "fmt"

)

func main(){
    var a *float32 = nil;
	var b *float32 = nil;
	var c float32 = 6;
	c = *b * *((*float32)(a));
	fmt.Println(a, b, c)
}
