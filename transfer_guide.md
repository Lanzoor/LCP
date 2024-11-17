# How to transfer savedata between multiple versions

You probably know that LCP does not allow you to use the same savedata file when the script and savedata file isn't in the same version.
But how can I prevent data loss, when this outdated release has some fatal bugs?
Well, this guide is for you!

## Option 1: Edit savedata directly

You're most likely going to [download a fresh new savefile](https://github.com/Lanzoor/LCP/blob/main/`savedata.json`). However, if you desire to use a specific version of a savefile,
tweak around with the downloadable zip files from the [releases](https://github.com/Lanzoor/LCP/releases) list.

Open the `savedata.json` file that you just downloaded, and open it. **You should still preserve your previous savedata in case you forget your stats.**
Now, you can start editing the savedata directly. If you are not familiar with JSON files, check out [this document](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON). You can simply transfer the old values to this file.

**But- not sure what option this is?**

Seriously, the savefile format might've changed during a recent release.
Don't worry though- the release notes should record all changes that were made!
To clarify, here are some option names that are different between the script file and the JSON file;

`??????` (`Ending`) shop upgrade (boolean) is `end` in the `savedata.json` file.

To make things more simple, the `script.py` file automatically changes values for you!
For example, you only need to change the shop upgrades and the script will automatically assign the correct value to the multiplier.
**This means that you shouldn't directly edit the multiplier, because if multiplier count and the shop upgrades aren't corresponding, the script will always, refer to the shop upgrades.**

This also applies to the `shopUpgradesPurchased` upgrade. (You don't need to change the `shopUpgradesPurchased` upgrade when transferring)

**So the only options you need to tinker with is the shop upgrades, points, and settings. Nothing else.**

After that, you can enjoy!

> NOTE: Manually editing the version tag is NOT recommended, you have been warned.

## Option 2: Ask me

You can contact Lanzoor (lanzoor in Discord), and I can manually do the steps above for you if you're too lazy! I will try to respond ASAP.
