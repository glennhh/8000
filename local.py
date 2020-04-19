#!/usr/bin/env python

import os 
import sys  
from github import Github 
import validators 
#from svn import remote
#import git  

git = Github('glennhh', 'jianwei@1')  

#repo = git.get_repo('https://github.com/glennhh/8000.git')

#####################################
###   parameter
#####################################  

#currPath = os.path.dirname(os.path.realpath(__file__)) 
currPath = '/home/cloudlab/Data/repos/'     
repoFolder = currPath + 'repos'    
usr = 'cloudlab'  
pwd = 'jianwei@1'   


def downloadRepos( repos, outputPath ):  
    for repo in repos:   
        url = 'https://github.com/' + str(repo.full_name)    
        print( url ) 
        if 'tree/master' in url:
            url = url.replace( 'tree/master', 'trunk' ) 
        #git.Git(repoFolder).clone(url)  
        #remote.RemoteClient(url).export( outputPath )   
        clone = 'git clone ' + url + ".git" 
        os.system("sshpass -p pwd ssh usr@localhost")
        os.chdir(repoFolder) # Specifying the path where the cloned project needs to be copied
        os.system(clone) # Cloning

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    repos = git.search_repositories(query, 'stars', 'desc')
    return repos   
      


    print(f'Found {repos.totalCount} repo(s)')
    '''
    for repoName in repos:  
        repo = git.get_repo(repoName.full_name)   
        print('repo is : ', repo) 
        for files in repo.get_contents(""): 
            while files:  
                print(files)  
                fileContent = files.pop(0)  
                if fileContent.type == "dir": 
                    files.extent( repo.get_contents( filecontent.path ) )  
                else:  
                    print(fileContant) 
     '''

if __name__ == '__main__':
    #keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = ['go', 'cloud', 'AWS'] 

    repos = search_github( keywords )  
    
    downloadRepos( repos, repoFolder )   

