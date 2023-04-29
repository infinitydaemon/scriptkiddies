import re
import time
import datetime
import matplotlib.pyplot as plt

# Define log file path and pattern
log_path = "/var/log/syslog"
log_pattern = r".*\[iptables\].*"

# Initialize lists to store data
data_dict = {}
time_list = []

# Set start time to current time
start_time = time.time()

# Define function to parse log lines
def parse_line(line):
    # Extract timestamp from log line
    timestamp = re.search(r"^\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}", line).group()
    # Convert timestamp to datetime object
    date_object = datetime.datetime.strptime(timestamp, "%b %d %H:%M:%S")
    # Add timestamp to time_list
    time_list.append(date_object)
    # Extract chain name from log line
    chain = re.search(r"CHAIN=(\S+)\s", line).group(1)
    # Extract action from log line
    action = re.search(r"ACTION=(\S+)\s", line).group(1)
    # Create key for data_dict
    key = "{}-{}".format(chain, action)
    # Increment value for key in data_dict
    data_dict[key] = data_dict.get(key, 0) + 1

# Define function to plot graph
def plot_graph():
    # Convert time_list to matplotlib format
    x = plt.plot_date(time_list, [0] * len(time_list))
    # Set y values for each key in data_dict
    y = []
    labels = []
    for key, value in data_dict.items():
        y.append(value)
        labels.append(key)
    # Plot graph
    plt.bar(labels, y)
    # Set graph title and axis labels
    plt.title("iptables Logs")
    plt.xlabel("Chain - Action")
    plt.ylabel("Number of Logs")
    # Save graph to file
    plt.savefig("iptables_logs.png")

# Loop indefinitely
while True:
    # Open log file
    with open(log_path, "r") as f:
        # Read lines
        lines = f.readlines()
        # Loop through lines
        for line in lines:
            # Check if line matches pattern
            if re.match(log_pattern, line):
                # Parse line
                parse_line(line)
    # Plot graph
    plot_graph()
    # Clear data_dict and time_list
    data_dict.clear()
    time_list.clear()
    # Wait 5 minutes
    time.sleep(300)
