FROM gcc:14
WORKDIR /app
COPY hello.cpp .
RUN g++ -static -o hello hello.cpp
CMD ["./hello"]
