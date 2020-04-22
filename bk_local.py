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

currPath = os.path.dirname(os.path.realpath(__file__)) 
repoSumPath = '/home/cloudlab/Data/repos/'     
repoFolder = repoSumPath + 'repos'    
usr = 'cloudlab'  
pwd = 'jianwei@1'   


def printRepoList( repos ):
    for repo in repos:   
        url = 'https://github.com/' + str(repo.full_name)    
        print( url ) 
 
def checkStock( x ):  
    # get current repos  
    #print( 'current repos : ', os.listdir( repoFolder ) ) 
    if x in os.listdir( repoFolder ):   
        return 1  
    return 0

  
def downloadRepos( repos, outputPath ):  
    #i, j = 0, len(repos)  
    i = 0 
    for rep in repos:
        i = i+1
    print( 'i is : ', i ) 

    for repo in repos:   
        print( repo )  
        return 0  
        #i = i + 1   
        #print('Processing ', i, '/', j) 
        if checkStock(repo):
            continue 
        url = 'https://github.com/' + str(repo.full_name)    
        print( url ) 
        if 'tree/master' in url:   
            url = url.replace( 'tree/master', 'trunk' ) 
        #git.Git(repoFolder).clone(url)  
        #remote.RemoteClient(url).export( outputPath )   
        clone = 'git clone ' + url + ".git" + ' &'  
        os.system("sshpass -p pwd ssh usr@localhost")
        os.chdir(repoFolder)                     # Specifying the path where the cloned project needs to be copied
        os.system(clone)                         # Cloning  
        

def search_github(keywords):
    #date = [ 'created:>2020-01-01', 
             #'created:2019-06-01..2020-01-01', 'created:2019-01-01..2019-06-01', 
             #'created:2018-06-01..2019-01-01', 'created:2018-01-01..2018-06-01', 
             #'created:2017-06-01..2018-01-01', 'created:2017-01-01..2017-06-01',
    date = [ 'created:2020-04-01..2020-05-01', 'created:2020-05-01..2020-06-01', 
             'created:2020-02-01..2020-03-01', 'created:2020-03-01..2020-04-01', 
             'created:2019-12-01..2020-01-01', 'created:2020-01-01..2020-02-01' 
           ]  
    re = []  
    for Tseg in date:   
        query = '+'.join(keywords) + '+in:readme+in:description' + '+' + Tseg  
        #repos = git.search_repositories(query, 'stars', 'desc')
        repos = git.search_repositories(query)
        re.append(repos)   
        print(f'Found {repos.totalCount} repo(s)')  
        #print( re[0].contents ) 
        #print( re[1].contents )  
         
        downloadRepos( repos, repoFolder )   
    #print( re[0].contents ) 
    #print( re[1].contents )  

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

    with open( currPath + '/words.txt', 'r') as words:  
        for line in words:
            keywords = line.strip()            #   ['go', 'cloud', 'AWS']   
            print(keywords)  
            repos = search_github( keywords )   
            #printRepoList( repos )               
 
            #downloadRepos( repos, repoFolder )   



