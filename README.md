# Kick Chat Overlay

A customizable, always-on-top, and frameless desktop application that allows you to monitor Kick.com chat. Ideal for streamers who want to keep an eye on chat while gaming or for users who want a minimal chat client.

![Application Screenshot](https://i.imgur.com/your_screenshot_url.png)
*(Note: Replace this link with a URL of your own screenshot.)*

---

## ✨ Features

- **Frameless & Transparent:** A minimal interface that doesn't get in the way of your game or other content.
- **Always on Top:** The chat window remains visible over all other applications.
- **Extensive Customization:**
  - Adjustable window size (width and height).
  - Configurable font size for chat text.
  - Adjustable window opacity (transparency).
- **Multi-Language Support:** The settings interface is available in English, Turkish, French, Russian, Chinese, and Korean.
- **Advanced Positioning:**
  - Place the window in 6 preset positions (corners and middle-sides) with one click.
  - A configurable hotkey to quickly cycle through positions.
  - Nudge the window pixel-by-pixel using configurable hotkeys (defaults to arrow keys).
- **Persistent Settings:** All your preferences (channel, size, position, hotkeys) are automatically saved in a `settings.json` file and loaded on the next launch.
- **Dynamic Filtering:** Uses JavaScript to hide unwanted elements from the Kick chat webpage for a cleaner view.

---

## 🚀 Installation

You must have **Python 3** installed on your system to run this application.

1.  **Clone or Download the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install Dependencies:**
    Open a Command Prompt (CMD) or terminal in the project folder and run the following command to install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🛠️ Usage

1.  Run the `kick_overlay.pyw` (or `kick_overlay.py`) script.
2.  In the settings window that appears:
    - Enter the **Kick channel name** you want to view.
    - Adjust settings like window size, font size, and opacity to your preference.
    - Configure the positioning and hotkey settings.
3.  Click the **"SAVE SETTINGS & LAUNCH"** button.

The settings window will close, and the chat overlay will appear on your screen with your chosen settings.

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
