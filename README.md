# music-module

A python library extension for Ci40 using a Buzz Click. Adds notes and rests to quickly put simple (very high pitched!) tunes together.

Requires pyletmecreate from [here](https://github.com/francois-berder/PyLetMeCreate). Also requires a Buzz Click board attached to Mikrobus 1.

Put mm.py and your script in the same directory. Just add "import mm" to the top of your script. Call functions within your python script as follows:

<pre>
mm.set_f7()
mm.quarter_play()
</pre>
