# main.py
# Entry point for the wxPython Prime Visualizer application

import wx
from panel import PrimePanel


class PrimeApp(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title="Prime Visualizer",
            size=(400, 350)
        )

        # Attach the main panel (contains all 5 buttons & logic hooks)
        PrimePanel(self)

        # Center window on screen and show
        self.Centre()
        self.Show()


def main():
    app = wx.App(False)
    frame = PrimeApp()
    app.MainLoop()


if __name__ == "__main__":
    main()
