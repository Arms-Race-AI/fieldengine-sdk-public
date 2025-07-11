#!/usr/bin/env python3
import hashlib, time, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--client", required=True)
args = parser.parse_args()

epoch = str(int(time.time()))
raw = f"{args.client}:{epoch}".encode()
key = hashlib.sha256(raw).hexdigest()

with open("license_key.txt", "w") as f:
    f.write(f"SHA256: {key}\n")

print("[OK] Minted key:", key)
