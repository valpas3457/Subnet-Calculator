import ipaddress

def subnet_calculator():
    try:
        # User input
        cidr = input("Enter an IP address with CIDR notation (e.g., 192.168.1.0/24): ")
        
        # Create the network object
        network = ipaddress.ip_network(cidr, strict=False)
        
        # Calculations
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        total_addresses = network.num_addresses
        usable_addresses = list(network.hosts())
        first_usable = usable_addresses[0] if usable_addresses else "None"
        last_usable = usable_addresses[-1] if usable_addresses else "None"
        
        # Subnet mask and wildcard
        subnet_mask = network.netmask
        wildcard = ipaddress.IPv4Address(int(network.hostmask))
        
        # Display results
        print("\n--- Subnet Information ---")
        print(f"Address:    {network.network_address}")
        print(f"Netmask:    {subnet_mask} = {network.prefixlen}")
        print(f"Wildcard:   {wildcard}")
        print(f"Network:    {network_address}/{network.prefixlen}")
        print(f"Broadcast:  {broadcast_address}")
        print(f"HostMin:    {first_usable}")
        print(f"HostMax:    {last_usable}")
        print(f"Hosts/Net:  {total_addresses - 2}")  # Excludes network and broadcast addresses
    except ValueError:
        print("Invalid IP address or CIDR. Please try again.")

# Run the program
subnet_calculator()