iniread
=======

Read simple ini file in popular script languages.

Contents:
--------
- config   - directory with a config sample
- direct   - examples of direct reading of a config - useful when only one
           script in a given language is being used
- imported - examples of usage when a script imports a module which reads
           a config - useful when few scripts in a given language shares
           the configuration and you do like the "DRY" principle.

Description:
-----------
If you ever faced the situation when few scripts in few languages had
to read a shared configuration file then this simple project is just
what you need.

I had bash, php and python scripts and an .ini file with a few variables - 
mostly the credentials for the database. I didn't want to repeat myself.
Quick googling gave me an answer for each language but no cross-language
solution. This project is an answer. Feel free and use it wherever you need.


Other languages:
---------------
Pull requests for new languages are welcomed but keep in mind that simplicity
is the key, so do not do too much checking or "universal" parsers - this
project is crafted for simple shell scripts sharing their config.

It can be done a lot better in a more universal way but... then it will be 
unreadable and therefore - useless for the key use case.


Project info:
------------
This code has been cloned from a GIT repository on GitHub:
https://github.com/chesteroni/iniread

It is licensed with the MIT License. 
Should you have any questions, please feel free to contact me via an email. 
