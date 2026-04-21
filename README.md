# IB Gateway Trading

Interactive Brokers (IBKR) Gateway docker for easy trading API integration.

## Overview

This project provides dockerfile and verification script for automated trading using Interactive Brokers' Gateway API.

## Files

- `docker-compose.yml` - Docker configuration for running IB Gateway
- `.env.example` - Example environment variables file
- `ivp.py` - Installation Verification Procedure script

## Setup

1. Copy `.env.example` to `.env` and fill in your credentials
2. Install dependencies (Docker or OrbStack)
3. Configure IB Gateway settings as needed

## Usage

1. Run docker image in background
```bash
docker compose up -d
```

2. Run the IVP script:
```bash
python ivp.py
```

## Configuration

Environment variables are loaded from `.env` file. Refer to `.env.example` for required variables.

## Disclaimer

Trading involves risk. Use at your own risk. This software is for educational purposes only.
