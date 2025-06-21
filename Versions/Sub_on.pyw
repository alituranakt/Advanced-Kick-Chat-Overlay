import webview
import tkinter as tk
from tkinter import messagebox
import sys
import re
import ctypes
import json
import os
import threading
import keyboard

# Ayar dosyasının adı
SETTINGS_FILE = 'settings.json'

# DİL VERİLERİ
LANGUAGES = {'tr': {'display_name': 'Türkçe', 'window_title': 'Kick Chat Overlay Ayarları', 'lang_label': 'Dil:', 'channel_label': 'Kick Kanal Adı:', 'resolution_label': 'Çözünürlük (Genişlik x Yükseklik):', 'font_size_label': 'Yazı Tipi Boyutu (px):', 'position_label': 'Pencere Konumu:', 'hotkey_label': 'Konum Döngü Kısayolu:', 'hotkey_example': 'Örn: ctrl+shift+x, alt+k', 'nudge_hotkeys_label': 'Pencere Kaydırma Kısayolları', 'nudge_labels': ['Yukarı:', 'Aşağı:', 'Sol:', 'Sağ:'], 'start_button': 'AYARLARI KAYDET & BAŞLAT', 'error_title': 'Hata', 'error_invalid_channel': 'Lütfen geçerli bir kanal adı girin.', 'error_invalid_resolution': 'Lütfen geçerli bir sayısal değer girin.', 'positions': ['Üst-Sağ', 'Üst-Sol', 'Alt-Sağ', 'Alt-Sol', 'Orta-Sağ', 'Orta-Sol']}, 'en': {'display_name': 'English', 'window_title': 'Kick Chat Overlay Settings', 'lang_label': 'Language:', 'channel_label': 'Kick Channel Name:', 'resolution_label': 'Resolution (Width x Height):', 'font_size_label': 'Font Size (px):', 'position_label': 'Window Position:', 'hotkey_label': 'Position Cycle Hotkey:', 'hotkey_example': 'e.g., ctrl+shift+x, alt+k', 'nudge_hotkeys_label': 'Window Nudge Hotkeys', 'nudge_labels': ['Up:', 'Down:', 'Left:', 'Right:'], 'start_button': 'SAVE SETTINGS & LAUNCH', 'error_title': 'Error', 'error_invalid_channel': 'Please enter a valid channel name.', 'error_invalid_resolution': 'Please enter a valid numeric value.', 'positions': ['Top-Right', 'Top-Left', 'Bottom-Right', 'Bottom-Left', 'Middle-Right', 'Middle-Left']}, 'fr': {'display_name': 'Français', 'window_title': "Paramètres de l'overlay de chat Kick", 'lang_label': 'Langue :', 'channel_label': 'Nom de la chaîne Kick :', 'resolution_label': 'Résolution (Largeur x Hauteur) :', 'font_size_label': 'Taille de la police (px) :', 'position_label': 'Position de la fenêtre :', 'hotkey_label': 'Raccourci de Cycle de Position :', 'hotkey_example': 'ex: ctrl+shift+x, alt+k', 'nudge_hotkeys_label': 'Raccourcis de Déplacement de Fenêtre', 'nudge_labels': ['Haut :', 'Bas :', 'Gauche :', 'Droite :'], 'start_button': 'ENREGISTRER & LANCER', 'error_title': 'Erreur', 'error_invalid_channel': 'Veuillez entrer un nom de chaîne valide.', 'error_invalid_resolution': 'Veuillez entrer une valeur numérique valide.', 'positions': ['Haut-Droite', 'Haut-Gauche', 'Bas-Droite', 'Bas-Gauche', 'Milieu-Droite', 'Milieu-Gauche']}, 'ru': {'display_name': 'Русский', 'window_title': 'Настройки оверлея чата Kick', 'lang_label': 'Язык:', 'channel_label': 'Название канала Kick:', 'resolution_label': 'Разрешение (Ширина x Высота):', 'font_size_label': 'Размер шрифта (пикс.):', 'position_label': 'Позиция окна:', 'hotkey_label': 'Горячая клавиша цикла:', 'hotkey_example': 'пример: ctrl+shift+x, alt+k', 'nudge_hotkeys_label': 'Клавиши перемещения окна', 'nudge_labels': ['Вверх:', 'Вниз:', 'Влево:', 'Вправо:'], 'start_button': 'СОХРАНИТЬ И ЗАПУСТИТЬ', 'error_title': 'Ошибка', 'error_invalid_channel': 'Пожалуйста, введите корректное название канала.', 'error_invalid_resolution': 'Пожалуйста, введите корректное числовое значение.', 'positions': ['Справа-Сверху', 'Слева-Сверху', 'Справа-Снизу', 'Слева-Снизу', 'Справа-Посередине', 'Слева-Посередине']}, 'zh': {'display_name': '简体中文', 'window_title': 'Kick 聊天悬浮窗设置', 'lang_label': '语言:', 'channel_label': 'Kick 频道名称:', 'resolution_label': '分辨率 (宽度 x 高度):', 'font_size_label': '字体大小 (像素):', 'position_label': '窗口位置:', 'hotkey_label': '位置切换快捷键:', 'hotkey_example': '例如: ctrl+shift+x, alt+k', 'nudge_hotkeys_label': '窗口微调快捷键', 'nudge_labels': ['上:', '下:', '左:', '右:'], 'start_button': '保存并启动', 'error_title': '错误', 'error_invalid_channel': '请输入有效的频道名称。', 'error_invalid_resolution': '请输入有效的数值。', 'positions': ['右上', '左上', '右下', '左下', '右中', '左中']}, 'ko': {'display_name': '한국어', 'window_title': 'Kick 채팅 오버레이 설정', 'lang_label': '언어:', 'channel_label': 'Kick 채널 이름:', 'resolution_label': '해상도 (너비 x 높이):', 'position_label': '창 위치:', 'hotkey_label': '위치 순환 단축키:', 'hotkey_example': '예: ctrl+shift+x, alt+k', 'nudge_hotkeys_label': '창 이동 단축키', 'nudge_labels': ['위:', '아래:', '왼쪽:', '오른쪽:'], 'start_button': '저장하고 시작하기', 'error_title': '오류', 'error_invalid_channel': '유효한 채널 이름을 입력하세요.', 'error_invalid_resolution': '유효한 숫자 값을 입력하세요.', 'positions': ['오른쪽-위', '왼쪽-위', '오른쪽-아래', '왼쪽-아래', '오른쪽-중간', '왼쪽-중간']}}
POSITION_KEYS = ["top_right", "top_left", "bottom_right", "bottom_left", "middle_right", "middle_left"]

class KickOverlayApp:
    def __init__(self):
        self.window = None
        self.root = None
        self.settings = self.load_settings()
        self.hotkey_thread = None
        
        self.lang_code = self.settings.get('language', 'tr')
        self.strings = LANGUAGES.get(self.lang_code, LANGUAGES['en'])
        self.positions = self.strings['positions']
        
        user32 = ctypes.windll.user32
        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)

        self.setup_gui()

    def load_settings(self):
        # DÜZELTME: Varsayılan kaydırma tuşları yön tuşları olarak ayarlandı.
        defaults = {
            "channel_name": "", "width": 320, "height": 330, "font_size": 11,
            "position_key": "bottom_right", "cycle_hotkey": "-", "language": "eng",
            "hotkey_up": "up",
            "hotkey_down": "down",
            "hotkey_left": "left",
            "hotkey_right": "right"
        }
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                    loaded_settings = json.load(f)
                    defaults.update(loaded_settings)
            except (json.JSONDecodeError, TypeError):
                pass
        return defaults

    def save_settings(self):
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4, ensure_ascii=False)

    def _change_language(self, choice):
        new_lang_code = 'en'
        for code, data in LANGUAGES.items():
            if data['display_name'] == choice:
                new_lang_code = code
                break
        if new_lang_code != self.settings.get('language'):
            self.settings['language'] = new_lang_code
            self.save_settings()
            self.root.destroy()
            self.__init__()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title(self.strings['window_title'])
        self.root.geometry("400x650") 
        self.root.resizable(False, False)
        self.root.configure(bg="#0E0C13")
        
        lang_frame = tk.Frame(self.root, bg="#0E0C13")
        lang_frame.pack(pady=5, padx=10, anchor='e')
        tk.Label(lang_frame, text=self.strings['lang_label'], font=("Arial", 10), fg="white", bg="#0E0C13").pack(side=tk.LEFT)
        lang_display_names = [LANGUAGES[lc]['display_name'] for lc in sorted(LANGUAGES.keys())]
        self.lang_var = tk.StringVar(self.root)
        self.lang_var.set(self.strings['display_name'])
        lang_menu = tk.OptionMenu(lang_frame, self.lang_var, *lang_display_names, command=self._change_language)
        lang_menu.config(font=("Arial", 8))
        lang_menu.pack(side=tk.LEFT)

        tk.Label(self.root, text="KICK CHAT OVERLAY", font=("Arial", 18, "bold"), fg="#53FC18", bg="#0E0C13").pack(pady=5)
        
        input_frame = tk.Frame(self.root, bg="#0E0C13")
        input_frame.pack(pady=10, fill="x", padx=20)
        
        tk.Label(input_frame, text=self.strings['channel_label'], font=("Arial", 12), fg="white", bg="#0E0C13").pack()
        self.channel_entry = tk.Entry(input_frame, font=("Arial", 12), width=28, justify=tk.CENTER)
        self.channel_entry.pack(pady=(5, 10))
        self.channel_entry.insert(0, self.settings.get('channel_name', ''))

        res_font_frame = tk.Frame(input_frame, bg="#0E0C13")
        res_font_frame.pack(pady=5)
        
        tk.Label(res_font_frame, text=self.strings['resolution_label'], font=("Arial", 12), fg="white", bg="#0E0C13").pack()
        resolution_frame = tk.Frame(res_font_frame, bg="#0E0C13")
        resolution_frame.pack(pady=5)
        self.width_entry = tk.Entry(resolution_frame, font=("Arial", 10), width=8, justify=tk.CENTER)
        self.width_entry.pack(side=tk.LEFT, padx=5)
        self.width_entry.insert(0, str(self.settings.get('width')))
        tk.Label(resolution_frame, text="x", font=("Arial", 10), fg="white", bg="#0E0C13").pack(side=tk.LEFT)
        self.height_entry = tk.Entry(resolution_frame, font=("Arial", 10), width=8, justify=tk.CENTER)
        self.height_entry.pack(side=tk.LEFT, padx=5)
        self.height_entry.insert(0, str(self.settings.get('height')))

        tk.Label(res_font_frame, text=self.strings['font_size_label'], font=("Arial", 12), fg="white", bg="#0E0C13").pack(pady=(10,0))
        self.font_size_entry = tk.Entry(res_font_frame, font=("Arial", 10), width=8, justify=tk.CENTER)
        self.font_size_entry.pack(pady=5)
        self.font_size_entry.insert(0, str(self.settings.get('font_size')))

        tk.Label(input_frame, text=self.strings['position_label'], font=("Arial", 12), fg="white", bg="#0E0C13").pack(pady=(10, 0))
        self.position_var = tk.StringVar(self.root)
        current_pos_key = self.settings.get('position_key', 'top_right')
        try:
            current_pos_display = self.strings['positions'][POSITION_KEYS.index(current_pos_key)]
        except (ValueError, IndexError):
            current_pos_display = self.strings['positions'][0]
        self.position_var.set(current_pos_display)
        position_menu = tk.OptionMenu(input_frame, self.position_var, *self.positions)
        position_menu.config(font=("Arial", 10), width=15)
        position_menu.pack(pady=5)

        tk.Label(input_frame, text=self.strings['hotkey_label'], font=("Arial", 12), fg="white", bg="#0E0C13").pack(pady=(10, 0))
        self.hotkey_entry = tk.Entry(input_frame, font=("Arial", 10), width=20, justify=tk.CENTER)
        self.hotkey_entry.pack(pady=5)
        self.hotkey_entry.insert(0, self.settings.get('cycle_hotkey'))
        tk.Label(input_frame, text=self.strings['hotkey_example'], font=("Arial", 8), fg="#666666", bg="#0E0C13").pack()
        
        nudge_frame = tk.LabelFrame(self.root, text=" " + self.strings.get('nudge_hotkeys_label', "Pencere Kaydırma Kısayolları") + " ", bg="#0E0C13", fg="#AAAAAA", padx=10, pady=10)
        nudge_frame.pack(pady=10, padx=20, fill="x")
        nudge_labels = self.strings.get('nudge_labels', ["Yukarı:", "Aşağı:", "Sol:", "Sağ:"])
        
        self.hotkey_up_entry = tk.Entry(nudge_frame, font=("Arial", 10), width=20, justify=tk.CENTER)
        self.hotkey_down_entry = tk.Entry(nudge_frame, font=("Arial", 10), width=20, justify=tk.CENTER)
        self.hotkey_left_entry = tk.Entry(nudge_frame, font=("Arial", 10), width=20, justify=tk.CENTER)
        self.hotkey_right_entry = tk.Entry(nudge_frame, font=("Arial", 10), width=20, justify=tk.CENTER)

        hotkey_entries = [self.hotkey_up_entry, self.hotkey_down_entry, self.hotkey_left_entry, self.hotkey_right_entry]
        setting_keys = ['hotkey_up', 'hotkey_down', 'hotkey_left', 'hotkey_right']

        for i, label in enumerate(nudge_labels):
            tk.Label(nudge_frame, text=label, font=("Arial", 10), fg="white", bg="#0E0C13").grid(row=i, column=0, sticky="w", pady=2)
            hotkey_entries[i].grid(row=i, column=1, padx=10)
            hotkey_entries[i].insert(0, self.settings.get(setting_keys[i]))

        self.root.bind('<Return>', lambda e: self.start_overlay())
        tk.Button(self.root, text=self.strings['start_button'], font=("Arial", 11, "bold"), bg="#53FC18", fg="black", width=25, height=2, command=self.start_overlay).pack(pady=10)
        
        self.root.mainloop()

    def start_overlay(self):
        try:
            selected_pos_display = self.position_var.get()
            pos_index = self.strings['positions'].index(selected_pos_display)
            self.settings['position_key'] = POSITION_KEYS[pos_index]
        except ValueError:
            self.settings['position_key'] = 'top_right'

        self.settings['channel_name'] = self.channel_entry.get().strip()
        self.settings['cycle_hotkey'] = self.hotkey_entry.get().strip().lower()
        self.settings['hotkey_up'] = self.hotkey_up_entry.get().strip().lower()
        self.settings['hotkey_down'] = self.hotkey_down_entry.get().strip().lower()
        self.settings['hotkey_left'] = self.hotkey_left_entry.get().strip().lower()
        self.settings['hotkey_right'] = self.hotkey_right_entry.get().strip().lower()

        if not self.settings['channel_name'] or not re.match(r'^[a-zA-Z0-9_]{3,25}$', self.settings['channel_name']):
            messagebox.showerror(self.strings['error_title'], self.strings['error_invalid_channel'])
            return
        
        try:
            self.settings['width'] = int(self.width_entry.get())
            self.settings['height'] = int(self.height_entry.get())
            self.settings['font_size'] = int(self.font_size_entry.get())
        except ValueError:
            error_msg = self.strings.get('error_invalid_resolution', 'Please enter valid numeric values.')
            messagebox.showerror(self.strings['error_title'], error_msg)
            return

        self.save_settings()
        self.root.destroy()
        self.create_overlay_window()

    def _calculate_coordinates(self, position_key, win_width, win_height):
        OFFSET = 8
        x, y = 0, 0
        
        if "left" in position_key: x = 0 - OFFSET
        elif "right" in position_key: x = self.screen_width - win_width

        if "top" in position_key: y = 0 - OFFSET
        elif "bottom" in position_key: y = self.screen_height - win_height + OFFSET
        elif "middle" in position_key: y = (self.screen_height / 2) - (win_height / 2)
            
        return int(x), int(y)

    def _cycle_position(self):
        try:
            current_index = POSITION_KEYS.index(self.settings.get('position_key', 'top_right'))
            next_index = (current_index + 1) % len(POSITION_KEYS)
            self.settings['position_key'] = POSITION_KEYS[next_index]
            new_x, new_y = self._calculate_coordinates(self.settings['position_key'], self.settings['width'], self.settings['height'])
            if self.window: self.window.move(new_x, new_y)
        except Exception as e:
            print(f"Konum değiştirilirken hata: {e}")
    
    def _nudge_window(self, dx=0, dy=0):
        if self.window:
            self.window.move(self.window.x + dx, self.window.y + dy)

    def _hotkey_listener(self):
        try:
            cycle_hotkey = self.settings.get('cycle_hotkey', '')
            if cycle_hotkey: keyboard.add_hotkey(cycle_hotkey, self._cycle_position)
            
            nudge_amount = 1
            hotkey_up = self.settings.get('hotkey_up', '')
            if hotkey_up: keyboard.add_hotkey(hotkey_up, lambda: self._nudge_window(dy=-nudge_amount))
            hotkey_down = self.settings.get('hotkey_down', '')
            if hotkey_down: keyboard.add_hotkey(hotkey_down, lambda: self._nudge_window(dy=nudge_amount))
            hotkey_left = self.settings.get('hotkey_left', '')
            if hotkey_left: keyboard.add_hotkey(hotkey_left, lambda: self._nudge_window(dx=-nudge_amount))
            hotkey_right = self.settings.get('hotkey_right', '')
            if hotkey_right: keyboard.add_hotkey(hotkey_right, lambda: self._nudge_window(dx=nudge_amount))

            keyboard.wait()
        except Exception as e:
            print(f"Kısayol kaydedilemedi: {e}")

    def create_overlay_window(self):
        win_width, win_height = self.settings['width'], self.settings['height']
        position_key = self.settings.get('position_key', 'top_right')
        font_size = self.settings.get('font_size', 14)
        x, y = self._calculate_coordinates(position_key, win_width, win_height)
        
        self.hotkey_thread = threading.Thread(target=self._hotkey_listener, daemon=True)
        self.hotkey_thread.start()
        
        js_code_to_inject = f"""
        setTimeout(() => {{
            function getElementByXPath(path) {{ 
                return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; 
            }}
            // DÜZELTME: Yeni filtre listeye eklendi.
            const pathsToRemove = [
                '/html/body/div/div[2]/div/div/div',
                '/html/body/div/div[1]/div/div[1]',
                '/html/body/div/div[1]/div/div/div[1]',
                '/html/body/div/div[1]/div/div/div[1]/div[1]',
                '/html/body/div/div[1]/div/div/div[2]',
                '/html/body/div/div[1]/div/div[2]/div[1]/div[2]/div/div[26]/div'
            ];
            pathsToRemove.forEach(path => {{
                const element = getElementByXPath(path);
                if (element && element.parentNode) {{ 
                    element.parentNode.removeChild(element); 
                }}
            }});

            if (document.documentElement) {{
                document.documentElement.style.setProperty('--chatroom-font-size', '{font_size}px');
            }}

        }}, 3000);
        """
        
        def inject_js(window):
            window.evaluate_js(js_code_to_inject)

        try:
            self.window = webview.create_window(
                f"Kick Chat - {self.settings['channel_name']}",
                f"https://kick.com/popout/{self.settings['channel_name']}/chat",
                width=win_width, height=win_height, x=x, y=y,
                resizable=True, on_top=True, transparent=True, frameless=True
            )
            webview.start(inject_js, self.window)
        except Exception as e:
            messagebox.showerror(self.strings['error_title'], f"Window creation error: {e}")

def main():
    KickOverlayApp()

if __name__ == "__main__":
    main()