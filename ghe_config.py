"""
GitHub Enterprise Configuration Module

This module provides configuration and utilities for working with
GitHub Enterprise (GHE) instances, particularly those hosted on
*.ghe.com domains.
"""

class GHEConfig:
    """Configuration class for GitHub Enterprise instances."""
    
    def __init__(self, hostname=None, token=None):
        """
        Initialize GHE configuration.
        
        Args:
            hostname (str): The GHE instance hostname (e.g., 'company.ghe.com')
            token (str): Personal access token for authentication
        """
        self.hostname = hostname or 'api.github.com'
        self.token = token
        self.base_url = self._build_base_url()
    
    def _build_base_url(self):
        """Build the base API URL for the GHE instance."""
        if self.hostname == 'api.github.com':
            return f'https://{self.hostname}'
        else:
            # GitHub Enterprise Cloud (*.ghe.com) and Server instances
            return f'https://{self.hostname}/api/v3'
    
    def get_api_url(self, endpoint):
        """
        Get the full API URL for a given endpoint.
        
        Args:
            endpoint (str): API endpoint path
            
        Returns:
            str: Full API URL
        """
        endpoint = endpoint.lstrip('/')
        return f'{self.base_url}/{endpoint}'
    
    def get_headers(self):
        """
        Get authentication headers for API requests.
        
        Returns:
            dict: Headers dictionary with authentication
        """
        headers = {
            'Accept': 'application/vnd.github.v3+json',
        }
        if self.token:
            headers['Authorization'] = f'token {self.token}'
        return headers
    
    def is_ghe_instance(self):
        """
        Check if this is a GitHub Enterprise instance.
        
        Returns:
            bool: True if GHE instance, False if github.com
        """
        return self.hostname != 'api.github.com'
    
    def __repr__(self):
        """String representation of the config."""
        return f'GHEConfig(hostname={self.hostname}, base_url={self.base_url})'


def create_ghe_config(hostname=None, token=None):
    """
    Factory function to create a GHE configuration.
    
    Args:
        hostname (str): The GHE instance hostname
        token (str): Personal access token
        
    Returns:
        GHEConfig: Configured GHE instance
    """
    return GHEConfig(hostname=hostname, token=token)


# Example usage
if __name__ == '__main__':
    # Example: GitHub.com (public)
    github_config = create_ghe_config()
    print(f'GitHub.com config: {github_config}')
    print(f'API URL for repos: {github_config.get_api_url("/repos/owner/repo")}')
    
    # Example: GitHub Enterprise instance
    ghe_config = create_ghe_config(hostname='company.ghe.com', token='ghp_example_token')
    print(f'\nGHE config: {ghe_config}')
    print(f'API URL for repos: {ghe_config.get_api_url("/repos/owner/repo")}')
    print(f'Is GHE instance: {ghe_config.is_ghe_instance()}')
