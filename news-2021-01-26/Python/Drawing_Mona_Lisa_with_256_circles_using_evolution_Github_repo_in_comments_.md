Drawing Mona Lisa with 256 circles using evolution [Github repo in comments]
============================================================================

[Github] https://github.com/ahmedkhalf/Circle-Evolution

Please note that this is a very early and undocumented version. I plan on adding color, and improving speed, then later putting it on PyPI. Push requests are appreciated :)

Use floyd-warshall algorithm bro. It will be really fast.

Shouldn't you move this render:

https://github.com/ahmedkhalf/Circle-Evolution/blob/master/circle_evolution/evolution.py#L75

....outside the loop? Each time you loop there is only one image created and so only one render is required.

It may result in a small speedup.

This is great.

It gets a really good match, especially if you unfocus your eyes / squint / look out the corner of your eyes. Then your brain doesn’t get distracted by the circles and just sees the shading.

I’d suggest at you include a requirements.txt or a Pipfile so other people can more easily use the code and see what packages you installed.

Will do this when I have time, thanks for the suggestion.

Id say its 99.65% of a Mona Lisa and that ain't bad.

or even just paste it into REAME.MD file :) nothing fancy, but still does the job well

Love that the solver couldn't figure out Mona Lisa's smile either

It found a near optimal solution with 256 circles.

Give it 5000 circles, and it'd work out an almost exact copy, lips included.

Haha! Came to say this.

Fun project! Congrats! I didn't read the code, yet I'm wondering: what kind of compression rate do you achieve?

Theoretically, because we are dealing with a 256*256 image, we can store each parameter in a single byte.

We are dealing with 256 genes (circles), and each gene has 5 parameters (x, y, radius, color, transparency). Therefore that is a total of 1,280 bytes (256*5) without metadata. The grayscale jpg is 23,085 bytes. We saved around 95% disk space.

Please note that all of this is theoretical, I did not try it. Also, this is a very lossy (and time-consuming) compression.

How to learn it? Every time I try to get involved into machine lerning it's so overwhelming. Where to start? Do I have to get deep mathematic understanding?

Although a lot of people associate genetic evolution with machine learning, I don't believe this to be the case. This is because with genetic evolution you aren't really teaching a machine, you are basically brute-forcing but in a "smart way". Everything was done in raw python (that is, no ML library) and the most complicated math I used was squaring. I recommend you take a look at the code posted above. I will also update the repo in the future and include detailed documentation.

Start from this project and start reading artificial intelligence a modern approach. It's the chapter about genetic algorithms.

Evolutionary algorithms are very different to machine learning - as OP said.

Here's basically how this evolutionary algorithm works.

Have 100 'Individuals' (each individual is it's own picture)

For each Individual, draw 256 circles (random location, random opacity, random blackness)

So now we have 100 sets of 256 random circles.

EVOLUTION TIME!!!

Now we grade the 'fitness' of each individual. Fitness is basically how 'correct' it is. In this, that's pretty easy to do. We just compare every pixel of the Individuals image, to the Mona Lisa.

Now we have 100 individuals with a 'fitness' score from 0 to 100.

We delete the 90 worst individuals.

We now have 10 indivudals, lets call them A,B,C,D,E,etc

Then, using breeding and mutation, we create 90 new individuals from the 10 remaining individuals. There are no strict rules about how you do this (as far as I know).

We will breed A+B, A+C, A+D, etc to create children, which will be new individuals. Child individuals inherit 'traits' from their parents. What are the parents traits? The 256 circles. So the child will randomly get 128 of the circles from one parent, and 128 of the circles from the other parent.

Mutation is exactly what it sounds like. Lets take individual A, and randomly change 12 of its circles.

Through mutation and breeding, we now have 100 individuals again.

EVOLUTION TIME!!!

Now we just keep doing the same thing, over and over and over. Score the fitness of the 100 individuals. Kill the 90 worst. Breed and mutate. Repeat. Thousands and thousands of times.

And eventually, you'll get the Mona Lisa.

As I said, it's up to the programmer how to do it. How many individuals? How much do you mutate? How do you breed (maybe you take more traits from a more fit parent)?

In terms of OP, I think the top left image is showing the fittest individual from every generation.

I recall a real world example of how these can be used is for doing timetables at universities - to ensure the least amount of 'clashing' classes for students.

I found this course from Harvard a while ago, it’s free and goes into a lot of detail (and it’s with python!). They even have a forum to ask anything about the course if you get stuck. Imo this is a pretty good place to start.

https://www.edx.org/course/cs50s-introduction-to-artificial-intelligence-with-python

Pythonistas

Online

Powerups
--------

Powerup and unlock perks for r/Python
-------------------------------------

### Community heroes

#### makedatauseful

#### CyberNaruto

#### Lord_Ryn

#### Nijadeen

#### fliplink1

#### BardsArentReal

#### Rum_And_Monkey

#### Head-Sick

#### gschizas

#### DeeeRooooo

#### 1010100111001001

#### smooverebel

#### brendanator55

#### JangoBeastwood

#### Im__Joseph

#### OvenCookedDepression

#### forgot_username1

#### cicloid

#### ghostiewm

#### Scotty770

#### squizzeak

#### hasecbinusr

#### belinux

#### ajurna

#### StrangeCalibur

#### AntennaBoy

#### steder

#### garchangel

#### mithra62

#### pooroldluu

#### ADarkcid

#### Sharkbait05

#### inflightfailure

#### pATREUS

#### jrobelen

#### pnkme45q

#### riskfighter

#### LikeALincolnLog42

#### PepperedBacon

#### JimmiPopMyinty

#### Angelsinger74

#### lululombard

#### c0224v2609

#### Tiraun

#### vape-naysh-420

#### Kamikazeq

#### lachiendupape

#### chaoscruz

#### xlordsnugglesx

#### dfndoe