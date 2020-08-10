# Purpose
Login Script for IP ACCT Solution based Broadband Login

# Usage
* Prerequisites: 
    * Have Python with pip and virtualenv installed
    *   * rename the file sampleenvfile to ".env" and enter your credentials there
    * Install Python3 and virtualenv for your distro
    * Create virtualenv and install requirements
        `python3 -m virtualenv lenv;
        source lenv/bin/activate.sh;
        pip install -r requirements.txt;
        `
    * Edit run.sh to refect your project path
    * Execute `./run.sh` 
    * Set crontab `crontab -e` to execute script every 15 mins. CHnage as per requirements in command below:
        * */15 * * * * ./**Project-Path**/run.sh
