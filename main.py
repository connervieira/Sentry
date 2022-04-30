# Sentry

# Copyright (C) 2022 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program (LICENSE.md)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.



print("Loading Sentry...")

import os # Required to interact with certain operating system functions
import json # Required to process JSON data
import utils # Load the utils.py script
style = utils.style # Load the command-line style-sheet from the utils script.
clear = utils.clear # Load the clear command from the utils script.

sentry_root_directory = str(os.path.dirname(os.path.realpath(__file__))) # This variable determines the folder path of the root Sentry directory. This should usually automatically recognize itself, but if it doesn't, you can set it manually.

config = json.load(open(sentry_root_directory + "/config.json")) # Load the configuration database from config.json

if (config["verbose_output"] == True):
    print("    Loading drone database...")

drone_database = json.load(open(sentry_root_directory + "/" + config["drone_database_name"])) # Load the drone database from the file name specifid in the configuration.


if (config["verbose_output"] == True):
    print("Loading complete.")
    input(style.italic + style.faint + "Press enter to continue" + style.end)





while True: # Run in a loop forever until terminated.
    clear() # Clear the screen.

    print(style.bold + "Please select an option" + style.end) # Prompt the user to select an option in the main Sentry menu.
    print("1. Run")
    print(style.faint + "2. View" + style.end)
    print(style.faint + "3. Configuration" + style.end)

    selection = str(input("Selection: ")) # Get the users selection input as a string.

    if (selection == "1"):
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




            if (config["verbose_output"] == True):
                print("Checking for drones...")


            detected_hazards = [] # This is a placeholder list of detected hazards that will be append to in the next step.

            for company in drone_database: # Iterate through each manufacturer in the drone database.
                for mac in drone_database[company]["MAC"]: # Iterate through each MAC address prefix for this manufacturer in the drone database.
                    for ap in access_points: # Iterate through each access point detected in the previous step.
                        if (''.join(c for c in ap[0] if c.isalnum())[:6].lower() == mac.lower()): # Check to see if the first 6 characters of this AP matches the MAC address of this company.
                            ap.append(company)
                            detected_hazards.append(ap) # Add the current access point to the list of hazards detected this cycle.


            clear() # Clear the console output.
            if (len(detected_hazards) > 0): # Check to see if any hazards were detected.
                print("Detected hazards:")
                for hazard in detected_hazards:
                    print("    " + hazard[0] + "")
                    print("        Name: " + hazard[1])
                    print("        Channel: " + hazard[2])
                    print("        Strength: " + hazard[3] + "%")
                    print("        Company: " + hazard[4])


    elif (selection == "2"):
        print("Not yet implemented.") # TODO
        input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.

    elif (selection == "3"):
        print("Not yet implemented.") # TODO
        input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.

    else:
        print(style.yellow + "Warning: Invalid selection." + style.end)
        input(style.italic + style.faint + "Press enter to continue" + style.end) # Wait for the user to press enter before continuing.
