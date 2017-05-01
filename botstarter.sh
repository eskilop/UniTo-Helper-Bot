while true; do
	python3 main.py & sleep 30m;
	killall python3;
	rm -rf /tmp/*;
done
