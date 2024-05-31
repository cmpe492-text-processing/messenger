# Project: WhatsApp Corpus Notification

This project is designed to send WhatsApp messages about the current status of a PostgreSQL table to two project partners. The messages include the total row count and a summary of the latest 100 subreddits with their respective counts. The messages are sent using the Twilio API.

## Directory Structure

```
.
├── main.py
├── database.py
├── requirements.txt
├── send-corpus-message.sh
└── .env.example
```

### main.py

This is the main script that imports `DatabaseManager` from `database.py`, constructs the messages, and sends them using the Twilio API. It is runnable and serves as the entry point for the cron job.

### database.py

This module contains the `DatabaseManager` class, which handles all database-related operations, including connecting to the PostgreSQL database and fetching data.

### requirements.txt

This file lists the dependencies for the project. The required packages are:
- `python-dotenv`
- `twilio`

### send-corpus-message.sh

This is the script used in the cron job to execute `main.py`. Make sure to make this file executable using the following command:

```bash
chmod +x send-corpus-message.sh
```

### .env.example

This is an example environment file. Copy this file to `.env` and fill in the appropriate values:

```
DATABASE_URL="postgresql://<username>:<password>@<host>:<port>/<database>"
TWILIO_ACCOUNT_SID=""
TWILIO_AUTH_TOKEN=""
TWILIO_FROM="+xxxxxxxxxxx"
TO_PHONE_NUMBERS="+xxxxxxxxxxx,+xxxxxxxxxxx"
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create and populate the .env file:**
   ```bash
   cp .env.example .env
   # Fill in the .env file with your credentials
   ```

4. **Make the script executable:**
   ```bash
   chmod +x send-corpus-message.sh
   ```

5. **Set up the cron job:**
   Open the crontab editor:
   ```bash
   crontab -e
   ```
   Add the following line to the crontab:
   ```bash
   0 0,1,6,8,10,12,14,16,18,20,22,23 * * * <absolute-path-to-script>/send-corpus-message.sh
   ```
   This cron job runs the script at the specified hours (midnight, 1 AM, 6 AM, 8 AM, 10 AM, noon, 2 PM, 4 PM, 6 PM, 8 PM, 10 PM, and 11 PM).

## Usage

The script sends WhatsApp messages with the following format:

```
<total_rows_in_table>

Latest 100 subreddits:

•⁠  ⁠subreddit1: count1
•⁠  ⁠subreddit2: count2
...
```

This allows you to monitor the state of your table as new data is added.

## Notes

- Ensure you have a valid Twilio account and have set up WhatsApp messaging on your Twilio number.
- The database connection and Twilio credentials must be correctly set in the `.env` file.
- Adjust the cron job timing as necessary to suit your needs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Twilio](https://www.twilio.com/) for their messaging API
- [Dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables

