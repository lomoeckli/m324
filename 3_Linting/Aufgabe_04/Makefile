.PHONY: run

run:
	docker run --rm \
		-e SONAR_HOST_URL="http://sonarqube:9000" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=exercise4" \
		-e SONAR_TOKEN="squ_4d120d8e603af7cbdf114b44e933aeadd336683c" \
		--network sonar-net \
		-v .:/usr/src \
		-u $(id -u):$(id -g) \
		sonarsource/sonar-scanner-cli