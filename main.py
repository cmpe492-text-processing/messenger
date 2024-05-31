import os
from dotenv import load_dotenv
import database
from twilio.rest import Client


def get_body() -> str:
    db = database.DatabaseManager()
    count = db.get_corpus_count()
    latest = db.get_latest_100_platforms()
    db.close_connection()

    platform_counts = {}
    for platform in latest:
        platform = platform.split('/', 1)[1]
        platform_counts.update({platform: platform_counts.get(platform, 0) + 1})

    b = '*' + str(count) + '*\n\n'
    b += '*Latest 100 subreddits:*\n\n'

    platform_counts = {k: v for k, v in sorted(platform_counts.items(), key=lambda item: item[1], reverse=True)}
    for platform, count in platform_counts.items():
        b += f'- {platform}: {count}\n'

    b += '\n'
    return b


def get_twilio_client() -> Client:
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    return Client(account_sid, auth_token)


def send_message(c: Client, b: str, f: str, t: str) -> None:
    """
    Send a message using the Twilio client.

    :param c:   Twilio client
    :param b:   Body of the message
    :param f:   From number
    :param t:   To number
    :return:
    """
    c.messages.create(
        from_='whatsapp:' + f,
        body=b,
        to='whatsapp:' + t
    )


if __name__ == '__main__':
    load_dotenv()

    body = get_body()
    client = get_twilio_client()

    from_ = os.getenv('TWILIO_FROM')
    to_ = os.getenv('TO_PHONE_NUMBERS')

    to_numbers = to_.split(',')
    for to_number in to_numbers:
        send_message(client, body, from_, to_number)
