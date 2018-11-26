export PYTHONPATH := python

.PHONY: render
render: site_url := "file:${CURDIR}/output"
render: clean
	python3 -m transom render --quiet --force input output
	python3 -m transom render --quiet --force --site-url "https://amqp.directory" input docs
	@echo "See the output at ${site_url}/index.html"

.PHONY: watch
watch:
	python3 -m transom render --quiet --watch input output

.PHONY: clean
clean:
	rm -rf output
	rm -rf python/__pycache__

.PHONY: update-%
update-%:
	curl "https://raw.githubusercontent.com/ssorj/$*/master/python/$*.py" -o python/$*.py
