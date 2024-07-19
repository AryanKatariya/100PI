#!/bin/bash

read -p "Enter a number: " num

result=1
while [ ${num} -gt 1 ] 
do
	let result=result*num
	let num=num-1
done

echo "result is ${result}"
	
