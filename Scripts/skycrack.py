import struct
import datetime
import socket
import csv
from collections import defaultdict

def parse_sky_file(filename, output_csv=None, aggregate_ip_csv=None, aggregate_day_csv=None):
    with open(filename, "rb") as f:
        data = f.read()
    
    offset = 0

    # --- Header ---
    magic = data[offset:offset+8]
    offset += 8
    if magic != b'\x91SKY\r\n\x1a\n':
        raise ValueError("Not a valid SKY file")
    
    version = data[offset]
    offset += 1
    if version != 0x01:
        raise ValueError("Unsupported SKY version")
    
    creation_ts = struct.unpack(">I", data[offset:offset+4])[0]
    creation_time = datetime.datetime.utcfromtimestamp(creation_ts)
    offset += 4
    
    hostname_len = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    hostname = data[offset:offset+hostname_len].decode()
    offset += hostname_len
    
    flag_len = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    flag = data[offset:offset+flag_len].decode()
    offset += flag_len
    
    num_entries = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    
    print(f"SKY v1 log created at {creation_time}, host={hostname}, flag={flag}, entries={num_entries}")

    # --- Body ---
    entries = []
    totals_ip = defaultdict(int)      # Sum bytes per source IP
    totals_day = defaultdict(int)     # Sum bytes per day (YYYY-MM-DD)

    for _ in range(num_entries):
        src_ip_int = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4
        dst_ip_int = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4
        ts = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4
        bytes_transferred = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4
        
        src_ip = socket.inet_ntoa(struct.pack(">I", src_ip_int))
        dst_ip = socket.inet_ntoa(struct.pack(">I", dst_ip_int))
        ts_dt = datetime.datetime.utcfromtimestamp(ts)
        
        entries.append({
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "timestamp": ts_dt,
            "bytes_transferred": bytes_transferred
        })
        
        totals_ip[src_ip] += bytes_transferred
        day_str = ts_dt.strftime("%Y-%m-%d")  # Extract date
        totals_day[day_str] += bytes_transferred

    # --- Optional: save raw entries to CSV ---
    if output_csv:
        with open(output_csv, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["src_ip","dst_ip","timestamp","bytes_transferred"])
            writer.writeheader()
            for e in entries:
                writer.writerow(e)
        print(f"Saved {num_entries} entries to {output_csv}")
    
    # --- Optional: save aggregated totals per IP ---
    if aggregate_ip_csv:
        with open(aggregate_ip_csv, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["src_ip","total_bytes_sent"])
            writer.writeheader()
            for ip, total in totals_ip.items():
                writer.writerow({"src_ip": ip, "total_bytes_sent": total})
        print(f"Saved aggregated totals per IP to {aggregate_ip_csv}")

    # --- Optional: save aggregated totals per day ---
    if aggregate_day_csv:
        with open(aggregate_day_csv, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["date","total_bytes_sent"])
            writer.writeheader()
            for day, total in totals_day.items():
                writer.writerow({"date": day, "total_bytes_sent": total})
        print(f"Saved aggregated totals per day to {aggregate_day_csv}")

    # --- Print summary ---
    max_ip = max(totals_ip, key=totals_ip.get)
    print(f"IP that sent the most bytes: {max_ip}, total bytes: {totals_ip[max_ip]}")
    
    max_day = max(totals_day, key=totals_day.get)
    print(f"Day with the most bytes sent: {max_day}, total bytes: {totals_day[max_day]}")
    
    return entries, totals_ip, totals_day

# --- Usage ---
entries, totals_ip, totals_day = parse_sky_file(
    "example.sky",
    output_csv="sky_log.csv",
    aggregate_ip_csv="sky_totals_ip.csv",
    aggregate_day_csv="sky_totals_day.csv"
)
