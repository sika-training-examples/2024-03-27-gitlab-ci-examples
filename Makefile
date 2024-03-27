generate-pipeline:
	python3 generate-gitlab-ci.py
	git add .gitlab-ci.yml
	git commit -m "ci: Update pipeline"
