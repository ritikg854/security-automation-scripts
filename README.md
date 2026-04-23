# Security Automation Scripts

This repository contains small, practical security automation scripts designed to support analyst workflows, investigation tasks, and security operations learning.

## Purpose

The purpose of this repository is to showcase simple technical projects that are relevant to SOC, blue-team, and cybersecurity analyst roles.

## Focus Areas

- IOC extraction
- Log handling
- Investigation support
- Analyst workflow automation
- Practical security scripting

## Current Contents

- `scripts/ioc_extractor.py` - a simple script to extract potential indicators of compromise such as IP addresses, domains, URLs, and email addresses from text
- `examples/sample_iocs.txt` - sample input file for testing the IOC extractor

## Current Script

- `ioc_extractor.py` - extracts potential indicators of compromise such as IP addresses, domains, URLs, and email addresses from a block of text

## Repository Structure

- `scripts/` - small security automation scripts
- `examples/` - sample input files used to test and demonstrate scripts

## Usage

Each script in this repository is designed as a small practical example of how automation can support cybersecurity analysis and security operations tasks.

## How to Run

Run the IOC extractor script with a sample input file:

```bash
python scripts/ioc_extractor.py examples/sample_iocs.txt
