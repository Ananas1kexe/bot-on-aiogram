# Telegram Notes Bot

## Description

This bot for Telegram allows users to create, view, and delete notes using an SQLite database through the `aiosqlite` library and `aiogram 3`. Each note is associated with a unique user identifier (`chat_id`) and has its own unique `note_id`.

## Requirements

- Python 3.9+
- `aiogram 3.x`
- `aiosqlite`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ananas1kexe/bot-on-aiogram
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file with your bot's token and save it at the root of the project:

    ```
    BOT_TOKEN=yourbottoken
    ```

## Database Structure

The `main.db` database contains a `notes` table where user notes are stored.

### `notes` Table

- `chat_id`: User's chat ID.
- `note_id`: Unique note identifier (auto-incremented).
- `note`: Content of the note.

## Usage

### Bot Commands

- **/create <note>**: Creates a new note. If a note already exists for the chat, it will not be overwritten.
  
  Example usage:
  ```
  /create Example note
  ```

- **/notes**: Shows all notes for the current user.
  
  Example usage:
  ```
  /notes
  ```

- **/delete <note_id>**: Deletes the note with the specified `note_id`.

  Example usage:
  ```
  /delete 1
  ```

### Example Workflow

1. The user sends the command `/create Note 1`.
2. The bot saves the note in the database and assigns a unique `note_id`.
3. The user sends the command `/notes`, and the bot responds with a list of all the user's notes.
4. If the user sends the command `/delete 1`, the bot deletes the note with `note_id = 1`.

## Running the Bot

To start the bot, run the following command:

```bash
python main.py
```

The bot will begin running and will listen for Telegram updates.

## Logging

All bot actions are logged to the console. In case of errors, information will be displayed with logging levels (INFO, ERROR).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them using `git commit -am 'Add feature'`.
4. Submit a pull request.

## License

MIT License. See the `LICENSE` file for more details.\
[https://github.com/Ananas1kexe/bot-on-aiogram/blob/main/LICENSE](https://github.com/Ananas1kexe/bot-on-aiogram/blob/main/LICENSE)
