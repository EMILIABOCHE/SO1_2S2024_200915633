# Build stage
FROM golang:1.17-alpine AS builder
WORKDIR /app
COPY . .
RUN go mod init myapp && go build -o myapp .

# Final stage
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/myapp .
EXPOSE 8080
CMD ["./myapp"]
