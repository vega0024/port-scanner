# Network Scanning Tool

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Important Note](#important-note)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This is a simple yet effective network scanning tool written in Python. It allows users to check the status of ports on a target IP address, helping to identify open and closed ports. This tool is designed to make network scanning accessible for everyone, whether you're a cybersecurity professional or just starting out.

## Features

- Scans all ports from 1 to 65535
- Real-time feedback on port status
- Color-coded output for easy readability (green for open ports, red for closed)

## Requirements

- Python 3.x
- `colorama` library (for colored output)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vega0024/port-scanner.git
   cd port-scanner
   ```

2. Install the required library:
   ```bash
   pip install colorama
   ```

## Usage

1. Run the script:
   ```bash
   python port-scanner.py
   ```

2. Enter the target IP address when prompted.

3. The tool will begin scanning and display the status of each port.

## Example Output

```
The port 80 is open on 192.168.1.1. >>>>>>>>>>>>>>>>>>>>>>>>>OPEN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
The port 22 is closed on 192.168.1.1.
```

## Important Note

Please use this tool responsibly and only scan networks that you own or have explicit permission to test. Unauthorized scanning can be considered illegal and unethical.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/nmuthukumarana24).
