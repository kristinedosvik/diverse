source: https://digitalfortress.tech/php/difference-file-mode-0777-vs-777/

mkdir(<folder_name>, <premissions>)

premission = 0777

0 = for interpreting or somthing when using c
7 = 111 = r=1, w=1, x=1 (owner gets read, write and execute premissions)
7 = 111 = rwx (group gets read, write and execute premissions)
7 = 111 = rwx (other users get read, write and execute premissions)
