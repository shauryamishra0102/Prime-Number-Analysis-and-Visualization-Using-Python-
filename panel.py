# panel.py

import wx
from primes import generate_primes, is_prime
from visualizer import visualize_prime_scatter, visualize_ulam_spiral
from utils import ensure_folders
from config import MAX_LIMIT


class PrimePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        ensure_folders()

        vbox = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="PRIME VISUALIZER")
        title.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD
            )
        )
        vbox.Add(title, 0, wx.ALL | wx.CENTER, 10)

        # Buttons
        btn_generate = wx.Button(self, label="Generate Primes")
        btn_check = wx.Button(self, label="Check Prime")
        btn_scatter = wx.Button(self, label="Prime Scatter Plot")
        btn_ulam = wx.Button(self, label="Ulam Spiral")
        btn_exit = wx.Button(self, label="Exit")

        vbox.Add(btn_generate, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(btn_check, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(btn_scatter, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(btn_ulam, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(btn_exit, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(vbox)

        # Bind events
        btn_generate.Bind(wx.EVT_BUTTON, self.on_generate_primes)
        btn_check.Bind(wx.EVT_BUTTON, self.on_check_prime)
        btn_scatter.Bind(wx.EVT_BUTTON, self.on_scatter)
        btn_ulam.Bind(wx.EVT_BUTTON, self.on_ulam)
        btn_exit.Bind(wx.EVT_BUTTON, self.on_exit)

    # ---- Helper ----
    def validate_input(self, value):
        try:
            n = int(value)
            if n < 2:
                raise ValueError
            if n > MAX_LIMIT:
                wx.MessageBox(
                    f"Maximum allowed value is {MAX_LIMIT}",
                    "Limit Exceeded",
                    wx.OK | wx.ICON_WARNING
                )
                return None
            return n
        except ValueError:
            wx.MessageBox(
                "Please enter a valid integer greater than 1.",
                "Invalid Input",
                wx.OK | wx.ICON_ERROR
            )
            return None

    # ---- Button functions ----

    def on_generate_primes(self, event):
        dlg = wx.TextEntryDialog(self, "Generate primes up to:", "Generate Primes")

        if dlg.ShowModal() == wx.ID_OK:
            n = self.validate_input(dlg.GetValue())
            if n is None:
                dlg.Destroy()
                return

            primes = generate_primes(n)

            prime_text = (
                f"Generated {len(primes)} primes up to {n}\n\n"
                + ", ".join(map(str, primes))
            )

            result_dlg = wx.Dialog(self, title="Prime Numbers", size=(600, 400))
            vbox = wx.BoxSizer(wx.VERTICAL)

            text_ctrl = wx.TextCtrl(
                result_dlg,
                value=prime_text,
                style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
            )

            vbox.Add(text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
            result_dlg.SetSizer(vbox)

            result_dlg.ShowModal()
            result_dlg.Destroy()

        dlg.Destroy()

    def on_check_prime(self, event):
        dlg = wx.TextEntryDialog(self, "Enter number to check:", "Prime Check")

        if dlg.ShowModal() == wx.ID_OK:
            n = self.validate_input(dlg.GetValue())
            if n is None:
                dlg.Destroy()
                return

            msg = f"{n} is a PRIME number" if is_prime(n) else f"{n} is NOT a prime number"
            wx.MessageBox(msg, "Result", wx.OK | wx.ICON_INFORMATION)

        dlg.Destroy()

    def on_scatter(self, event):
        dlg = wx.TextEntryDialog(self, "Visualize primes up to:", "Prime Scatter")

        if dlg.ShowModal() == wx.ID_OK:
            n = self.validate_input(dlg.GetValue())
            if n is None:
                dlg.Destroy()
                return

            visualize_prime_scatter(n)

        dlg.Destroy()

    def on_ulam(self, event):
        dlg = wx.TextEntryDialog(self, "Generate Ulam spiral up to:", "Ulam Spiral")

        if dlg.ShowModal() == wx.ID_OK:
            n = self.validate_input(dlg.GetValue())
            if n is None:
                dlg.Destroy()
                return

            visualize_ulam_spiral(n)

        dlg.Destroy()

    def on_exit(self, event):
        self.GetParent().Close()
