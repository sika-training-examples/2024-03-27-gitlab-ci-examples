# .gitlab-ci.yml

image: golang:1.22-bullseye

build:
  parallel:
    matrix:
      - GOOS:
          - linux
          - darwin
          - windows
        GOARCH:
          - amd64
          - arm64
  artifacts:
    paths:
      - hello-${GOOS}-${GOARCH}
  script:
    - go build -o hello-${GOOS}-${GOARCH} main.go
