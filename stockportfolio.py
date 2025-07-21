#!/usr/bin/env python3
"""
Stock Portfolio Tracker (manual prices)
• User enters ticker & quantity pairs
• Prices are hard‑coded
• Total value printed and optionally stored
"""

PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 135.0,
    "MSFT": 420.0,
    "AMZN": 130.0,
}

import csv
from pathlib import Path


def get_positions():
    positions = {}
    print("Enter positions (blank ticker to finish)")
    while True:
        ticker = input("Ticker: ").strip().upper()
        if not ticker:
            break
        qty = input("Quantity: ").strip()
        if not qty.isdigit():
            print("Quantity must be a whole number.")
            continue
        positions[ticker] = positions.get(ticker, 0) + int(qty)
    return positions


def calc_value(positions):
    total = 0.0
    for tkr, qty in positions.items():
        price = PRICES.get(tkr)
        if price is None:
            print(f"⚠️  {tkr} not in price table (skipped).")
            continue
        total += price * qty
    return total


def maybe_save(positions, total):
    choice = input("Save results to CSV? [y/N] ").strip().lower()
    if choice != "y":
        return
    fname = Path("portfolio_value.csv")
    with fname.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Quantity", "Price", "Value"])
        for tkr, qty in positions.items():
            price = PRICES.get(tkr, 0)
            writer.writerow([tkr, qty, price, price * qty])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", total])
    print(f"💾  Saved to {fname.absolute()}")


def main():
    positions = get_positions()
    total = calc_value(positions)
    print(f"\n📈  Portfolio value: ${total:,.2f}")
    maybe_save(positions, total)


if __name__ == "__main__":
    main()
