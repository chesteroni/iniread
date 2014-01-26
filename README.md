iniread
=======

Read simple ini file in popular script languages.

If you ever faced the situation when few scripts in few languages had
to read a shared configuration file then this simple project is just
what you need.

I had bash, php and python scripts and an .ini file with a few variables
- mostly the credentials for the database. I didn't want to repeat myself.
Quick googling gave me an answer for each language but no cross-language
solution. This project is an answer. Feel free and use it wherewer you need.

Pull requests for new languages are welcomed but keep in mind that simplicity
is the key, so do not do too much checking or "universal" parsers - this
project is crafted for simple shell scripts sharing their config.

It can be done a lot better in a more universal way but... then it will be 
unreadable and therefore - useless for the key use case.
