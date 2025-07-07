---
id: 213
title: Moving a file from a local computer to a server through a jump server
date: 2016-05-20T02:25:12+00:00
author: mrbusche
permalink: /2016/05/20/moving-a-file-from-a-local-computer-to-a-server-through-a-jump-server/
categories:
  - linux
tags:
  - linux
  - scp
  - ssh
---

This is a problem I've been routinely facing at work because we have new firewall rules and can only access new servers through a jump box. Accessing the server through ssh isn't a problem after I've ssh'd into the jump server, but moving a file from my local computer to the other server is a pain. What you need to do is move the file from your local computer to an accesible directory on the jump server. For me this involves using [WinSCP](https://winscp.net/eng/download.php) to drag and drop the file to my /home/mbusche directory.

Once the file has been moved to the jump server you need to use the [scp command](https://docs.oracle.com/cd/E26502_01/html/E29001/remotehowtoaccess-55154.html) to move the file from the jump server to the other server. In my case the command looks something like this.

    scp /home/mubusche/sonar.jar mbusche@cvms1255:/home/mbusche/

The syntax is

    scp fileLocationOnCurrentServer username@servername:folderLocationToMoveFile/

Now generally you won't have write access to all folders under your username and may need to sudo in as another user to move the file to the directory you need. To do that you need to login to the destination server via ssh, sign in as a user with permissions and then move the folder

    ssh serverName
    sudo su - userWithAccess
    sudo mv /home/mbusche/sonar.jar /webdata/plugins/
