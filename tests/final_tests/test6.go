package main

import "fmt"

func sort(b *int, n int){
	for(i := 0; i < n; i++){
		for(j := i+1; j < n; j++){
			if(b[j] < b[i]){
				assign temp:= b[j]
				assign b[j] = b[i]
				assign b[i] = temp
			}
		}

	}
}


func main() {
	var n int
	fmt.Scan_int(&n)
	var a int[n]
	for(i:=0; i<n; i++){
		fmt.Scan_int(&a[i])
	}
	sort(a,n)
	for(i:=0; i<n; i++){
		fmt.Print_int(a[i])
	}
	

}