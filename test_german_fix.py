#!/usr/bin/env python3

import sys
import os

# Add the markitdown package to the path
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), 'markitdown', 'packages', 'markitdown', 'src'
))

from markitdown.converters._pdf_converter import fix_german_encoding

# Test the fix function with various examples
test_cases = [
    "Leitfaden f�r den erfolgreichen KI-Start im Mittelstand",
    "�  Analyse: Status von Daten",
    "� Copyright 2025, Das Lizenz Atelier GmbH & Co. KG",
    "M�hlenbergstra�e 6, 28876 Oyten, Germany",
    "Die folgenden Module sind frei w�hlbar und kombinierbar",
    "k�nnen die Module individuell zusammengestellt werden",
    "mit dem Modul �Ausgangspunkt kl�ren� zu beginnen"
]

for test_text in test_cases:
    print("Original:", repr(test_text))
    print("Fixed:   ", repr(fix_german_encoding(test_text)))
    print()