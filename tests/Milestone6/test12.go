package main



func main() {
	var x int = 5
	if x == 5 {
		__syscall(1, 10)
		x = 7
		if x/3 < 9 {
			i:=0
			for(i<10){
				__syscall(1, i)
				i+=1
			}

		}else{
			if x > 1{
				__syscall(1,100)
			}
		}
	}

}