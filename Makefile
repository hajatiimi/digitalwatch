DOT = /usr/bin/dot

all: digitalwatch.dot digitalwatch.pdf digitalwatch.png

digitalwatch.dot: digitalwatch.des
	python2 ./des-to-dot.py digitalwatch.des > digitalwatch.dot

digitalwatch.png: digitalwatch.dot
	${DOT} -Tpng < digitalwatch.dot > digitalwatch.png

digitalwatch.pdf: digitalwatch.dot
	${DOT} -Tpdf < digitalwatch.dot > digitalwatch.pdf
