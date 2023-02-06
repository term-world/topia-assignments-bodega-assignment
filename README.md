
| Date              |          |
|:------------------|:---------|
| `TODO` | Assigned |
| `TODO`   | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# ZERO-FRILLS ZONING PROPOSAL ZAPS ZOMBIFIED ECONOMY

*Reported by `The Reporter, TNN` from `TODO` on `TODO`*

A bold new proposal from `The Mayor` promises to make money waves of magnificent magnitudes in the shallower parts of `term-world`'s economic landscape. `The Mayor` refers to his brainchild as "Prop Stop n' Shop", an apt name for a measure meant to meaningfully magnify the microeconomies of myriad `term-world` neighborhoods.

"Prop Stop n' Shop" sets aside nearly 10% of each residential area's acreage for purely profitable purposes. It's `The Mayor`'s hope that this endeavor will help jumpstart a jetlagged economy--putting a little more jingle-jangle in our citizen's jean pockets.

`The Mayor` is formally tasking the residents of each neighborhood with the creation of a neighborhood `bodega` that might showcase the unique cultures (and commercial capabilities) of each of `term-world`'s compact communities. We wager that within a week or two we should witness the wonders of their work--our wallets certainly can't wait!

## Overview

In this set of activities we cover:

* Markdown
* working collaboratively using Github
  * branching
  * merging
  * issuing "Pull Requests"

You'll complete three main tasks:

1. Developing a department of the bodega that contains `10` items in list file (more below)
2. Collaborating a website for your bodege that demonstrates all it has to offer
3. Completing a collaborative reflection authored by all of the members of your neighborhood

## Supporting media

We haven't yet talked directly about Markdown, though we've used it a couple of times. The following video introduces you to the ideas behind Markdown and fellow citizen, Professor Bonham-Carter.

[![TItle screen featuring a picture of Oliver Bonham-Carter](https://img.youtube.com/vi/cdJEUAy5IyA/maxresdefault.jpg)](https://www.youtube.com/watch?v=cdJEUAy5IyA&list=PLsYZRXov75ZHSwWiCk0-jad1RcTuu_-zmD&index=5)

### Previous Learning Objectives

If you wish to review previous learning objectives from our assignments, you can visit the [`Syllabus`](https://chompe.rs/100-syllabus) for helpful information. However, it's also important to make an effort to retain what we have covered thus far as we progress through the course sections of the Readme might be taken out.

## Accessing bodega Content

In order to complete the workload for the `bodega` you'll first need to `clone` the `bodega` repository into your `workshop`.

When you `clone` a repository you're duplicating its contents and adding them to your local workspace. Since you'll be working collaboratively with your neighbors, you'll each need your own copy of the `bodega` to work with.

Steps to `clone` collaborative assignments are the same as individual work, and are available in our course [CONTRIBUTING.md file](../../../course-materials/blob/main/CONTRIBUTING.md).

## Completing `bodega` content

### "List" files

**You must create a branch named for your department in which to conduct your work.**

To stock your bodega, each group member is in charge of a single "department" (i.e. category) of items to stock. To stock a department, you must first have a list of items to stock! Here, each person must create a _single_ `*.list` file containing a new item on each line.

To do this:

* find your `bodega`'s `stockroom` folder in your file explorer
* right click the folder and select `New File`
* create a file whose name is `DEPARTMENT.list`
  * e.g. `savorysnacks.list`
* add _no fewer_ than `10` items to your list
* follow all python variable naming rules
  * no dashes
  * no symbols beyond `_`
  * numbers cannot start the object name (unless spelled out)

Once you've created your list, run the `Stocker.py` to stock the department. This should create a folder and fill it with goods.

Once finished, running `Counter.py` should inventory your store!

### Bodega site

**You must create a branch named `YOUR_DEPARTMENT-SITE` to conduct your work.**

All of the files for your bodega site are located in the `site` folder. Every neighborhood member should make a "post" in their own file in the `_posts` folder. This file's name _must_ follow the naming convention:

```
YEAR-MONTH-DAY-DEPARTMENT_NAME.md
```

You will need to copy the example file to make your department file. Be sure to rename it using the convention above. 

* Provide a short description of yoru department _and_
* using a Markdown list, list what your department contains

Each `.md` file contains information about the department page. For example:

```yaml
---
layout: post
title:  "example"
author: cliv3
categories: [ bodega, departments ]
image: assets/images/bodega_template.png
---
```

This information helps create, categorize, and design the post. Change it to reflect your contribution to the `bodega` site (via department).

Anything appearing below this header uses Markdown. See earlier in this section for information on what to write here.

#### About page

**Create one branch called `about-page` to capture your work on this section of the assignment; all members should contribute to the same branch.**

Your group should also edit the about page to give an overview of your bodega and neighborhood. This file is in the `pages` folder and follows a similar composition as the posts discussed above.

Do not rename or copy this file -- edit the content directly in it.

### Collaborative reflection

**Create one branch called `reflection` to capture your work on this section of the assignment; all members should contribute to the same branch.**

All of the above tasks completed, finish the collaborative reflection located in the `breakroom`.

## Making an improvement proposal

This assignment begins your opportunity to propose and improve the world of `term-world` at-large. For this assignment, proposals may include making graphics to improve the `bodega` site experience, creating new items or actions in the `traffic-circle` itself or another assignment-related improvement not contemplated in the prior narrow categories.

To make an improvement proposal, you must _create an issue_ on this repository. Do so by:

* clicking the `Issues` tab at the top of the page.
* clicking the green `New Issue` button
* selecting the `Improvement Proposal` template 

**Make sure to link your issue with the pull request you used to make your actually improvement.**

### Improvement Suggestions

Here are some proposal suggestions you can consider implementing for this assignment. Please choose `one` (and only one) to file using the [`term-world Improvement Proposal system`](../../issues/new/choose).

|Improvement Suggestions |Description        |
|:-----------------------|:----------------------------------------------------|
|Design                  |Add an illustrative header to your `bodega` department |      
|Design                  |Create a logo for the `bodega` front page            |
|Design                  |Replace the `TNN` ad with a neighborhood/`bodega`-specific ad |
|Markdown                |Create a compelling ad copy for your `bodega`'s "About" page |
|Markdown                |Create compelling ad copy for your `bodega` department |
|Data                    |Add `bodega` departments to the page menu using `_data/menus.yml` |
|Programming             |Greet visitors on entry to the `bodega` using the `WelcomeSign.py` file |
|Programming             |Display an ASCII-art logo for your bodega in the `WelcomeSign.py` file |
|Programming             |Figure out how to run the `Counter.py` file on visitor entry (using the `.events` file) |

**If you are not following an improvement suggestion, you will need to have your improvement approved in writing through the [`Improvement Proposal process`](../../issues/new/choose).**

## Branching bodega content

Even when working collaboratively with others on a single project, you'll still need to `add`, `commit`, and `push` your work. However, there's a few additional steps that keep your group's workflow organized.

Each repository has a `main` branch that represents exactly that, the "main" version of the repository. This is the version that is cloned whenever somebody runs a `git clone` command with that repository as its target, and the contents of `main` are what is pulled when somebody updates their local workspace's version of the repository with `git pull`.

However, each repository can also have multiple alternative versions of itself that simultaneously exist. These versions are referred to as "branches".

![CMPSC 100 - GitHub flow](https://user-images.githubusercontent.com/1552764/216829828-93512274-3a44-47ef-bcb8-a44f17d9be7b.png)

Branches are *very* useful when collaborating with other people on the same project--they can keep multiple portions of a developing project organized, and keep partially implemented (or incomplete) code from interfering with other developers.

You'll see firsthand just how useful this is as we work collaboratively over the next couple weeks, but for now, trust us: going through the extra couple of steps to branch your work when starting a new project (*especially* when working with other people) is a proactive step to avoiding many a headache later in the development process.

### Creating a `branch`

So, how do we do all this good stuff?

After having `clone`d the repository you wish to `branch` in:

* locate the repository in your `Source Control` sidebar
* click the `...` menu to expand source control options
* locate and click the `Branch >` menu
* find and click `Create branch`

![image](https://user-images.githubusercontent.com/1552764/216830482-c5ccbfd3-5b7f-40a3-85f4-d2385c37fcce.png)

* name your branch

![image](https://user-images.githubusercontent.com/1552764/216830721-8f0d3458-4ecd-443a-929e-9c9c0c3714e5.png)

Notice that the branch on the Status bar has changed from `main` to the name of the branch you've created. You're now on that branch!

![image](https://user-images.githubusercontent.com/1552764/216830788-04697ad0-870f-42a3-bbd4-fee20c0c82f4.png)

### Switching `branch`es

This can happen one of two ways:

* click the name of the `branch` on the Status bar at the bottom of the screen and choose a new branch
* click the name of the `branch` you're on in the `Source Control` window next to the repository name you'd like to switch in

### Pushing to a `branch`

As written above, `clone` operations for collaborative assignments stay the same. However, contributing your work is a bit different. Here, we're going to use `branch`es to submit changes for consideration. The `Pull Request` process, detailed next, governs whether or not those changes make it in to the final work.

![image](https://user-images.githubusercontent.com/1552764/216830911-c3850cc5-96c0-4b75-bbea-c9e9fc1bf4e0.png)

The first time you put your branch on GitHub, you'll be asked to `Publish` it. This is just like synchronizing your changes. Once you're finished doing so, you should be able to see your branch on GitHub.

### Getting others' changes to a `branch` 

If this is truly a collaborative effort, we _should_ be able to coordinate their changes, too. (And, we can.)

#### For a branch you already have

To retrieve changes to a branch that already exists _and is already published to Github_:

![image](https://user-images.githubusercontent.com/1552764/216832015-3cea16e9-44b6-4ebe-bba7-cc65b791f5dd.png)

* make sure you're on the branch you wish to synchronize
  * check your Status bar to see if the `branch` name matches the `branch` you wish to update
* click the `...` menu and locate the `Pull` option
* click `Pull`

#### For a branch you don't have

If a branch exists on GitHub, and it's not part of your local collection, we need to `fetch` information from GitHub first.

* locate the `...` menu in `Source Control`
* click the `Fetch` option to update _your_ copy of the repository

![image](https://user-images.githubusercontent.com/1552764/216832590-fbcb182b-e8cb-47be-8b28-303ed82a3512.png)

In the above figure:
* `branch`es _you have_ have the `Source Control` branching icon
* `branch`es still on the _remote_ feature an icon that looks like a cloud
* after `Fetch`ing, switch to the `branch` you'd like to update
* follow the above steps to `Pull`

### A "Pull Request"

Once you've completed this step, you'll now need to create a **pull request** on GitHub. This is a formal request to other collaborators on your project to review the code you've submitted--an important step when working together on the same project.

In a web browser, navigate to the repository page on GitHub (for the repository that you've just submitted new changes for). Towards the upper-left corner you'll see a dropdown that will have `main` selected as default (`main` being one of the branches for your repository, this is the "production-ready" branch). Select your branch from the dropdown, and you may see a yellow box prompting you to create a pull request; click that if you see it, or navigate to `Pull Requests` at the top and subsequently click the green `New pull request` button.

![CMPSC 100 - PR Diagram](https://user-images.githubusercontent.com/1552764/216871681-fa99d94e-5d8a-4878-8f0e-d919dd199031.png)

Now, in the top left corner select the branch you wish to add your updated changes to, or the "base" branch--generally speaking this will likely be `main`, the aforementioned "production-ready" branch. In the bar on the righthand side, add Reviewers to the pull request (this should be all of your neighborhood collaborators). Finally, click `Create pull request`.

![CMPSC 100 - PR Review](https://user-images.githubusercontent.com/1552764/216872857-9f07f4c8-cab6-4e0e-b0ee-b327ee6f8e04.png)

You'll also be responsible for responding to and reviewing pull requests created by other collaborators on your team. Comment on each other's work about changes you'd like to see made to code submitted, and be sure to keep all communication both specific and professional.

### Merging bodega content

Regardless of the method that you use to merge your changes, you should obey the golden rule of collaboration:

> discuss all changes with your fellow citizens to understand what content you _should_ include

As with all collaboration, we should default to behaviors which promote _collaboration_.

#### On `term-world`

At some point, you may attempt to synchronize your changes only to see something like the following message:

![image](https://user-images.githubusercontent.com/1552764/216834131-2e5d095b-32f5-4217-b9be-491733dafe25.png)

This indicates that we need to manage a _conflict_. Here, we have the ability to click several options to choose _which_ changes we accept.

#### On GitHub

After all collaborators have had a chance to weigh in on a new pull request, if the work is up to snuff and ready to join the "production-ready" `main` branch, then your designated neighborhood team lead will have to merge that work into the `main` branch.

If you *are* said team lead, you'll need to navigate to the pull request on GitHub. If there are no "conflicts" (i.e., differences that can't be automatically handled by GitHub) between the pull request's branch and the `main` branch, simply click the `Commit merge` button and the merge is complete!

In some cases however, you'll have to specify what parts of a pull request make it into the `main` branch. If that's the case, you'll instead see a `Resolve conflicts` button. Click that and you'll be presented with a proposed merged copy of the code, with some extra lines added in. Something akin to:

```
 <<<<<<< HEAD
To reconcile
=======
At some point, you may attempt to synchronize your changes only to see something like the following message:

![image](https://user-images.githubusercontent.com/1552764/216833280-50cbd619-6abd-4074-a003-3dd366be0efa.png)

This indicates that we need to manage a _conflict_.
 >>>>>>> 9eb36e10772091394f7b61bfb8eeef32971b8b1d
```

To resolve said conflicts, you'll need to delete the portion of code you don't want to appear in the final product, as well as any `<<<<<<`, `=======`, or `>>>>>>` lines. The `HEAD` designation represents what you _currently have_. The long-numbered entry below the `========` represents the _incoming_ change being proposed.

Once complete, click `Mark as resolved` followed by `Commit merge`, and the changes on the branch will be joined with the `main` branch! This will update your local workspace with the content stored in the `main` branch.

## `term-world` Server Backup Policy

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e., weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.


Remember: to err is human; to back up your work is *divine*.
