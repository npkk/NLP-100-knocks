# TOO DIFFICULT BECAUSE split COMMAND DON'T HAS ROW-BASED SPLIT FUNCTION.

echo "16.sh > "
read n
# in output, input 15 as n
split -n $n -d input/popular-names.txt output/16-