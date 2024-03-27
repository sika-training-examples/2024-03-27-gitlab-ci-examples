FROM golang:1.21 as build
WORKDIR /build
COPY . .
RUN CGO_ENABLED=0 GOARCH=arm64 go build -o hello main.go

FROM debian:12-slim
WORKDIR /app
COPY --from=build /build/hello .
CMD ["./hello"]