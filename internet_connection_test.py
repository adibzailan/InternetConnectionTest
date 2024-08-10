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
    if speed < 5:
        return "Bad"
    elif 5 <= speed < 25:
        return "Normal"
    else:
        return "Good"

def main():
    try:
        download, upload, ping = check_internet_speed()
        print(f"\nDownload speed: {download:.2f} Mbps")
        print(f"Upload speed: {upload:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")
        
        # Determine speed category
        download_category = categorize_speed(download)
        upload_category = categorize_speed(upload)
        
        print(f"Download Speed Category: {download_category}")
        print(f"Upload Speed Category: {upload_category}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Internet connection might be unavailable.")

if __name__ == "__main__":
    main()
