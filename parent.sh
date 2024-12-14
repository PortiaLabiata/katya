mkdir ../hello\ parent
cd ../hello\ parent
echo 'hello parent!!' > parent.txt
cat parent.txt
lsattr parent.txt | cut -f1 -d' '
