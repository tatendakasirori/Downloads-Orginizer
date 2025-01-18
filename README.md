# Automated Downloads Organizer

This project is designed to automatically organize files in the Downloads folder based on their extensions. It also provides the ability to schedule the script to run on system startup on the operating system (Windows, macOS, and Linux).

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Customization](#customization)
- [Contributing](#contributing)
  - [Contributing Guidelines](#contributing-guidelines)
- [Troubleshooting](#troubleshooting)

## Project Description

This project automatically organizes files in the Downloads folder by sorting them into categorized subfolders based on their file extensions (e.g., PDFs, png, etc.). The project is cross-platform, and it works on Windows, macOS, and Linux. It also provides a feature to schedule the script to run on system startup, ensuring automatic organization of files.

## Files in the Project

### `automate.py` (scheduler.py)
This module is responsible for scheduling the script to run automatically when the system starts up. It supports three operating systems:
- **Windows**: Uses Windows Task Scheduler.
- **macOS**: Uses `launchd` to add tasks to Activity Monitor.
- **Linux**: Uses `cron` to schedule tasks.

### `downloads_organizer.py` (organizer.py)
This module monitors the Downloads folder and moves files into categorized subfolders based on their file extension. It uses the `watchdog` library to detect when a new file is added to the Downloads folder and automatically organizes them.

### `get_path.py`
This module provides utility functions to retrieve and create the required directories for the Downloads folder and the Organized Downloads folder. It ensures that the necessary folders exist and returns the correct paths.

## Features
- **Auto-Organize Downloads**: The script detects new files in the Downloads folder and automatically organizes them into categorized folders (e.g., PDFs, images, etc.).
- **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- **Startup Scheduler**: Allows you to add the script to the system startup task scheduler (Task Scheduler for Windows, `launchd` for macOS, and `cron` for Linux).

## Requirements
- Python 3.6+
- `watchdog` library for file monitoring:
  ```bash
  pip install watchdog
 
## How to Use

### Step 1: Clone the Repository
Clone this repository to your local machine: git clone https://github.com/your-username/automated-downloads-organizer.git


### Step 2: Schedule the Script to Run on Startup
To ensure the script runs automatically on startup, run the `automate.py` script.
This will schedule the script to run when the user logs in.


## Customization
- **File Categories**: You can modify the `organizer.py` file to customize how files are organized based on their extensions.
- **Directories**: The `get_path.py` module allows you to specify custom directories for the Downloads and Organized Downloads folders.
- 
## Contributing

We welcome contributions! To contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Test your changes to ensure everything works.
5. Commit your changes (`git commit -am 'Add new feature'`).
6. Push to the branch (`git push origin feature-branch`).
7. Open a pull request.

-### Code of Conduct
Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) when participating in the project.
# Code of Conduct

## Introduction

Thank you for being a part of our project, **Automated Downloads Organizer**. We are committed to fostering an open and inclusive community. To achieve this, all participants in this project—contributors, maintainers, and users—are expected to adhere to the following code of conduct.

## Our Standards

We are committed to creating a friendly, safe, and respectful environment for everyone. By participating in this project, you agree to:

- Be respectful to all individuals, regardless of their background, expertise, or opinions.
- Provide constructive feedback and accept it gracefully.
- Collaborate in good faith to achieve shared goals.
- Avoid behavior that could be interpreted as harassment, trolling, or discrimination.
- Prioritize the project’s success and the well-being of the community over personal disputes.

Examples of unacceptable behavior include:

- Insults, harassment, or offensive comments, whether in public or private.
- Sharing private information about others without explicit permission.
- Personal attacks or sustained arguments that disrupt the community.
- Any other behavior deemed inappropriate for a professional and collaborative space.

## Scope

This Code of Conduct applies to all spaces where the project operates, including:

- GitHub repositories (issues, pull requests, discussions)
- Communication channels (email, forums, or other platforms)
- Any events or activities organized under the project’s banner

## Reporting Violations

If you witness or experience behavior that violates this Code of Conduct, please report it to the project maintainers at **[tatendakasirori1000@gmail.com](mailto:tatendakasirori1000@gmail.com)**. Your report will be treated with the utmost confidentiality, and we will take appropriate action to address the situation.

## Consequences

Violations of this Code of Conduct will be addressed on a case-by-case basis. Possible consequences include, but are not limited to:

1. A warning and request to cease the offending behavior.
2. Temporary or permanent exclusion from project spaces.
3. Escalation to relevant authorities if the behavior violates legal standards.

## Acknowledgment

This Code of Conduct is inspired by the [Contributor Covenant](https://www.contributor-covenant.org) and adapted to suit our community. 

## Questions and Feedback

If you have any questions, suggestions, or feedback about this Code of Conduct, feel free to contact us at **[tatendakasirori1000@gmail.com](mailto:tatendakasirori1000@gmail.com)**.

Thank you for helping us create a welcoming and inclusive environment!


## Troubleshooting

### Task Scheduler Not Working (Windows)
- Make sure you run the script as an Administrator. 
- Ensure the path to the Python executable is correct in the Task Scheduler.

### Permissions Issue (macOS/Linux)
- Ensure you have the necessary permissions to add tasks to the system scheduler. You might need `sudo` for macOS/Linux.








