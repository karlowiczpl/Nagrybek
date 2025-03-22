import pygame
from .dialogue import Dialog

class FightDialog(Dialog):
    def __init__(self, dialog_text, who, window):
        super().__init__(dialog_text, who, window)
        self._wid
