SHELL:=/bin/bash


build:
	docker build -t barcode_recongizer .

run:
	 docker run --rm -p 8080:8080 --name barcode_recongizer barcode_recongizer
