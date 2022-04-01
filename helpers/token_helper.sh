#!/usr/bin/env bash
# This script configures the local validator for test transfers
set -x

solana config set --url d
solana config set --keypair /Users/dusankovacevic/Desktop/tests/devnet-deploy.json

solana airdrop 2

# Mint new tokens owned by our CLI account
spl-token mint "Gssm3vfi8s65R31SBdmQRq6cKeYojGgup7whkw4VCiQj" 10000000000

spl-token transfer "Gssm3vfi8s65R31SBdmQRq6cKeYojGgup7whkw4VCiQj" 100000000 "Cetz5BzrUQzRWtHYwVqUacvvp78CUScUU5LuTAH5WR34" --fund-recipient --allow-unfunded-recipient