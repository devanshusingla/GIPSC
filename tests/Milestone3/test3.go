package main

import (
	"fmt"
	"math/rand"
	"time"
)

func getString(length int) string {
	b := make([]byte, length)
	rand.Read(b)
	return fmt.Sprintf("%x", b)[:length]
}

func main() {
	n := 10
	s2i_mp := make(map[string]int)
	i2s_sl := make([]string, n)
	fmt.Println("After declaration..")
	fmt.Println("Length of Map: ", len(s2i_mp))
	fmt.Println("Length of Slice: ", len(i2s_sl), "Capacity of Slice: ", cap(i2s_sl))
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < n; i++{
		i2s_sl[i] = getString(((i+2)*(i+1))/2)
		s2i_mp[i2s_sl[i]] = ((i+2)*(i+1))/2
	}
	fmt.Println("\nAfter storing values..")
	fmt.Println("Length of Map: ", len(s2i_mp))
	fmt.Println("Length of Slice: ", len(i2s_sl), "Capacity of Slice: ", cap(i2s_sl))
	for key, value := range s2i_mp {
		fmt.Println("Key: ", key, "Value: ", value)
	}

	for i := 0; i < n; i++{
		delete(s2i_mp, i2s_sl[i])
		fmt.Println("Deleted key: ", i2s_sl[i], " Value: ", ((i+2)*(i+1))/2)
	}
	fmt.Println("\nAfter deleting key-value pairs from map..")
	fmt.Println("Length of Map: ", len(s2i_mp))
	fmt.Println(`
		Hello, 
		This is a raw string,
		\n\t these don't work
		F
	`)
}
