#!/usr/bin/env python

from github import Github as gh



repo = gh.get_repo('https://github.com/glennhh/8000.git')
print( repo.get_topics() )










