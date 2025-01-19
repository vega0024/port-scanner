# Port Scanner

A simple Python script that scans a specified IP address for open ports. This tool utilizes the `socket` library to attempt connections to ports in the range of 1 to 65535 and provides color-coded output to indicate whether each port is open or closed.

## Features

- Scans all ports from 1 to 65535.
- Color-coded output using the `colorama` library:
  - Green for open ports.
  - Red for closed ports.
- User-friendly interface that prompts for the target IP address.

## Requirements

- Python 3.x
- `colorama` library

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:

   ```bash
   pip install colorama
   ```

## Usage

1. Run the script:

   ```bash
   python port_scanner.py
   ```

2. When prompted, enter the target IP address you wish to scan.

3. The script will continuously scan the specified IP address for open ports, displaying the results in real-time.

## Example Output

```
Enter target IP address: 192.168.1.1
The port 22 is open on 192.168.1.1.>>>>>>>>>>>>>>>>>>>>>>>OPEN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
The port 80 is closed on 192.168.1.1.
The port 443 is open on 192.168.1.1.>>>>>>>>>>>>>>>>>>>>>>>OPEN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
...
```

## Notes

- Scanning a large number of ports may take some time, depending on the network conditions and the target system's response.
- Ensure you have permission to scan the target IP address to avoid any legal issues.


## Author

Nipuna Muthukumarana - [LinkedIn Profile](https://www.linkedin.com/in/nmuthukumarana24)

---
