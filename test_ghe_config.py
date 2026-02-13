"""
Unit tests for GHE configuration module.
"""

import unittest
from ghe_config import GHEConfig, create_ghe_config


class TestGHEConfig(unittest.TestCase):
    """Test cases for GHEConfig class."""
    
    def test_default_github_config(self):
        """Test default configuration uses GitHub.com."""
        config = GHEConfig()
        self.assertEqual(config.hostname, 'api.github.com')
        self.assertEqual(config.base_url, 'https://api.github.com')
        self.assertFalse(config.is_ghe_instance())
    
    def test_ghe_cloud_config(self):
        """Test configuration for GHE Cloud instance."""
        config = GHEConfig(hostname='company.ghe.com')
        self.assertEqual(config.hostname, 'company.ghe.com')
        self.assertEqual(config.base_url, 'https://company.ghe.com/api/v3')
        self.assertTrue(config.is_ghe_instance())
    
    def test_ghe_server_config(self):
        """Test configuration for GHE Server instance."""
        config = GHEConfig(hostname='ghe.mycompany.local')
        self.assertEqual(config.hostname, 'ghe.mycompany.local')
        self.assertEqual(config.base_url, 'https://ghe.mycompany.local/api/v3')
        self.assertTrue(config.is_ghe_instance())
    
    def test_get_api_url(self):
        """Test API URL construction."""
        config = GHEConfig(hostname='company.ghe.com')
        
        # Test with leading slash
        url = config.get_api_url('/repos/owner/repo')
        self.assertEqual(url, 'https://company.ghe.com/api/v3/repos/owner/repo')
        
        # Test without leading slash
        url = config.get_api_url('repos/owner/repo')
        self.assertEqual(url, 'https://company.ghe.com/api/v3/repos/owner/repo')
    
    def test_get_headers_without_token(self):
        """Test headers without authentication token."""
        config = GHEConfig()
        headers = config.get_headers()
        self.assertIn('Accept', headers)
        self.assertNotIn('Authorization', headers)
    
    def test_get_headers_with_token(self):
        """Test headers with authentication token."""
        config = GHEConfig(token='ghp_test_token')
        headers = config.get_headers()
        self.assertIn('Accept', headers)
        self.assertIn('Authorization', headers)
        self.assertEqual(headers['Authorization'], 'token ghp_test_token')
    
    def test_factory_function(self):
        """Test factory function for creating config."""
        config = create_ghe_config(hostname='test.ghe.com', token='test_token')
        self.assertEqual(config.hostname, 'test.ghe.com')
        self.assertEqual(config.token, 'test_token')
    
    def test_repr(self):
        """Test string representation of config."""
        config = GHEConfig(hostname='test.ghe.com')
        repr_str = repr(config)
        self.assertIn('GHEConfig', repr_str)
        self.assertIn('test.ghe.com', repr_str)


if __name__ == '__main__':
    unittest.main()
