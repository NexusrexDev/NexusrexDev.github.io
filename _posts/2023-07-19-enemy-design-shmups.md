---
layout: post
title: "Enemy Design in Shmups"
categories: analysis
excerpt: "An attempt to analyze enemy designs from several shmup games and write them down in a detailed manner!"
---

# A beginning
This post is mainly made as a form of guidance for myself after tackling several shmup games *(Ranging from simple jam entries in the spirit of simple shmups akin to Space Invaders and 1942 and more advanced shmups)* in attempt to understand how a basic enemy unit can be designed, and what cliches can be found in common between said games.

# Let's get into it
An enemy can be divided into 3 phases:
1. Intro
2. Action
3. Departure

## Intro attributes

| Name | Description |
| :-------------: | ------------- |
| **None** | The enemy simply moves into the scene, getting instantly into the *action* phase. <br><br> ![None animation]({{ "/assets/blog_assets/enemy-design-shmups/intro_none.gif" | relative_url }}) <br> <sub>*A forward moving enemy, no intro animation*</sub> |
| **Tween to position** | The enemy tweens into a specific position, usually accompanied by being instantiated in other spots of the screen and different types of tweening to provide interesting effects. <br><br> ![Tween animation]({{ "/assets/blog_assets/enemy-design-shmups/intro_tween.gif" | relative_url }}) <br> <sub>*An enemy tweening to position, linear interpolation and easing in-out*</sub> |
| **Foreground animation** | The enemy has an animation, usually scaling down if coming from the foreground, disabling its hitbox through the animation. <br><br> ![Foreground animation]({{ "/assets/blog_assets/enemy-design-shmups/intro_foreground.gif" | relative_url }}) <br> <sub>*An enemy coming from the foreground, done with 2 tweens*</sub> |
| **Teleport** | The enemy has a teleportation animation before being instantiated/spawned in place of the animation. |
{:.table}

## Action attributes
The action attributes are split into two types:
1. Movement attributes
2. Shooting attributes

The types can be either simultaneous, or focused on one of the types.

### Movement attributes

| Name | Description |
| :-------------: | ------------- |
| **Straight line** | The enemy moves in a straight line. Can be either of a moderate speed, the background’s scrolling speed *(if the enemy is part of the ground/stationary)* or slow to imply heaviness. *(for bullet sponges and bomb-types)* <br><br> ![Straight line animation]({{ "/assets/blog_assets/enemy-design-shmups/intro_none.gif" | relative_url }}) <br> <sub>*An enemy moving in a straight line*</sub> |
| **At player** | The enemy moves in the player’s direction, similar speed traits as the straight line variant. |
| **Sinewave** | The enemy moves in a sine wave vertically while having normal horizontal movement. Multiples can be used to create interesting shapes. *(Wave, reverse sine)* <br><br> ![Sinewave animation]({{ "/assets/blog_assets/enemy-design-shmups/movement_sine.gif" | relative_url }}) <br> <sub>*Enemies moving in a sine wave, one then multiple*</sub> |
| **Zigzag** | The enemy moves forward then up and back before continuing forward to resemble a zigzag shape. <br><br> ![Zigzag animation]({{ "/assets/blog_assets/enemy-design-shmups/movement_zigzag.gif" | relative_url }}) <br> <sub>*An enemy moving in a downwards zigzag*</sub> |
| **Dash** | The enemy moves in a bigger speed than a regular enemy, usually combined with an intro. |
| **Repositioning** | The enemy moves around a set of predefined spots. Can be combined with shooting projectiles after moving through such spots or during every movement. <br><br> ![Repositioning animation]({{ "/assets/blog_assets/enemy-design-shmups/movement_repositioning.gif" | relative_url }}) <br> <sub>*An enemy repositioning across various spots, shooting after stopping at selected times*</sub> |
| **Hovering** | The enemy moves around the scene slowly, usually used for bigger enemies or bosses to stop them from being completely stationary. <br><br> ![Hovering animation]({{ "/assets/blog_assets/enemy-design-shmups/movement_hover.gif" | relative_url }}) <br> <sub>*The closest approximation to such a behavior with a small enemy*</sub> |
{:.table}

### Shooting attributes

| Name | Description |
| :-------------: | ------------- |
| **Straight line** | The enemy shoots a projectile *(or a cluster)* that moves forward. <br><br> ![Straight shot animation]({{ "/assets/blog_assets/enemy-design-shmups/shooting_straightline.gif" | relative_url }}) <br> <sub>*An enemy shooting forward*</sub> |
| **At player** | The enemy shoots a projectile *(or a cluster)* that moves in the player’s direction. <br><br> ![At player animation]({{ "/assets/blog_assets/enemy-design-shmups/shooting_atplayer.gif" | relative_url }}) <br> <sub>*An enemy shooting a cluster in the player’s direction*</sub> |
| **Spread shot** | The enemy shoots more than one projectile at once, spread to shape an arc. The arc’s main angle can be either a forward line, or in a specific direction. *(ie. the player’s)* <br><br> ![Spread shot animation]({{ "/assets/blog_assets/enemy-design-shmups/shooting_spreadshot.gif" | relative_url }}) <br> <sub>*An enemy shooting 3 projectiles*</sub> |
| **Spraying** | The enemy scatters multiple projectiles *(or clusters)* with a brief gap between each projectile, akin to using a machine gun to spray bullets. <br><br> ![Spray shot animation]({{ "/assets/blog_assets/enemy-design-shmups/shooting_spraying.gif" | relative_url }}) <br> <sub>*An enemy spraying 5 projectiles*</sub> |
| **Radial blast** | The enemy shoots projectiles spread in the shape of a circle at once. Changing angles between blasts can provide an interesting challenge *(used in danmakus/bullet hell games)* <br><br> ![Radial blast animation]({{ "/assets/blog_assets/enemy-design-shmups/shooting_radialblast.gif" | relative_url }}) <br> <sub>*An enemy shooting 10 projectiles in a circle*</sub> |
| **Charging <sub>(Special)</sub>** | The enemy takes a moment to charge before blasting multiple shots, one after another. The projectile style can be any of the attributes discussed above. |
| **Bomb <br><sub>(Special)</sub>** | The enemy triggers the shots like a bomb when killed, usually using a radial blast. |
{:.table}

## Departure attributes

| Name | Description |
| :-------------: | ------------- |
| **None** | The enemy continues with the *action* phase, usually found in *movement*-focused enemies. |
| **Movement** | The enemy uses one of the *movement* attributes as a way to leave the scene, usually used after a *shooting* attribute/phase that takes a longer time. |
| **Disappearing** | The enemy has another teleportation animation to leave the scene, which can be used as a way to reward the player for quickly defeating the enemy before disappearing. |
{:.table}

# References
I was heavily inspired by Garret Bright’s [Build a Bad Guy Workshop article](https://www.gamedeveloper.com/design/build-a-bad-guy-workshop---designing-enemies-for-retro-games) and how he structured the article, definitely worth a read.
I played:
- [Twin Strike](https://www.lexaloffle.com/bbs/?tid=43453) *(pico8 game)* by Mikesta
- [Warwind](https://louiechapm.itch.io/warwind) *(pico8 game, jam entry)* by LouieChapm
- [ZeroRanger](https://se-made.com/zeroranger.html) *(Demo)* by System Erasure
- Lords of Thunder *(Sega CD)* by Red Entertainment/Hudson Soft
- Gunbird 1 and 2 *(Arcade, Sega Dreamcast)* by Psikyo

I watched the playthroughs of:
- [Star Soldier R](https://www.youtube.com/watch?v=yZRBxNcLQuk) *(Wiiware)* by Hudson Soft
- [Darius Twin](https://youtu.be/9OjfHqxdNjA) *(SNES)* by Taito
