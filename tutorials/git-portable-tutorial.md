# Git Portable Tutorial

This tutorial will get you up and running with Git Portable. You'll learn how to install and configure Git Portable as well as how to use it with the Tube Notcher repository.

## Setup

We'll be using GitPortable on Windows. Download the installer from the project's [Github page](https://github.com/bungeshea/GitPortable). 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor01.png)

Run the `.paf.exe` file (the installer) and choose a place on your flash drive to install. The installer will create the GitPortable folder, so don't create it first.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor02.png)

Now run `GitPortable.exe` to get started.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor03.png)

You'll see a command line prompt.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor04.png)

Type `git gui` and hit `ENTER` to start the GUI. It may complain about a missing `/tmp` folder. This is okay for now.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor05.png)

The GUI will start with this window, since we're starting fresh. We already have a repository on Bitbucket, so choose `Clone Existing Repository`. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor07.png)

It'll ask you for a `Source Location`. You can find this in the top right corner of the Bitbucket repository [Overview page](https://bitbucket.org/songjx/tube-notcher). 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor08.png)

For `Target Directory`, choose a new location on your flash drive. Hit `Clone`.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor09.png)

It'll ask for your password.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor10.png)

It might ask again.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor12.png)

And again.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor13.png)

Almost there.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor14.png)

Once the cloning is complete, we see the main Git Gui window. This is where we'll be doing all of our git work. Notice the `Current Branch: master` in the top status bar. This means all the work we do now will be on the local `master` branch. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor15.png)

## First Commit

Our working directory `G:\tube-notcher\demo` now contains all of our tube notcher project files, so let's make a change locally. I've added another test update to README.md. This is what shows up as the project description on the Bitbucket repo overview page.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor16.png)

I've now saved that file (in Notepad++) and returned to the Git Gui window. Hit `Rescan` to pick up changes in the working directory. `README.md` appears listed under `Unstaged Changes`. The changes made to `README.md` appear in the 	`File: README.md` area. The changes are shown in diff format. This works okay for text files, but not so well for Solidworks files. This is fine.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor17.png)

Before we commit, we need to stage the changes we made. Hit `Stage Changed` to stage all changed files. For us, this is only `README.md`. Notice that the bottom status bar now reads `Ready to commit`, now that our staging area isn't empty.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor18.png)

But wait! Our commit isn't useful unless we include an informative commit message. The first line should be a very short summary of changes made - it should only be a few words. After a blank line, the rest of the message should contain more detailed information. Anyone, especially your team members, should be able to read your commit message and understand what you changed and why.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor19.png)

Now we hit `commit` and...the program complains that we haven't set up an identity yet. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor20.png)

Open a new instance of `GitPortable.exe` and type in the commands. Pay attention to the dashes and spaces. Use the same email you used to sign up for Bitbucket.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor21.png)

Now go back to Git Gui and hit `commit`. You'll get a success message in one of the status bars: 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor22.png)

## First Push

Great! Now that we've made a commit we like, and we're done for now, we can push those changes up to the remote repository. Hit `Push` in Git Gui. We made changes on our local `master ` branch, so we'll push that one. We only have one remote, called `origin`, so we'll push there. Our changes will be reflected in the `origin/master` branch. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor23.png)

Hit `Push`  in the Push window, and it'll ask for your password again. If you find this annoying, feel free to [set up SSH for Git](https://confluence.atlassian.com/display/BITBUCKET/Set+up+SSH+for+Git). You won't have to type your password any more.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor24.png)

Success. The `master -> master` indicates that we pushed our local `master` branch to the remote `master`. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor25.png)

If we go to the Bitbucket overview page, we see that the readme now reflects our update, `test update #2`. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor26.png)

We can see more information about our commit (and all past commits) at the `Commits` page. Note the short commit messages. Also note the `Mark-II` tag on commit `90cd571`. Also note the several new branches that have been created. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor27.png)

## Branches

You won't always be working on the `master` branch. If you want to work on something new on the side for a while, make a new branch and make your commits there until you're ready to merge your changes back into `master`, which will serve as our "official" main branch. 

### Working on a Tracking Branch

I've made a branch called `new-vise` where I've started CADing up the new milling vise. Let's do some work there. 

Currently, the `new-vise` branch exists on my (Jackie's) local working directory, because I created it, and in the remote repository, because I've pushed my work. Our fresh repository doesn't have it yet, so we'll make a new local branch to track it. This branch will track the `origin/new-vise` branch so that we can push to it and fetch updates from it. In Git Gui, go to `Branch > Create...` to open the `Create Branch` dialogue. 

Select `Match Tracking Branch Name`, unless you want your local branch name not to match the remote one. I wouldn't recommend this.

Select the `Tracking Branch` radio button and `origin/new-vise`. `Fetch Tracking Branch` means your new local branch will be up to date with the remote one. `Checkout after Creation` means you'll switch to that branch now, so you can work on it right away. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor28.png)

Hit `Create`. `Current Branch: new-vise` lets you know that you're now on the `new-vise` branch. Now you can do work on `new-vise`.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor30.png)

### Creating a New Branch

We don't have anything to add to `new-vise` right now, but we do have some other new stuff we wanted to do. Let's make a new branch from scratch. We're currently on `new-vise`, but the work we're doing has nothing to do with the new vise, so we'll branch off of `master` instead. To do that, we need to checkout `master` again. Go to `Branch > Checkout...` 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor32.png)

Note that we have two local branches now, `master` and `new-vise`. Hovering on a branch name shows some information about the last commit. Select `master` and hit `Checkout`.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor33.png)

Checking out a different branch means your working directory has to be changed to match the current state of that branch. This might take a minute. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor34.png)

Now that we're on `master`, we can make a new branch off `master`. We'll name our new branch `demo-branch`. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor35.png)

We'll update the readme again, this time on our new branch. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor36.png)

After saving and `Rescan`ing, we see our unstaged changes in `README.md`. But wait, what are those `.tmp` files?

#### Side note: `.gitignore`

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor36.png)

It doesn't really matter. Those are temporary files made by some other program, so we don't need them cluttering our project. I'll tell git to ignore `.tmp` files by editing the `.gitignore` file. You don't necessarily need to know this, but if you ever want to add to it, the `.gitignore` file is located in the main project folder. It's a plain text file, so you can use Notepad, or edit it directly from Bitbucket. I'll use Vim. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor39.png)

`*.tmp` matches files with the `.tmp` extension. Note all the temporary Solidworks file types listed.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor40.png)

### Creating a New Branch, Continued

Now we can `Rescan` and those `.tmp` files will be gone. We can write our commit message, stage changes, and commit.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor43.png)

The remote doesn't have `demo-branch` yet, so let's push.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor44.png)

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor46.png)

Now on the Bitbucket Commits page, we can see the commit on our new branch, nicely labeled. Note that each branch so far has its own starting point on `master`, so our tree isn't too complex yet.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor47.png)

### Merging

Now that we've done some work on `demo-branch`, we might decide that we're happy with our demo and we want to integrate our `demo-branch` changes back into `master`. First, we need to switch back to `master` by checking it out: 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor48.png)

Then, open the `Local Merge` dialogue, select `demo-branch` to be merged in, and hit `Merge`: 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor49.png)

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor51.png)

Now that we've merged `demo-branch` into `master`, we don't need `demo-branch` any more. Let's delete it. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor52.png)

We should also push the merge.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor53.png)

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor54.png)

Again, our `demo-branch` change shows up in the Bitbucket readme.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor56.png)

Now, on Bitbucket, `demo-branch` will disappear from the `Active` heading and appear under `Merged`, even though we deleted it locally. Let's delete it in Bitbucket too.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor62.png)

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor63.png)

## Remote Changes 

Besides your teammate pushing from their computer, remote changes can also be made right in the Bitbucket site, at least for text files.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor56.png)

We'll made a remote change to the readme. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor58.png)

Here's the default commit message. We'll keep it.

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor59.png)

## Fetching and Merging

Since someone has made a change to `origin/master`, we should probably get that change before we try to do any further work on `master`; otherwise, some messiness could happen. This is done by fetching: 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor60.png)

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor61.png)

Fetching downloads the remote changes. This means they're available to you, but your local branches are unaffected until you merge the updated remote branch into your local. So, we'll merge `origin/master` into `master`:

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor65.png)

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor66.png)

If we open the readme again from our working directory, we'll see that we now have the remote change. 

![git-tutor##](https://s3.amazonaws.com/tube-notcher/tutorial/git-tutor67.png)