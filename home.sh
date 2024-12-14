mkdir $HOME/hello\ home/
echo 'hello home!!' > $HOME/hello\ home/home.txt
cat $HOME/hello\ home/home.txt
lsattr $HOME/hello\ home/home.txt | cut -f1 -d' '
