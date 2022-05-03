# Sentry

# Copyright (C) 2022 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program (LICENSE.md)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.



print("Loading Sentry...")

import os # Required to interact with certain operating system functions.
import subprocess # Required to manage sub-processes.
import signal # Required to manage sub-proceses.
import json # Required to process JSON data.
import utils # Load the utils.py script.
import time # Required to delay code execution.

style = utils.style # Load the command-line style-sheet from the utils script.
clear = utils.clear # Load the clear command from the utils script.

sentry_root_directory = str(os.path.dirname(os.path.realpath(__file__))) # This variable determines the folder path of the root Sentry directory. This should usually automatically recognize itself, but if it doesn't, you can set it manually.


if (os.path.exists(sentry_root_directory + "/config.json")): # Check to see if the configuration file exists at the expected path.
    config = json.load(open(sentry_root_directory + "/config.json")) # Load the configuration database from config.json
else: # The configuration file does not exist at the expected path.
    config = {"threat_database_name": "drones.json", "verbose_output": false, "save_detected_hazards": true, "detected_hazards_file": "history.json", "show_all_access_points": true, "radio_backend": "nmcli" } # Set reasonable default settings to prevent errors if the user decides to continue with no valid configuration file.
    
    print(style.yellow + "Warning: The configuration file could not be found. Please make sure the `config.json` file exists in the Sentry folder. Reasonable default settings have been set." + style.end) # Indicate that the configuration file could not be loaded.
    input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.


if (config["radio_backend"] != "nmcli" and config["radio_backend"] != "airodump"):
    config["radio_backend"] = "nmcli" # Set the radio backend configuration value to NetworkManager by default.
    print(style.yellow + "Warning: The radio_backend configuration value isn't a valid option. Defaulting to NetworkManager." + style.end) # Indicate that the radio_backend configuration value is invalid.
    input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.


if (config["verbose_output"] == True): # Check to see if the configuration value for verbose console output is enabled.
    print("    Loading threat database...")
    
if (os.path.exists(sentry_root_directory + "/" + config["threat_database_name"])): # Check to see if the threat database file exists at the expected path.
    threat_database = json.load(open(sentry_root_directory + "/" + config["threat_database_name"])) # Load the threat database from the file name specified in the configuration.
else:
    print(style.red + "Error: The threat database file specified in the configuration doesn't exist in the Sentry folder. The following file path couldn't be loaded: " + sentry_root_directory + "/" + config["threat_database_name"] + style.end)
    input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.


if (config["verbose_output"] == True): # Check to see if verbose console output is enabled.
    print("Loading complete.") # Indicate that loading is complete.
    input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.


if (config["save_detected_hazards"] == True): # Check to see if hazard saving is enabled.
    if (os.path.exists(sentry_root_directory + "/" + config["detected_hazards_file"])): # Check to see if the threat history file exists.
        threat_history_file = open(sentry_root_directory + "/" + config["detected_hazards_file"]) # Open the threat history file.
        threat_history = json.load(threat_history_file) # Load the threat history from the file.
    else:
        threat_history = [] # Set the threat history to a blank placeholder list.




while True: # Run in a loop forever until terminated.
    clear() # Clear the screen.

    print(style.bold + "Please select an option" + style.end) # Prompt the user to select an option in the main Sentry menu.
    print("1. Run")
    print("2. View")
    print(style.faint + "3. Configuration" + style.end)

    selection = str(input("Selection: ")) # Get the users selection input as a string.
    clear() # Clear the screen.

    if (selection == "1"): # Check to see if the user selected the "Run" option on the main menu.
        if (config["radio_backend"] == "nmcli"):
            while True: # Run in a loop forever until terminated.
                if (config["verbose_output"] == True):
                    print("Scanning for access points...")

                access_point_detection_command = "nmcli dev wifi rescan; nmcli -c no -f BSSID,SSID,CHAN,SIGNAL dev wifi | tail -n +2" # Set up the access point scanning command.
                command_output = str(os.popen(access_point_detection_command).read()) # Execute the access point scanning command.

                raw_access_points = command_output.split("\n") # Split the raw command output into a list, line by line.

                access_points = [] # Create a placeholder list for all of the access points and their data.
                for access_point in raw_access_points: # Iterate through each detected access point, and separate it's information into a sub-list.
                    access_points.append(access_point.split()) # Add the information from each access point to the access point list.

                for access_point in access_points: # Iterate through each entry in the list of access points.
                    if (access_point == []): # Check to see if this entry is blank.
                        access_points.remove(access_point) # Remove this entry from the list.


                if (config["show_all_access_points"] == True): # Check to see if the configuration value to show all access points is enabled.
                    print("Detected access points:")
                    for ap in access_points:
                        print("    " + ap[0] + "") # Display this device's MAC address.
                        print("        Name: " + ap[1]) # Display this device's name.
                        print("        Channel: " + ap[2]) # Display this device's channel.
                        print("        Strength: " + ap[3] + "%") # Display this device's relative signal stength.

                    time.sleep(1) # Wait for 1 second, to allow the user to see all of the detected access points for a brief moment.



                if (config["verbose_output"] == True): # Check to see if the verbose output configuration value is enabled.
                    print("Checking for threats...")


                detected_hazards = [] # This is a placeholder list of detected hazards that will be append to in the next step.

                for company in threat_database: # Iterate through each manufacturer in the threat database.
                    for mac in threat_database[company]["MAC"]: # Iterate through each MAC address prefix for this manufacturer in the threat database.
                        for ap in access_points: # Iterate through each access point detected in the previous step.
                            if (''.join(c for c in ap[0] if c.isalnum())[:6].lower() == mac.lower()): # Check to see if the first 6 characters of this AP matches the MAC address of this company.
                                ap.append(company) # Add this device's associated company to this access point's data.
                                ap.append(round(time.time())) # Add the current time to this access point's data.
                                detected_hazards.append(ap) # Add the current access point to the list of hazards detected this cycle.


                clear() # Clear the console output.
                if (len(detected_hazards) > 0): # Check to see if any hazards were detected.
                    print("Detected hazards:")
                    for hazard in detected_hazards: # Iterate through each detected hazard.
                        print("    " + hazard[0] + "") # Show this hazard's MAC address.
                        print("        Name: " + hazard[1]) # Show this hazard's name.
                        print("        Channel: " + hazard[2]) # Show this hazard's wireless channel.
                        print("        Strength: " + hazard[3] + "%") # Show this hazards relative signal strength.
                        print("        Company: " + hazard[4]) # Show company or brand that this hazard is associated with.
                    threat_history.append(hazard) # Add this threat to the treat history.
                    
                    with open(sentry_root_directory + "/" + config["detected_hazards_file"], 'w') as hazard_history_file: # Open hazard history file.
                        hazard_history_file.write(str(json.dumps(threat_history, indent = 4))) # Save the current hazard history to the file.




        elif (config["radio_backend"] == "airodump"): # Check to see if the configuration indicates that Sentry should operate in airodump-ng mode.
            os.popen("rm -f " + sentry_root_directory + "/airodump_data*.csv") # Delete any previous airodump data.

            airodump_command = "sudo airodump-ng wlan0mon -w airodump_data --output-format csv --background 1 --write-interval 1" # Set up the command to start airodump.
            proc = subprocess.Popen(airodump_command.split()) # Execute the command to start airodump.
            time.sleep(1) # Wait for 1 second to give airodump time to start.

            while True: # Run forever until terminated.
                clear() # Clear the console output.
                grab_output_command = "cat " + sentry_root_directory + "/airodump_data-01.csv" # Set up the command to grab the contents of airodump's CSV output file.
                command_output = str(os.popen(grab_output_command).read()) # Execute the output file grab command.

                line_split_output = command_output.split("\n") # Split the raw command output into a list, line by line.
                detected_devices = [] # Create a placeholder list for all of the detected devices and their data.
                for device in line_split_output: # Iterate through each detected device, and separate it's information into a sub-list.
                    detected_devices.append(device.split(",")) # Add the information from each detected device to the access point list.


                # Remove invalid entries from the listed of detected devices.
                for device in detected_devices: # Iterate through each entry in the list of devices.
                    if (len(device) <= 3): # Check to see if this entry is shorter than expected.
                        detected_devices.remove(device) # Remove this entry from the list.

                for device in detected_devices: # Iterate through each entry in the list of devices.
                    if (device[0] == "BSSID"): # Check to see if this entry is of the first header of the airodump output.
                        detected_devices.remove(device) # Remove this entry from the list.
                    elif (device[0] == "Station MAC"): # Check to see if this entry is of the second header of the airodump output.
                        detected_devices.remove(device) # Remove this entry from the list.

                for device in detected_devices: # Iterate through each entry in the list of devices.
                    if (len(device) <= 3): # Check to see if this entry is shorter than expected.
                        detected_devices.remove(device) # Remove this entry from the list.



                for device_key, device in enumerate(detected_devices): # Iterate through each entry in the list of devices.
                    for entry_key, entry in enumerate(device): # Iterate through each data entry for this device.
                        detected_devices[device_key][entry_key] = entry.strip() # Remove leading whitespace before any data in this entry.

                detected_hazards = [] # This is a placeholder list of detected hazards that will be append to in the next step.
                for company in threat_database: # Iterate through each manufacturer in the threat database.
                    for mac in threat_database[company]["MAC"]: # Iterate through each MAC address prefix for this manufacturer in the threat database.
                        for device in detected_devices: # Iterate through each access point detected in the previous step.
                            if (''.join(c for c in device[0] if c.isalnum())[:6].lower() == mac.lower()): # Check to see if the first 6 characters of this AP matches the MAC address of this company.
                                device.append(company) # Add this device's associated company to this device's data.
                                device.append(round(time.time())) # Add the current time to this device's data.
                                detected_hazards.append(device) # Add the current device to the list of hazards detected.


                if (config["show_all_access_points"] == True): # Check to see if the configuration value to show all access points is enabled.
                    print("Detected devices:")
                    for device in detected_devices:
                        print("    " + device[0] + "") # Display this device's MAC address.
                        print("        First Seen: " + device[1]) # Display the time-stamp of the last time this device was seen.

                    time.sleep(1) # Wait for 1 second, to allow the user to see all of the detected access points for a brief moment.


                print("Detected threats:")
                for device in detected_hazards:
                    print("    " + device[0] + "") # Display this device's MAC address.
                    print("        First Seen: " + device[1]) # Display the time-stamp of the last time this device was seen.

                time.sleep(1) # Wait for 1 second between each cycle.
                



    elif (selection == "2"): # Check to see if the user selected the "View" option on the main menu.
        for threat in threat_history: # Iterate through each threat loaded from the threat history file.
            print("Time: " + str(time.ctime(threat[5])).replace("  ", " ") + " (" + str(threat[5]) + ")") # Show the time that this threat was detected.
            print("    Name: " + str(threat[1])) # Show the name of this threat.
            print("    MAC: " + str(threat[0])) # Show the MAC address of this threat.
            print("    Channel: " + str(threat[2])) # Show the wireless channel of this threat.
            print("    Strength: " + str(threat[3]) + "%") # Show the relative signal strength of this threat.
            print("    Company: " + str(threat[4])) # Show the company or brand that this threat was associate with in the alert database at the time it was detected.
            print("") # Add a line break to visually separate each threat in the threat history.

        input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.

    elif (selection == "3"): # Check to see if the user selected the "Configuration" option on the main menu.
        print("Not yet implemented.") # TODO
        input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.

    else: # The user has selected an invalid option on the main menu.
        print(style.yellow + "Warning: Invalid selection." + style.end) # Inform the user that the selection they made on the main menu doesn't align with a valid option.
        input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.
