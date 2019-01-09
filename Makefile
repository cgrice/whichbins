OUT_FILE?=./whichbins.zip
DELIVERABLE=$(abspath $(OUT_FILE))

install:
	pipenv install --three

clean:
	rm -f ${DELIVERABLE}

package:
	$(eval VENV = $(shell pipenv --venv))
	cd ${VENV}/lib/python3.7/site-packages && zip -r9 ${DELIVERABLE} ./*
	zip -r9 ${DELIVERABLE} whichbins
	zip -r9j ${DELIVERABLE} bins.json