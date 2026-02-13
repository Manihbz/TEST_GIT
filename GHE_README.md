# GHE Instance Information

This repository includes a utility script to identify your GitHub Enterprise (GHE) instance.

## Usage

Run the script to display your current GitHub instance information:

```bash
python3 ghe_instance.py
```

## What it does

The script will:
1. Read your git remote configuration
2. Parse the remote URL
3. Identify whether you're using GitHub.com or a GitHub Enterprise instance
4. Display the instance hostname

## Example Output

For a repository on GitHub.com:
```
==================================================
GitHub Enterprise Instance Information
==================================================

Remote URL: https://github.com/Manihbz/TEST_GIT

GitHub Instance: github.com
Type: GitHub.com (Public)

==================================================
```

For a repository on GHE:
```
==================================================
GitHub Enterprise Instance Information
==================================================

Remote URL: https://ghe.example.com/myorg/myrepo

GitHub Instance: ghe.example.com
Type: GitHub Enterprise (GHE)

Your GHE instance is: ghe.example.com

==================================================
```

## Requirements

- Python 3.x
- Git repository with a configured remote
