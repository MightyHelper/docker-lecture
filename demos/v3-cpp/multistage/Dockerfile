FROM gcc:14 AS build
WORKDIR /app
COPY hello.cpp .
RUN g++ -static -o hello hello.cpp

FROM scratch
COPY --from=build /app/hello /hello
CMD ["/hello"]
