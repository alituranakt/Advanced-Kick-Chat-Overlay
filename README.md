# Kick Chat Overlay

A customizable, frameless, always-on-top desktop application for viewing Kick.com chat. Ideal for streamers who want to keep an eye on chat while gaming or for users who want a minimal, unobtrusive chat client.

![Application Screenshot][(https://prnt.sc/d5prBtppCMSX)
![Client Screenshot] (https://prnt.sc/HCn1KDj-cYLZ)

---

## ✨ Features

-   **Frameless:** A minimal interface that doesn't get in the way of your game or other content.
-   **Always on Top:** The chat window remains visible over all other applications.
-   **Extensive Customization:**
    -   Adjustable window size (width and height).
    -   Configurable font size for chat text.
    -   Adjustable window opacity (from 0% to 100%).
-   **Multi-Language Support:** Settings interface available in English, Turkish, French, Russian, Chinese, and Korean.
-   **Advanced Positioning:**
    -   Place the window in 6 preset positions (corners and middle-sides).
    -   A configurable hotkey to quickly cycle through all positions.
    -   Nudge the window pixel-by-pixel using configurable hotkeys (defaults to arrow keys).
-   **Persistent Settings:** All your preferences (channel, size, position, hotkeys) are automatically saved in `settings.json` and loaded on the next launch.
-   **Dynamic Filtering:** Uses JavaScript to hide unwanted elements from the Kick chat webpage for a cleaner view.

---

## 🚀 Getting Started

There are two ways to use this application. The easy way for most users, and the developer way for those who want to run from the source code.

### For Users (Recommended)

This is the easiest way to get started. No installation required.

1.  Go to the [**Releases Page**](https://github.com/alituranakt/Advanced-Kick-Chat-Overlay/releases) of this repository.
2.  Under the latest release (e.g., `v1.0`), find the **Assets** section.
3.  Download the `KickChatOverlay.exe` file.
4.  Run the downloaded file. That's it!

### For Developers (Running from Source)

If you want to run the application from the source code, you'll need Python 3 installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/alituranakt/Advanced-Kick-Chat-Overlay.git](https://github.com/alituranakt/Advanced-Kick-Chat-Overlay.git)
    cd Advanced-Kick-Chat-Overlay
    ```

2.  **(Optional but Recommended) Create a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python kick_overlay.py
    ```

---

## 🛠️ How to Use

After launching the application, the settings window will appear:

1.  **Kick Channel Name:** Enter the name of the Kick channel you want to view.
2.  **Customization:** Adjust the Resolution, Font Size, and Window Opacity to your liking.
3.  **Positioning:** Choose a preset position from the dropdown menu.
4.  **Hotkeys:** Configure your preferred keyboard shortcuts for cycling positions and nudging the window.
5.  Click the **"SAVE SETTINGS & LAUNCH"** button.

The settings window will close, and the chat overlay will appear on your screen with your chosen settings. You can then use the hotkeys to adjust the window during use.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
