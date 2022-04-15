run:
	python3 get_addr_bot.py

runbg:
	nohup python3 get_addr_bot.py &
	echo $! > pid

stop:
	kill `cat pid`
	rm -f pid

clean:
	rm -f *.log
	rm -f pid

configure:
	echo '{\n    "token": "<TELEGRAM_TOKEN>",\n    "adm_id": <YOUR_TELEGRAM_ID>,\n    "path_to_ngrok_log": "<path/to/ngrok/log>",\n}' > config.json
	
install:
	pip3 install -r requirements.txt
