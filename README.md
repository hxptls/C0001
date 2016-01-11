A short url getter of github.com.
================
####C0001####

****************

|Code ID    |0001           |
|:---------:|:--------------|
|Author     |Hexapetalous   |
|Date       |Jan 11, 2015   |
|Satisfied  |Yes            |
|OS         |elementary OS 0.3.2 Freya (64-bit)                 |
|Hardware   |Dual-Core Intel(R) Core(TM) i5-4288U CPU @ 2.60GHz |
|Language   |Python3        |
|Dependence |requests       |
|IDE        |PyCharm        |

****************

The idea of `C0001` came from a junior of mine when he show me his github account which is a strange string. "What's that mean?" I wondered. "No meaning. Just because it has a great shortened url."

That was true. [http://git.io/T](http://git.io/T). I love that.

So this is a program that can help you to find out which shortened url has not been used and what does it refers to.

    $ python3 slot_machine.py 
    http://git.io/! -> https://github.com/joshdk/././
    http://git.io/& -> https://github.com/zeebo/.
    http://git.io/* -> https://github.com/joshdk/././.
    http://git.io/1 -> https://github.com/sotarok/heala
    http://git.io/2 -> https://github.com/easy-websocket
    http://git.io/= -> https://github.com/justecorruptio/Snatch 
    http://git.io/E -> https://github.com/Detry322/././
    ...

Some of them maybe useless to you. But, who knows?

****************

**TODO LIST**

-   Deal with errors and exceptions.
-   It seems like a strange algorithm transfer a regular url to a shortened one. Figure it out.

****************

Copyright &copy; 2016 Hexapetalous. All rights reserved.