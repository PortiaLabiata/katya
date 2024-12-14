mkdir /tmp/hello\ world
touch /tmp/hello\ world/absolute.txt
echo 'hello world!!' > /tmp/hello\ world/absolute.txt
cat /tmp/hello\ world/absolute.txt
lsattr /tmp/hello\ world/absolute.txt | cut -f1 -d' '
