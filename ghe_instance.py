#!/usr/bin/env python3
"""
GHE Instance Information Utility

This script helps identify and display GitHub Enterprise (GHE) instance information.
"""

import os
import subprocess
import sys


def get_git_remote_url():
    """Get the git remote URL from the current repository."""
    try:
        result = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def parse_ghe_instance(url):
    """Parse the GHE instance from a git remote URL."""
    if not url:
        return None
    
    # Remove git@ prefix and .git suffix if present
    url = url.replace('git@', '').replace('.git', '')
    
    # Remove protocol if present
    for protocol in ['https://', 'http://', 'ssh://']:
        if url.startswith(protocol):
            url = url.replace(protocol, '')
    
    # Extract the host (first part before /)
    parts = url.split('/')
    if parts:
        host = parts[0].split(':')[0]  # Remove port if present
        return host
    
    return None


def main():
    """Main function to display GHE instance information."""
    print("=" * 50)
    print("GitHub Enterprise Instance Information")
    print("=" * 50)
    
    # Get the remote URL
    remote_url = get_git_remote_url()
    
    if not remote_url:
        print("\nError: Could not find git remote URL.")
        print("Make sure you're in a git repository with a remote configured.")
        sys.exit(1)
    
    print(f"\nRemote URL: {remote_url}")
    
    # Parse the instance
    instance = parse_ghe_instance(remote_url)
    
    if instance:
        print(f"\nGitHub Instance: {instance}")
        
        # Determine if it's GHE or GitHub.com
        if instance == 'github.com':
            print("Type: GitHub.com (Public)")
        else:
            print(f"Type: GitHub Enterprise (GHE)")
            print(f"\nYour GHE instance is: {instance}")
    else:
        print("\nError: Could not parse instance from remote URL.")
        sys.exit(1)
    
    print("\n" + "=" * 50)


if __name__ == '__main__':
    main()
