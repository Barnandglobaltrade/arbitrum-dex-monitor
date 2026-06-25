# arbitrum-dex-monitor
Simple Python tool to monitor real-time WETH/USDC prices on Arbitrum using Foundry/Cast.
# Arbitrum DEX Monitor

A simple, lightweight Python tool to monitor real-time WETH/USDC prices on the Arbitrum network using Foundry/Cast.

## How it works
This script fetches the `sqrtPriceX96` from the Uniswap V3 pool contract on Arbitrum and calculates the current price of WETH in USDC.

## Prerequisites
- Foundry (specifically the `cast` tool)
- Python 3

## Usage
Run the monitoring script in your terminal:
```bash
python monitor.py
