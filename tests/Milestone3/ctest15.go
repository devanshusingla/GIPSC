package main

// import "fmt"

func main() {
	n := 5
	var a [5]int
	for i := 0; i < n; i++ {
		// fmt.Scan_int(&a[i])
	}

	start := 0
	end := n - 1
	key := 8

    for start <= end {
		m := start + ((end-start)/2)
		if a[m] == key {
			// fmt.Print_int(m)
            
		}

		if a[m] < key {
			start = m
		} else {
			end = m - 1
		}
	}
}
