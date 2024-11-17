# Subnet Calculator

A simple Python script to calculate and display subnet-related information for a given IP address and subnet mask in CIDR notation. This tool is useful for network engineers, system administrators, and students learning about IP addressing and subnetting.

## Features

- Calculates essential subnet details:
  - Network Address
  - Broadcast Address
  - First Usable Address (HostMin)
  - Last Usable Address (HostMax)
  - Subnet Mask
  - Wildcard Mask
  - Total Usable Hosts
- Validates user input and handles errors gracefully.
- Supports IPv4 CIDR notations (e.g., `192.168.1.0/24`).

## Getting Started

### Prerequisites
- Python 3.6 or higher.

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/subnet-calculator.git
    cd subnet-calculator
    ```

2. Run the script:
    ```bash
    python subnet_calculator.py
    ```

## Usage

1. Run the script from the terminal.
2. Enter an IP address with CIDR notation when prompted. Example:
    ```bash
    Enter an IP address with CIDR notation (e.g., 192.168.1.0/24): 192.168.0.1/24
    ```

The script will display detailed subnet information:
```text
--- Subnet Information ---
Address:    192.168.0.0
Netmask:    255.255.255.0 = 24
Wildcard:   0.0.0.255
=>
Network:    192.168.0.0/24
Broadcast:  192.168.0.255
HostMin:    192.168.0.1
HostMax:    192.168.0.254
Hosts/Net:  254
