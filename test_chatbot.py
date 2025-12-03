#!/usr/bin/env python3
"""
Quick test script to verify chatbot functionality
"""

import json
from datetime import datetime

print("=" * 60)
print("🤖 CHATBOT IA - TEST SCRIPT")
print("=" * 60)
print()

# Test 1: Check if generateSimulatedResponse works
test_messages = [
    "Bonjour",
    "Quelle heure est-il?",
    "Quelle date sommes-nous?",
    "Python",
    "Merci",
    "Qui es-tu?",
]

print("📋 Test Cases pour generateSimulatedResponse:")
print("-" * 60)

for msg in test_messages:
    print(f"\n✓ Input: '{msg}'")
    # Les réponses seraient générées en JavaScript, on affiche juste ce qui devrait arriver
    if "heure" in msg.lower():
        now = datetime.now()
        print(f"  Expected: Il est {now.strftime('%H:%M')} ⏰")
    elif "date" in msg.lower():
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        print(f"  Expected: Nous sommes le {date_str} 📅")
    elif "bonjour" in msg.lower():
        print(f"  Expected: Bonjour! 👋 Comment puis-je vous aider...")
    elif "python" in msg.lower():
        print(f"  Expected: Python est un excellent choix!...")
    elif "merci" in msg.lower():
        print(f"  Expected: De rien! 😊 Y a-t-il autre chose...")
    elif "qui es-tu" in msg.lower():
        print(f"  Expected: Je suis votre assistant La Tour! 🤖...")

print("\n" + "=" * 60)
print("✅ Test Script Complete")
print("=" * 60)
print()
print("📖 How to verify:")
print("1. Open F12 (Developer Tools)")
print("2. Go to Console tab")
print("3. Look for [Chatbot] logs")
print("4. Test manually in chatbox")
print()
