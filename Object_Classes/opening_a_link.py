#!/usr/bin/python3

"""This file will open a youtube link or any other link"""
"""it shows how objects can be used in real life"""

import webbrowser

class Browser:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def openLink(self):
        """opens the link given"""
        webbrowser.open(self.link)

web = Browser("web", "https://www.youtube.com/watch?v=2IMM3rb7qsU&ab_channel=DailyRecitationTVHD")

web.openLink()
