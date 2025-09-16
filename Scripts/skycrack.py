import struct
import datetime
import socket
import csv

def parse_sky_file(filename, output_csv=None):
    with open(filename, "rb") as f: #read bit by bit
        data = f.read()

    offset = 0

    magic = data[offset:offset+8]
    offset += 8

    if magic != b'\x91SKY\r\n\x1a\n':
        raise ValueError("Invalid .sky file")

    version = data[offset]

    offset += 1

    if version != 0x01:
        raise ValueError("Invalid .sky version")

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

    entries = []
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
    
    # --- Optional: save to CSV ---
    if output_csv:
        with open(output_csv, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["src_ip","dst_ip","timestamp","bytes_transferred"])
            writer.writeheader()
            for e in entries:
                writer.writerow(e)
        print(f"Saved {num_entries} entries to {output_csv}")
    
    return entries

# --- Usage ---
entries = parse_sky_file("example.sky", output_csv="sky_log.csv")
for e in entries[:5]:  # print first 5 entries
    print(e)