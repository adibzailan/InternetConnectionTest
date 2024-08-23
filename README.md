# 🚀 InternetConnectionTest

Hey there! Welcome to InternetConnectionTest, a nifty Python script that gives you the lowdown on your internet connection speed using Speedtest.net's awesome infrastructure.

## ✨ What's Cool About It?

- 📥 Measures download speeds
- 📤 Measures upload speeds
- 🏓 Calculates ping
- 🏷️ Categorizes speeds from "Very Poor" to "Excellent"
- 📊 Serves up a clear, easy-to-read output

## 🛠️ What You'll Need

- Python 3.x (because who's using 2.x anymore, right?)
- speedtest-cli library (the real MVP)

## 🚀 Getting Started

1. Clone this bad boy:
   
   ```
   git clone https://github.com/adibzailan/internet_connection_test.git
   ```

2. Hop into the project folder:
   
   ```
   cd internet_connection_test
   ```

3. Install the star of the show:
   
   ```
   pip install speedtest-cli
   ```

## 🎬 Lights, Camera, Action!

Fire it up from your command line:

```
python run-internet_connection_test.py
```

Here's what'll go down:

1. Find the server with the best ping (because we're not savages)
2. Test your download speed (crossing fingers for you)
3. Test your upload speed (for all you content creators out there)
4. Show off the results, including:
   - Download speed (in Mbps, because bits are so last century)
   - Upload speed (also in Mbps, consistency is key)
   - Ping (in ms, for the gamers among us)
   - Speed categories for download, upload, and ping
   - An overall connection rating (drum roll, please)
   - How long the test took (because time is money, friend)

## 🏎️ Speed Categories

We've gone all out with the categories:

- Very Poor: < 10 Mbps (time to call your ISP?)
- Poor: 10-25 Mbps (could be worse, could be better)
- Fair: 25-50 Mbps (not too shabby)
- Good: 50-100 Mbps (now we're talking)
- Very Good: 100-500 Mbps (living the high-speed life)
- Excellent: > 500 Mbps (are you at NASA?)

Ping categories are in there too, from "Excellent" to "Poor". Because latency matters!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for all the legal jazz. But basically, do what you want with it (just don't blame us if anything goes wrong, okay?).

Now go forth and test that internet speed! 🚀