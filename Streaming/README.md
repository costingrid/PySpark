## logs:
- **structured-streaming**:\
  Reads server access logs from a logs directory and counts the number of appearances of each status code.

- **windowed-streaming**:\
  Reads server access logs from a logs directory and counts the number of requests for each endpoint in the last 60 seconds. Prints the highest 20 counts every 10 seconds.