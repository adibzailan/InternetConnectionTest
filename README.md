# InternetConnectionTest

InternetConnectionTest is a Python script that measures and categorizes your internet connection speed using the Speedtest.net infrastructure.

## Features

- Measures download and upload speeds
- Calculates ping
- Categorizes speeds as "Bad", "Normal", or "Good"
- Provides clear, formatted output of results

## Requirements

- Python 3.x
- speedtest-cli library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/adibzailan/internet_connection_test.git
   ```

2. Navigate to the project directory:
   ```
   cd internet_connection_test
   ```

3. Install the required package:
   ```
   pip install speedtest-cli
   ```

## Usage

Run the script from the command line:

```
python internet_connection_test.py
```

The script will perform the following steps:
1. Find the best server based on ping
2. Test download speed
3. Test upload speed
4. Display results, including:
   - Download speed (Mbps)
   - Upload speed (Mbps)
   - Ping (ms)
   - Speed categories for both download and upload

## Speed Categories

Speeds are categorized as follows:
- Bad: < 5 Mbps
- Normal: 5-25 Mbps
- Good: > 25 Mbps

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.