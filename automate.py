import os
import platform
import subprocess
import sys

def add_to_task_scheduler_windows(script_path):
    # Add a scheduled task in Windows Task Scheduler
    try:
        # Define the command to create the task using schtasks
        script_path = f"{script_path.replace('automate', 'downloads_organizer')}"
        command = f'schtasks /create /tn "MyPythonScript" /tr "python {script_path}" /sc onlogon /f'
        
        # Run the command to add the task to Task Scheduler
        subprocess.run(command, check=True, shell=True)
        print("Successfully added to Task Scheduler in Windows.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add to Task Scheduler. Error: {e}")
        print("Make sure you are running the script as an administrator.")

def add_to_activity_monitor_mac(script_path):
    # Add to Activity Monitor: macOS doesn't have a direct API for this, so we use launchd (plist file) for task scheduling.
    try:
        # Prepare a command for adding a background job via launchd
        plist_content = f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.myscript.backgroundtask</string>
            <key>ProgramArguments</key>
            <array>
                <string>{script_path}</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
        </dict>
        </plist>
        """
        plist_file_path = "/Library/LaunchDaemons/com.myscript.backgroundtask.plist"

        # Create the plist file in the right location
        with open(plist_file_path, "w") as f:
            f.write(plist_content)

        # Load the new task into launchd (this will start it automatically)
        subprocess.run(["sudo", "launchctl", "load", plist_file_path], check=True)
        print("Successfully added to Activity Monitor on macOS.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add task on macOS. Error: {e}")
        print("Make sure you are running the script as an administrator and have correct permissions.")

def add_to_cron_linux(script_path):
    # Add a cron job in Linux
    try:
        # Open the crontab file for editing
        cron_job = f'@reboot python3 {script_path}'
        subprocess.run(f'(crontab -l ; echo "{cron_job}") | crontab -', shell=True, check=True)
        print("Successfully added to cron on Linux.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add to cron. Error: {e}")
        print("Make sure you are running the script with proper permissions.")

def main():
    # Get the current OS
    current_os = platform.system()

    # Get the script path (example: path to this script or other script to be scheduled)
    script_path = os.path.abspath(sys.argv[0])  # The script running this code (you can replace with any file path)

    # Perform logic based on OS
    if current_os == 'Windows':
        add_to_task_scheduler_windows(script_path)
    elif current_os == 'Darwin':  # macOS
        add_to_activity_monitor_mac(script_path)
    elif current_os == 'Linux':
        add_to_cron_linux(script_path)
    else:
        print(f"Unsupported operating system: {current_os}")

if __name__ == "__main__":
    main()
