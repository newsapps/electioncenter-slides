# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "building-with-tarbell"

# Descriptive title of project
TITLE = "Building websites with Tarbell"

# Google spreadsheet key
SPREADSHEET_KEY = "0Ak3IIavLYTovdEV5NXNmMktOZzlrUzAzS2NHd1JWYWc"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt", "docs/*", "slides/*"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "tarbell.tribapps.com/build-with-tarbell",
    "staging": "apps.beta.tribapps.com/build-with-tarbell",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': '2014-primaries',
    'title': '2014 Primaries'
}
