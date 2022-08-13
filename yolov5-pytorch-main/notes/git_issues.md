# git相关问题

[TOC]



## 本地和GitHub上同时修改信息

### 本地和GitHub上同时修改文件内容

- 当你在GitHub上修改信息后，在本地也修改，那么就会出现报错，git不知道是以本地修改的为主还是以GitHub上修改的为主，解决办法如下：
  1. git status  查看修改信息
  2. git stash 将修改内容保存到堆栈中
  3. git pull 将本地仓库更新到最新
  4. git stash pop 将堆栈中的修改应用到当前的分支
  5. git status 再查看一下，有需要可以手动修改，即修改需要push的文件（夹）内容
  6. git push  推送到GitHub上

### 本地git push出现 everything up_to_date

- 最大的原因是，你在git commit时 -m 你写成 =m 或者其他，反正就是没有正常commit上去，重新commit就好啦，其他影响还没遇到，友友们自行百度，嘻~