while true; do
	nc localhost 5000 < /var/log/syslog -w 2
	echo "Sending log to logstash..."
	sleep 5
done
