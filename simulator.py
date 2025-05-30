import ipaddress

# Routing table containing networks, next hop, and associated interface
routing_table = [
    {"network": "192.168.1.0/24", "next_hop": "192.168.1.1", "interface": "eth0"},
    {"network": "192.168.0.0/16", "next_hop": "192.168.0.1", "interface": "eth1"},
    {"network": "0.0.0.0/0", "next_hop": "10.0.0.1", "interface": "eth2"},
]

# Function to find the best route (longest prefix match) for a given destination IP
def find_best_route(destination_ip):
    # Convert input string to an IP address object
    dest_ip = ipaddress.ip_address(destination_ip)
    best_match = None  # Holds the best matching route
    max_prefix = -1    # Tracks the longest prefix length found

    # Iterate over all routes in the routing table
    for route in routing_table:
        net = ipaddress.ip_network(route["network"])
        # Check if the destination IP is in the current network
        if dest_ip in net:
            # Select the route with the longest prefix match
            if net.prefixlen > max_prefix:
                best_match = route
                max_prefix = net.prefixlen

    return best_match  # Return the best matching route or None if no match found

# Main program handling user interaction
def main():
    print("📡 Routing Table Simulator")
    destination_ip = input("Enter destination IP address: ")

    try:
        # Find the best route for the entered IP address
        route = find_best_route(destination_ip)
        if route:
            print(f"✅ Matched Route: {route['network']} → Interface: {route['interface']} (Next hop: {route['next_hop']})")
        else:
            print("❌ No matching route found.")
    except ValueError:
        # Handle invalid IP address input
        print("⚠️ Invalid IP address.")

# Script entry point: run main() only if this script is executed directly
if __name__ == "__main__":
    main()