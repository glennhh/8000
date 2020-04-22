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
#repoFolder = repoSumPath + 'repos'    
usr = 'cloudlab'  
pwd = 'jianwei@1'   

repoSize = '30000'   # repo size limit   
repoAm = 50       # repo amount to download   



def findPath(searchwords): 
    keywords = searchwords.split(' ')   
    if 'go' in keywords[1]:
        return repoSumPath + keywords[1].split(':')[1] + '/' + keywords[2] + '/'     
    elif 'java' in keywords[1]:  
        return repoSumPath + keywords[1].split(':')[1] + '/' + keywords[2]  + '/'      
    elif 'python' in keywords[1]:
        return repoSumPath + keywords[1].split(':')[1] + '/' + keywords[2] + '/'   
    else: 
        return repoSumPath + 'other/'   


def printRepoList( repos ):
    for repo in repos:   
        url = 'https://github.com/' + str(repo.full_name)    
        print( url ) 
 
def checkStock( x, path ):  
    # get current repos  
    #print( 'current repos : ', os.listdir( repoFolder ) ) 
    if x in os.listdir( path ):   
        return 1  
    return 0
  
def downloadRepos( repos, outputPath ):  
    i = 0 
    print( 'Start downloading ... ' ) 
    for repo in repos:   
        i = i+1  
        if i == repoAm:           # repoAm   
            return 1  
        if checkStock( repo, outputPath ):
            continue 
        url = 'https://github.com/' + str(repo.full_name)    
        if 'tree/master' in url:   
            url = url.replace( 'tree/master', 'trunk' ) 
        #git.Git(repoFolder).clone(url)  
        #remote.RemoteClient(url).export( outputPath )   
        clone = 'git clone ' + url + ".git" + ' &'  
        os.system("sshpass -p pwd ssh usr@localhost")
        os.chdir( outputPath )                     # Specifying the path where the cloned project needs to be copied
        os.system( '@echo off; ' + clone)                         # Cloning  
        

def search_github(keywords):
    #date = [ 'created:>2020-01-01', 
             #'created:2019-06-01..2020-01-01', 'created:2019-01-01..2019-06-01', 
             #'created:2018-06-01..2019-01-01', 'created:2018-01-01..2018-06-01', 
             #'created:2017-06-01..2018-01-01', 'created:2017-01-01..2017-06-01',
    #date = [ 'created:2020-04-01..2020-05-01', 'created:2020-05-01..2020-06-01', 
             #'created:2020-02-01..2020-03-01', 'created:2020-03-01..2020-04-01', 
             #'created:2019-12-01..2020-01-01', 'created:2020-01-01..2020-02-01' 
    #re = []  
    #for Tseg in date:   
        #query = '+'.join(keywords) + '+in:readme+in:description' + '+' + Tseg 
        query = keywords + ' in:readme in:description size:<' + repoSize + ' '   
        repos = git.search_repositories(query, 'stars', 'desc')    
        print( query )  
        #repos = git.search_repositories(query)
        #re.append(repos)   
        print(f'Found {repos.totalCount} repo(s)')  
        #print( re[0].contents ) 
        #print( re[1].contents )  
        return repos

if __name__ == '__main__':
    #keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')

    with open( currPath + '/words.txt', 'r') as words:  
        for line in words:
            keywords = line.strip()             #   ['go', 'cloud', 'AWS']   
            #print(keywords)  
            repos = search_github( keywords )   
            #printRepoList( repos )               
            outputPath = findPath( keywords )  
            downloadRepos( repos, outputPath )   


