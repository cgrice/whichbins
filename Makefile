OUT_FILE?=./whichbins.zip
DELIVERABLE=$(abspath $(OUT_FILE))

install:
	pipenv install --three

clean:
	pipenv clean
	rm -f ${DELIVERABLE}

package:
	$(eval VENV = $(shell pipenv --venv))
	cd ${VENV}/lib/python3.7/site-packages && zip -r9 ${DELIVERABLE} ./*
	zip -r9 ${DELIVERABLE} whichbins
	zip -r9j ${DELIVERABLE} bins.json

deploy:
	aws s3 cp whichbins.zip s3://whichbins-artifacts/deploy.zip
	aws lambda update-function-code \
      --function-name whichbins-lambda \
      --s3-bucket whichbins-artifacts \
      --s3-key deploy.zip --region eu-west-1