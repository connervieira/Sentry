# Configuration

This document explains each configuration value in the `config.json` file.

- `threat_database_name`
    - **Type**: String
    - **Description**: This configuration value defines the name of the database file that Sentry will use to identify the threat status of various access points.
- `verbose_output`
    - **Type**: Boolean
    - **Description**: This configuration value determines whether or not Sentry will display in-depth information messages during loading and operation. When enabled, Sentry will display information about loading and operation stages, in addition to the normal messages.
- `save_detected_hazards`
    - **Type**: Boolean
    - **Description**: This configuration value determines whether or not Sentry will record the threats it detects to a JSON file. When enabled, Sentry will create a file, based on the `detected_hazards_file` configuration value in it's own directory.
- `detected_hazards_file`
    - **Type**: String
    - **Description**: This configuration value defines the file name that Sentry will use to record detected hazards, provided the `save_detected_hazards` configuration value is enabled.
- `show_all_access_points`
    - **Type**: Boolean
    - **Description**: This configuration value will determines whether or not Sentry will display all detected access points, not just those that are deemed to be threats.
- `radio_backend`
    - **Type**: String
    - **Description**: This configuration value determines the radio receiver back-end that Sentry will use, and (by extension), the features and functionality that are available.
    - **Options**: This setting can be set to the following options.
        - `nmcli` - This option is the NetworkManager backend, and uses the built-in Linux networking backend to detect wireless access point. This option is stable, simple, and reliable.
        - `airodump` - This option uses AirCrack-NG as a backend, which offers much greater coverage, but is significantly more complicated to set up. To use this backend, aircrack-ng, as well as airmon-ng need to be set up and running.
