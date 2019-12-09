package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Print(err)
	}
	defer file.Close()

	freq := 0

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		inint, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println("shiz")
		}
		freq += inint
	}

	fmt.Println(freq)
}
