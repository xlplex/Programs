import socket
import time

def ping_ip(ip_address):
    try:
        start_time = time.time()
        # Socket erstellen
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout für die Verbindung setzen

        # IP-Adresse pingen
        s.connect((ip_address, 80))
        end_time = time.time()

        # Zeitdauer für die Verbindung berechnen
        ping_time = end_time - start_time
        return f"Ping to {ip_address} successful. Time: {ping_time} seconds"
    except socket.error as e:
        return f"Unable to ping {ip_address}. Error: {e}"
    finally:
        s.close()

def main():
    ip_address = input("Geben Sie die IP-Adresse ein, die Sie pingen möchten: ")
    result = ping_ip(ip_address)
    print(result)

if __name__ == "__main__":
    main()
