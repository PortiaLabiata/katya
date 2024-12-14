mkdir ./hello\ current
cd ./hello\ current
echo 'hello current!!' > ./current.txt
cat current.txt
lsattr current.txt | cut -f1 -d' '
