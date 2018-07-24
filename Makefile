export PYTHONPATH := python

.PHONY: render
render: site_url := "file:${PWD}/output"
render: clean
	transom --quiet --site-url ${site_url} render --force input output
	transom --quiet --site-url "https://www.ssorj.net/amqp-directory" render --force input docs
	@echo "See the output at ${site_url}/index.html"

.PHONY: clean
clean:
	rm -rf output
	rm -rf python/__pycache__
