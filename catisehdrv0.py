import tkinter as tk
from tkinter import ttk, font
import threading
import time
import random

# =============================================================================
# CURSOR CLONE x CAT'S IDE MERGE
# =============================================================================
# Visuals: Anysphere Cursor (Dark, Sidebar, File Tree, Split Panes)
# Logic: Windows 11 Style Agents (Creator, Coder, Researcher, Reasoner)
# Interaction: Terminal-style streaming text (Matrix Green text effect)

class Theme:
    # Cursor / VS Code Dark Modern Palette
    BG_MAIN = "#0F0F0F"       # Deep dark background
    BG_SIDEBAR = "#181818"    # Slightly lighter for side panels
    BG_EDITOR = "#0F0F0F"     # Editor background
    BG_INPUT = "#2B2D31"      # Input fields
    FG_PRIMARY = "#CCCCCC"    # Main text
    FG_SECONDARY = "#8B949E"  # Comments/dimmed text
    BORDER = "#2B2D31"        # Subtle borders
    
    # Text Streaming Color
    TERMINAL_TEXT = "#23D18B" # Matrix/Terminal Green
    
    # Agent Brand Colors (From Cat's IDE)
    AGENT_CREATOR = "#ff8c00"    # Orange
    AGENT_CODER = "#107c10"      # Green
    AGENT_RESEARCHER = "#9c27b0" # Purple
    AGENT_REASONER = "#e91e63"   # Pink
    ACCENT = "#3794FF"           # Default Cursor Blue

class CursorIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Cursor Clone • Agent Edition")
        self.root.geometry("1600x1000")
        self.root.configure(bg=Theme.BG_MAIN)
        
        self.current_agent = "Coder" # Default agent
        
        self.setup_styles()
        
        # Main Container
        self.main_container = tk.Frame(self.root, bg=Theme.BG_MAIN)
        self.main_container.pack(fill="both", expand=True)
        
        # Build UI Sections
        self.build_sidebar()
        self.build_editor_area()
        self.build_chat_panel()
        
        # Initial Content
        welcome_code = (
            "# Welcome to Cursor Agent Edition\n"
            "# Select an Agent on the right to begin.\n\n"
            "def main():\n"
            "    print('System Online')\n"
            "    return True\n"
        )
        self.editor.insert("1.0", welcome_code)
        self.add_chat_message("System", "Select an agent to begin session.", "system")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", 
                      gripcount=0, background=Theme.BG_SIDEBAR, 
                      darkcolor=Theme.BG_MAIN, lightcolor=Theme.BG_MAIN,
                      troughcolor=Theme.BG_MAIN, bordercolor=Theme.BG_MAIN, 
                      arrowcolor=Theme.FG_SECONDARY)

    def build_sidebar(self):
        # --- Activity Bar (Far Left) ---
        activity_bar = tk.Frame(self.main_container, bg=Theme.BG_SIDEBAR, width=50)
        activity_bar.pack(side="left", fill="y")
        activity_bar.pack_propagate(False)
        
        for txt in ["📂", "🔍", "⚡", "⚙️"]:
            lbl = tk.Label(activity_bar, text=txt, bg=Theme.BG_SIDEBAR, 
                           fg=Theme.FG_SECONDARY, font=("Segoe UI", 14))
            lbl.pack(pady=15)

        # --- File Explorer ---
        explorer = tk.Frame(self.main_container, bg=Theme.BG_MAIN, width=220)
        explorer.pack(side="left", fill="y")
        explorer.pack_propagate(False)
        
        tk.Label(explorer, text="EXPLORER", bg=Theme.BG_MAIN, fg=Theme.FG_SECONDARY, 
                 font=("Segoe UI", 8, "bold"), anchor="w").pack(fill="x", padx=15, pady=15)
        
        files = ["main.py", "agent_logic.py", "styles.css", "README.md", "memory.db"]
        for f in files:
            tk.Label(explorer, text=f"  📄 {f}", bg=Theme.BG_MAIN, fg=Theme.FG_PRIMARY, 
                     font=("Segoe UI", 10), anchor="w").pack(fill="x", padx=10, pady=2)
            
        tk.Frame(self.main_container, bg=Theme.BORDER, width=1).pack(side="left", fill="y")

    def build_editor_area(self):
        # --- Center Editor ---
        editor_frame = tk.Frame(self.main_container, bg=Theme.BG_EDITOR)
        editor_frame.pack(side="left", fill="both", expand=True)
        
        # Tab bar
        tab_bar = tk.Frame(editor_frame, bg=Theme.BG_MAIN, height=35)
        tab_bar.pack(fill="x")
        tab_bar.pack_propagate(False)
        
        tab = tk.Label(tab_bar, text=" main.py ", bg=Theme.BG_EDITOR, fg=Theme.FG_PRIMARY, font=("Segoe UI", 10))
        tab.pack(side="left")
        tk.Frame(tab, bg=Theme.ACCENT, height=2).place(x=0, y=0, relwidth=1)

        # Code Editor
        self.editor = tk.Text(editor_frame, 
                            bg=Theme.BG_EDITOR, fg=Theme.FG_PRIMARY, 
                            insertbackground="white", font=("Consolas", 13),
                            selectbackground="#264F78", padx=15, pady=15,
                            borderwidth=0, highlightthickness=0)
        self.editor.pack(fill="both", expand=True)

    def build_chat_panel(self):
        tk.Frame(self.main_container, bg=Theme.BORDER, width=1).pack(side="left", fill="y")

        # --- Right Chat Panel ---
        chat_frame = tk.Frame(self.main_container, bg=Theme.BG_MAIN, width=450)
        chat_frame.pack(side="right", fill="y")
        chat_frame.pack_propagate(False)

        # 1. Agent Selector Header
        header = tk.Frame(chat_frame, bg=Theme.BG_MAIN, height=60)
        header.pack(fill="x", padx=10, pady=5)
        
        self.agent_lbl = tk.Label(header, text="AGENT: Coder", fg=Theme.AGENT_CODER, 
                                bg=Theme.BG_MAIN, font=("Segoe UI", 9, "bold"))
        self.agent_lbl.pack(anchor="w", pady=(5,5))

        # Agent Buttons Row
        btn_frame = tk.Frame(header, bg=Theme.BG_MAIN)
        btn_frame.pack(anchor="w", fill="x")
        
        agents = [
            ("Creator", Theme.AGENT_CREATOR),
            ("Coder", Theme.AGENT_CODER),
            ("Researcher", Theme.AGENT_RESEARCHER),
            ("Reasoner", Theme.AGENT_REASONER),
        ]
        
        for name, color in agents:
            # Styled "Pill" Buttons
            btn = tk.Button(btn_frame, text=name, bg=Theme.BG_INPUT, fg=color,
                          font=("Segoe UI", 8, "bold"), relief="flat", bd=0,
                          activebackground=color, activeforeground="white",
                          command=lambda n=name, c=color: self.switch_agent(n, c))
            btn.pack(side="left", padx=2, ipadx=5, ipady=2)

        # 2. Chat History
        self.chat_display = tk.Text(chat_frame, 
                                  bg=Theme.BG_MAIN, fg=Theme.FG_PRIMARY,
                                  font=("Consolas", 11), wrap="word",
                                  borderwidth=0, highlightthickness=0,
                                  state="disabled", padx=15, pady=10)
        self.chat_display.pack(fill="both", expand=True)
        
        # Tags for Coloring
        self.chat_display.tag_config("user", foreground="white", font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_config("system", foreground=Theme.FG_SECONDARY, font=("Segoe UI", 9, "italic"))
        self.chat_display.tag_config("terminal_content", foreground=Theme.TERMINAL_TEXT)
        
        # Agent Name Tags
        self.chat_display.tag_config("Creator", foreground=Theme.AGENT_CREATOR, font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_config("Coder", foreground=Theme.AGENT_CODER, font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_config("Researcher", foreground=Theme.AGENT_RESEARCHER, font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_config("Reasoner", foreground=Theme.AGENT_REASONER, font=("Segoe UI", 10, "bold"))

        # 3. Input Area
        input_container = tk.Frame(chat_frame, bg=Theme.BG_MAIN)
        input_container.pack(fill="x", padx=15, pady=20)
        
        self.chat_input = tk.Text(input_container, height=4, 
                                bg=Theme.BG_INPUT, fg="white",
                                font=("Segoe UI", 11), insertbackground="white",
                                borderwidth=1, relief="flat", padx=10, pady=10)
        self.chat_input.pack(fill="x")
        self.chat_input.bind("<Return>", self.handle_input)
        self.chat_input.bind("<Shift-Return>", lambda e: "break")

        tk.Label(input_container, text="Ctrl+K to generate, Enter to chat", 
                 bg=Theme.BG_MAIN, fg=Theme.FG_SECONDARY, font=("Segoe UI", 8)).pack(anchor="w", pady=5)

    def switch_agent(self, name, color):
        self.current_agent = name
        self.agent_lbl.config(text=f"AGENT: {name}", fg=color)
        self.add_chat_message("System", f"Switched to {name} Agent.", "system")

    def handle_input(self, event):
        msg = self.chat_input.get("1.0", "end-1c").strip()
        if not msg: return "break"
        
        self.chat_input.delete("1.0", "end")
        self.add_chat_message("You", msg, "user")
        
        # Start AI thread
        threading.Thread(target=self.stream_ai_response, args=(msg,), daemon=True).start()
        return "break"

    def add_chat_message(self, sender, text, tag):
        self.chat_display.config(state="normal")
        if sender:
            # If sender is an agent, use their specific color tag
            label_tag = sender if sender in ["Creator", "Coder", "Researcher", "Reasoner"] else "user"
            self.chat_display.insert("end", f"\n{sender}:\n", label_tag)
        
        # Content always formatted based on type
        content_tag = "terminal_content" if sender not in ["You", "System"] else tag
        self.chat_display.insert("end", f"{text}\n", content_tag)
        
        self.chat_display.config(state="disabled")
        self.chat_display.see("end")

    def stream_ai_response(self, user_query):
        time.sleep(0.4) # Network delay simulation
        
        # Agent Logic from Cat's IDE
        replies = {
            "Creator": [
                "Brainstorming creative solutions...\n> Analyzing aesthetic patterns...\n> Generating design concepts...\n\nHere is a fresh approach:",
                "Visualizing architecture...\n> Sketching interface Mockups...\n\nIdea: What if we made it more organic?"
            ],
            "Coder": [
                "Scanning codebase...\n> accessing main.py\n> optimizing algorithms...\n\nPatch generated successfully:",
                "Debugging runtime...\n> grep -r 'FIXME' .\n> Refactoring legacy functions...\n\nHere is the clean implementation:"
            ],
            "Researcher": [
                "Querying documentation...\n> searching stack_overflow dump\n> cross-referencing API v2.0\n\nAccording to the specs:",
                "Analyzing libraries...\n> comparable modules found: 3\n> reading whitepapers...\n\nBest practice recommendation:"
            ],
            "Reasoner": [
                "Constructing logic tree...\n> premise: user wants terminal style\n> inference: use streaming output\n\nConclusion:",
                "Deep thinking in progress...\n> evaluating edge cases...\n> probability of failure: 0.01%\n\nLogical deduction follows:"
            ]
        }

        # Select Intro
        intro = random.choice(replies.get(self.current_agent, replies["Coder"]))
        
        # Build Body
        body = ""
        if "code" in user_query.lower() or self.current_agent == "Coder":
            code_snippet = (
                "\n\ndef optimized_solution():\n"
                f"    # {self.current_agent} logic applied\n"
                "    process.start()\n"
                "    return True"
            )
            body = code_snippet
        else:
            body = "\n\nOperation complete. Awaiting further directives."

        full_response = intro + body

        # Stream Header (Agent Name)
        self.chat_display.config(state="normal")
        self.chat_display.insert("end", f"\n{self.current_agent}:\n", self.current_agent)
        self.chat_display.config(state="disabled")

        # Stream Content (Terminal Style)
        for char in full_response:
            self.chat_display.config(state="normal")
            self.chat_display.insert("end", char, "terminal_content")
            self.chat_display.config(state="disabled")
            self.chat_display.see("end")
            time.sleep(random.uniform(0.005, 0.025)) # Typewriter speed

        self.chat_display.config(state="normal")
        self.chat_display.insert("end", "\n", "terminal_content")
        self.chat_display.config(state="disabled")
        self.chat_display.see("end")

if __name__ == "__main__":
    root = tk.Tk()
    app = CursorIDE(root)
    root.mainloop()
