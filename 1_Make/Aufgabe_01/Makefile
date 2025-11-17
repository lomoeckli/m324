all: ip host address
ip:
	echo "$(shell hostname -I | awk '{print $$1}')" > ip
host:	
	echo "$$(hostname)" > host
address: ip host
	echo "$$(cat host)@$$(cat ip)" > address
clean:
	rm -f ip host address