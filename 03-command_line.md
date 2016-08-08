# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

time command	See how long a command takes
cd -	Go to previous directory
ls -lrt	List files by date. See also newest and find_mm_yyyy
rsync -P rsync://rsync.server.com/path/to/file file	Only get diffs. Do multiple times for troublesome downloads
sed 's/string1/string2/g'	Replace string1 with string2
sort -u file1 file2	Union of unsorted files
sort file1 file2 | uniq -d	Intersection of unsorted files
sort file1 file1 file2 | uniq -u	Difference of unsorted files
sort file1 file2 | uniq -u	Symmetric Difference of unsorted files
join -t'\0' -a1 -a2 file1 file2	Union of sorted files
join -t'\0' file1 file2	Intersection of sorted files
join -t'\0' -v2 file1 file2	Difference of sorted files
join -t'\0' -v1 -v2 file1 file2	Symmetric Difference of sorted files

---

###Q2.  List Files in Unix   
What do the following commands do:  
`ls`  -- lists directories contents of files and directories
`ls -a`   -- Include directory entries whose names begin with a dot (.) Write a slash (`/') after each filename if that file is a directory.
`ls -l`  -- List in long format - show permissions
`ls -lh`  -- list long format with readable file size
`ls -lah` -- list long format with readable file size & Include directory entries whose names begin with a dot (.) Write a slash (`/') after each filename if that file is a directory. 
`ls -t`  -- Sort by time and date
`ls -Glp`  -- inhibit display of group information. List in long format - show permissions, append indicator (one of /=@|) to entries


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-c	Displays files by file timestamp.
-m	Displays the names as a comma-separated list.
-L	Displays the file or directory referenced by a symbolic link.
-R	Displays subdirectories as well.
-t	Displays newest files first. (based on timestamp)

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.


xargs command in unix or Linux is a powerful command used in conjunction with find and grep command in UNIX to divide a big list of arguments into small list received from standard input. find and grep command produce long list of file names and we often want to either remove them or do some operation on them but many unix operating system doesn't accept such a long list of argument. 




devuser@system:/etc find . -name "*bash*"
./bash.bashrc
./bash.bash_logout
./defaults/etc/bash.bashrc
./defaults/etc/bash.bash_logout
./defaults/etc/skel/.bashrc
./defaults/etc/skel/.bash_profile
./postinstall/bash.sh.done
./setup/bash.lst.gz
./skel/.bashrc
./skel/.bash_profile

devuser@system:/etc find . -name "*bash*" | xargs
./bash.bashrc ./bash.bash_logout ./defaults/etc/bash.bashrc ./defaults/etc/bash.bash_logout ./defaults/etc/skel/.bashrc ./defaults/etc/skel/.bash_profile ./postinstall/bash.sh.done ./setup/bash.lst.gz ./skel/.bashrc ./skel/.bash_profile


 

