__Zebiano__  
As I said, having a rooted phone has some perks, like for example creating bash scripts that might do about any action you want. So I created a script (500ish lines) that inputs touches on certain pixels. If you mix that with a quick RGB check on certain pixels as well, you've got yourself a script that competes the daily quests from the afk game. If you're interested I can show you, or you may even try it for yourself. You need a rooted phone though, and it needs to be in the 1920x1080 resolution. The rest should be fine I'd say!

With this in mind, I also wanted to do that for the lab... Though the lab is way harder since it involves choosing which tiles to use, actually fighting with the chance of loosing a fight (which is bad) and the most difficult part: choosing the right cards. Since I only have the RGB from pixels and inputs, it's really hard to make a script that may be able to run the lab. That's why I started thinking about creating one on the pc that might be able to "read" cards, and just have overall more features to play with. 
But then again, if I need to start my pc in order to run the lab, I wouldn't do it, so I'd like to do it on my phone... Idk, still gotta decide :sweat_smile:
And that's where you and your subreddit come into play: knowing where is what for each lab is crucial for a possible script I'd write!
Though again, it's a very slim chance I'd create it on mobile. I guess python would be the best...? I'm not familiar with it though.
 
__FiyaFly__  
I'd love to see that script. That's a great idea that helps actually in a couple things I had in mind for this: comparing pixel values. Would definitely cut down on the amount of screen to analyze. I feel stupid, but I never thought about just doing it in bash. I really should get around to rooting my phone, because that opens a lot of doors for me lol

Python was my first thought as well, especially due to the compatibility of it, but I'm glad you confirmed that thought. I'm a bit rusty, but used to be rather well versed in Python. Wanted to be sure I didn't have the "When all you have is a hammer, everything looks like a nail" mentality for it lol.

I guess a start to think about would be can a rooted android run python? Might not change much, but might help you make the decision on PC or phone lol. If your phone can run python scripts, we could set it up to determine whether it's running on PC or phone.

At the very least, what I'm thinking of that you could do if you wanted to create or recreate it with bash, two options come to mind:

1. I can give you the hex code for the colors I'm using, and you could do an RGB check on the image. I always use the same template, so you could use the resolution as reference to map out what's going on. This option would be useful to get straight to the rest of the interesting stuff to deal with for the lab. lol

2. If we focus on the auto mapper, we could have that output the results in an easier format to parse with a lab run script, as well as obviously output the mapping to post. 

The auto mapper is gonna come with it's own challenges, but especially with you already having some pixel mapping, you might have some better ideas on resolving them.
Two things that could become a problem are that while you're in the lab, the floor can scroll up and down, so having a solid point of reference can't really be relied on, at least not easily. the second thing is that at least the flags (can't remember offhand for the others) are animated, so any RGB checks would have to cover a range as opposed to a set value
 
__Zebiano__  
Can a rooted android run python
I actually think it can. There are some apps/libraries I've read about that make it a possibility. Though idk how "good" it is,bid have to check.

The floor can scroll up and down
Actually, on my phone, when you start the lab, you're all the way down possible. Whenever you end a fight the map doesn't scroll up, you stay where you are. I've tested it, that it's possible to stay down as long as you can, and then scroll all the way to the top and still be able to see your "flag". Hard to explain, but basically: the scrollable map should not be an issue!

The flags are animated
You mean the cards? What. For me they aren't... Oooh I know what you mean. That could become a problem yes, but I'm optimistic, it should still work! 

Now, I actually just quickly thought about the possibility for an auto lab mapper, and it's actually pretty doable! I can for sure return an array of hex values (or an object, don't know) that would tell us where everything is on the lab. It's one/two simple colour check on each individual tile.

The next problem I can think of, is in order to be able to map out the second lab for example, I need to be able to pass the first one right?
Though that should still be doable. I can create a script that checks the current lab I'm at, and then lets me play it. Whenever I pass that floor, I run the script again and he checks the new floor, and so on... That could be an option! I'd actually love to do that :)
 
__Zebiano__  
Tell me a bit more about how you actually do all of the mapping. I'm guessing you run it on bluestacks and just paint the tiles accordingly on paint. But how do you do it for the third floor? Since there are two options... Do you use two accounts?
 
__FiyaFly__  
Yep. Bluestacks, paint, and two accounts. As far as I know there's no other way besides using two accounts. I've got three total, but I've debated either splitting one to a different login (if they permit that) or making a different login with another account. Right now you can't sign into AFK arena from two places on the same login, so basically I have to run my main account through to hard mode, switch accounts, then run my secondary through floor 3. So in that 45 mins I spend making the lab path I'm almost doing two full runs. Lol

I can reply to your other info in a few mins. Not at my PC.
 
__Zebiano__  
Oh I see. Yeah that makes sense... I understand it's quite a tedious job...
 
__FiyaFly__  
It's not terrible overall, but it's unoptimized. lol. 
Long response on the scripting notes so it'll have to be two messages lol:
Though idk how "good" it is,but have to check.

I think as long as it runs, we should be generally good. The only place it might become a problem is which version of Python it can run, but I think we could build it with that in mind.

Whenever you end a fight the map doesn't scroll up, you stay where you are.

Okay, so then yeah you're right we should be able to work around that, as long as there's no external input while it's working to move the screen up. I want to say we should probably try to initiate a check for that as well, but I guess I wouldn't say it's necessary. Just something to keep in mind. That's where a lot of my projects get exponentially bigger usually is miscellaneous error-checking, so that's why I like having someone to run that through lol.

I can for sure return an array of hex values (or an object, don't know) that would tell us where everything is on the lab. It's one/two simple colour check on each individual tile.

My first mental response to that was something along the lines of referencing the amount of different circumstances we'll have to check for and thinking it'd be a bigger check, but the more I think about it, the more I think you're right and we should be able to actually do that pretty decently. We'd have to quantify each circumstance, but with a switch/case statement, we should be able to cover that pretty well I think. Especially if we did a return on the hex/rgb values. I haven't explored it yet, but I think we could probably do a ranged check on those values (as opposed to checking to see if it matches every color it possibly could be). That would tremendously cut down on the code. Basically just checking "Is it some form of red?" instead of "Here's the values of every hue of red it may possibly be. Go." lol.
The next problem I can think of, is in order to be able to map out the second lab for example, I need to be able to pass the first one right?

I don't think that'll be too much of an issue, but I haven't thought out the precise logistics of it. When you're in the lab it tells you at the top which floor you're on: 

Arcane Labyrinth: Hard Mode
Arcane Labyrinth: Floor 1
Arcane Labyrinth: Floor 2
Arcane Labyrinth: Floor 3

If we can read that (OCR maybe? or possibly some color checks, maybe.) Then it can determine for itself where it's at, and we wouldn't have to worry about it. Hell, on the second run we could use it as a verify for the first two floor maps, just to make sure it matches the first run, and if not, throw us a warning so we know something's broken. lol.

I know we'll be able to do it, but the main thing that comes into my head every time I think on the color checks is that there is a decent amount of circumstances to consider. A quick count (may not be entirely accurate, but close) tells me there are 10 possibilities for each tile, give or take:

1. Empty
2. Boss
3. Wagon
4. Fountain
5. Shop
6. Red Flag
7. Brown Flag
8. Hero Res
9. Wrizz
10. Current location

Excluding the last one, each one of those could be in one of three states: white (Next row up), Gray (More than one row up), or highlighted (Tiles that you can select for your next move). so... 28? (3 states on 9 possibilities, plus location)

__Zebiano__  
Thats where a lot of my projects get exponentially bigger usually is miscellaneous error-checking
Same... xD we need to control ourselves ahah

We could probably do a ranged check on those values (the colours)
Honestly, I think (and hope) that won't be necessary. I think it's possible to find that one pixel that even with an animated flag, the hex value won't change. Well have to see.

There are 10 possibilities for each tile
I didn't even think about that... Hm. It's still possible to work around it though, I have an idea in mind, but it's easier to talk about than to write. Maybe we can one day chat? I'm guessin you live in the US because of the server timezone, but we'll be able to find some time. I'm in Europe.

Also, so dope the amount of people! I honestly thought there was one or two more, not all those xD

And yeah, I think discord has some markdown implemented, but not all of it...? Dunno.
So... Wanna chat one day? When do you usually have time? I'm free for the next 3 and half hours I'd say if that suits you. I'd like to discuss just basic things like the ones talked here, just to have an idea what we want and how well do it.
 
__FiyaFly__  
Sheesh. After that second run, I've got this to say: auto-mapping? Yeah I still think we can do it. A script that can run it for you?... Hell, sometimes I can barely get through it myself, so programming the logic for running it for you might be a hefty task...

Mind you, I'm still game for doing just that. Something being difficult just generally means I'm diving headfirst into it faster. lol. But, just as a note, could really take some effort. lol
 
__Zebiano__  
Yep I know...
That's why we should focus first on the auto mapper!
I guess it'll end up being one of those scripts that you use whenever you don't have time for the lab but still want to give it a try. It might not be the best way to try it, but at least floor one you've managed to do. I guess.
We'll see. But let's first focus on the auto mapper!