# GitHub Enterprise (ghe.com) Instance Support

This repository includes support for working with GitHub Enterprise instances, particularly those hosted on `*.ghe.com` domains.

## Overview

The `ghe_config.py` module provides configuration and utilities for connecting to and working with GitHub Enterprise instances.

## Features

- Support for GitHub.com (public) and GitHub Enterprise instances
- Automatic API URL construction for GHE instances
- Authentication header management
- Support for both GitHub Enterprise Cloud (*.ghe.com) and Server instances

## Usage

### Basic Example

```python
from ghe_config import create_ghe_config

# Configure for a GHE instance
ghe = create_ghe_config(
    hostname='company.ghe.com',
    token='ghp_your_token_here'
)

# Get API URL for an endpoint
repos_url = ghe.get_api_url('/repos/owner/repo')
print(f'API URL: {repos_url}')

# Get authentication headers
headers = ghe.get_headers()
print(f'Headers: {headers}')

# Check if it's a GHE instance
if ghe.is_ghe_instance():
    print('This is a GitHub Enterprise instance')
```

### Using with GitHub.com

```python
from ghe_config import create_ghe_config

# Default configuration uses GitHub.com
github = create_ghe_config()
api_url = github.get_api_url('/user')
# Returns: https://api.github.com/user
```

### Using with GHE Cloud (*.ghe.com)

```python
from ghe_config import create_ghe_config

# For GHE Cloud instances
ghe = create_ghe_config(hostname='mycompany.ghe.com')
api_url = ghe.get_api_url('/repos/owner/repo')
# Returns: https://mycompany.ghe.com/api/v3/repos/owner/repo
```

## Configuration

The `GHEConfig` class accepts the following parameters:

- `hostname` (str, optional): The GHE instance hostname (e.g., 'company.ghe.com'). Defaults to 'api.github.com' for public GitHub.
- `token` (str, optional): Personal access token for authentication.

## API URL Construction

The module automatically constructs the correct API URL based on the hostname:

- **GitHub.com**: `https://api.github.com`
- **GHE Cloud (*.ghe.com)**: `https://<hostname>/api/v3`
- **GHE Server**: `https://<hostname>/api/v3`

## Testing

Run the module directly to see example usage:

```bash
python ghe_config.py
```

This will demonstrate configuration for both GitHub.com and a GHE instance.

## Requirements

No additional dependencies are required beyond Python 3.x standard library.

## Security Notes

- Never commit access tokens to version control
- Use environment variables or secure credential storage for tokens
- Ensure your GHE instance URL is correct before making API calls
