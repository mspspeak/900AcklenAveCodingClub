

*Problem 1*

Sedbit log 20780909, Neptune orbit.

I have been a prisoner on an ancient spacecraft for 6 weeks.

Luckily I was able to wire my way out of my cell.  I can sneak out every couple days to raid the ship for supplies.  Something great happened the other day:  I figured out where the security post is.  

I was able to sneak in when Tim the security guard is asleep and get access to the ancient linux computer controlling the cameras and also to how the 8 airlocks open and close.

I know airlock 5 leads to the hanger bay where my ship is stashed.

That's the door I need to open.

That's also the door I need to watch because Tim will come back in through that door.

Here's my plan:

I have to wait for him to leave his post.

Run a series of programs in the security post.

Rush down and hide near airlock 5.  There's a spacesuit closet where I can get a suit and hide.

Wait for Tim to come back inside.

A minute later my programs will put the cameras near airlock 5 on a loop and open the locked airlock door so I can escape.  

I have three programs.

The first program runs the other two every minute.  (Linux can do this for me.)

The second program reads a file and looks through the contents and if it sees the information that tells it that airlock 5 is open, it prints out the escape sequence 8AR7W98.  There's a text file on the system that contains characters.  Each character is ascii encoded.  8-bits.  Each bit is a 0 or 1.  0 means the door is shut.  1 means the door is open.  The fifth bit is from the right... so 00010000 would be the fifth door open.  10000000 is the 8th door open.  11111111 is all eight doors open.  I found a printable ascii table in my archives.

https://i.pinimg.com/474x/7a/80/4b/7a804be53c3c44ee6b32ef956f11b658.jpg

It looks like there are several characters that could mean the 5th bit is on.  So I'll need to watch for one of those and if I see it, print out the escape sequence.

The third program is listening to the second program and when it sees the escape sequence, it will send me a notification near airlock 5 that the door just opened.  Then a minute later, it will turn the camera loop on and open the door.  (I've cobbled this together with old shell commands.)

I've just got to code this second program if I want to escape.

Sedbit out.

Directions

You will be writing the second program Sedbit needs.

The computer running the security system is a very old computer scavenged from the 2020s.  

It's capable of running any code you can run today on a current computer.

Here's what your program needs to do:

- reads a text file

- go through all the text data in the file and look to see if the fifth bit is set.

- if it's set, output the escape sequence.  (Think print statement or console out or whatever's appropriate to your code.)

Have fun! 

Hopefully Sedbit will escape.  This part is up to you!

matt







