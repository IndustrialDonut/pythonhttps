run_server:
	echo "PIP VENV MUST BE ACTIVATED"
	uwsgi --http-socket 10.0.0.42:5683 --mount /=server_symmetric:app
