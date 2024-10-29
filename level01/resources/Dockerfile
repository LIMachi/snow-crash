# Use Alpine Linux as a base image
FROM alpine:latest

# Install John the Ripper
RUN apk update && \
    apk add --no-cache john

# Set the working directory
WORKDIR /root

# Create the DES hash file with the given content
RUN echo "flag01:42hDRfypTqqnw" > des-hash.txt

# Default command to run John the Ripper on des-hash.txt and display the results
CMD ["sh", "-c", "john des-hash.txt && cat ~/.john/john.pot"]
