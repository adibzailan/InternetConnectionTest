import speedtest
import time

def check_internet_speed():
    print("Testing internet speed...")
    st = speedtest.Speedtest()
    
    print("Getting best server based on ping...")
    st.get_best_server()
    
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    ping = st.results.ping
    
    return download_speed, upload_speed, ping

def categorize_speed(speed):
    if speed < 10:
        return "Very Poor"
    elif 10 <= speed < 25:
        return "Poor"
    elif 25 <= speed < 50:
        return "Fair"
    elif 50 <= speed < 100:
        return "Good"
    elif 100 <= speed < 500:
        return "Very Good"
    else:
        return "Excellent"

def categorize_ping(ping):
    if ping < 20:
        return "Excellent"
    elif 20 <= ping < 50:
        return "Very Good"
    elif 50 <= ping < 100:
        return "Good"
    elif 100 <= ping < 150:
        return "Fair"
    else:
        return "Poor"

def main():
    try:
        start_time = time.time()
        download, upload, ping = check_internet_speed()
        end_time = time.time()
        
        print("\n--- Results ---")
        print(f"Download speed: {download:.2f} Mbps ({categorize_speed(download)})")
        print(f"Upload speed: {upload:.2f} Mbps ({categorize_speed(upload)})")
        print(f"Ping: {ping:.2f} ms ({categorize_ping(ping)})")
        print(f"Test duration: {end_time - start_time:.2f} seconds")
        
        overall_rating = min(categorize_speed(download), categorize_speed(upload), categorize_ping(ping))
        print(f"\nOverall connection rating: {overall_rating}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Internet connection might be unavailable.")

if __name__ == "__main__":
    main()