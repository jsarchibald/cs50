# Week 8 Exercises

Exercises designed by Josh Archibald for the section of [week 8 of CS50](https://cs50.harvard.edu/college/2020/fall/weeks/8).

Exercises can be completed using the CS50 IDE.


## Magic 8 Ball

Life is filled with uncertainty, which is why we take probability courses like STAT 110. Another way to cope with uncertainty, however, is to trust in a magic ball filled with some blue goo substance that will indicate...something. The signal is pretty noisy; it can be hard to figure out what the ball means. But it's magical!

Today, we shall make a Magic 8 Ball.


### 0. Open the CS50 IDE.

Navigate in the terminal to the directory where you want to do your work using `cd` and `mkdir` as needed.

### 1. Create `index.html`.

Recall from lecture that typically `index.html` is used to denote the index page, or the root page of a directory. In the olden days of the web this index page would be useful for navigating folders of HTML files.

To start our HTML page it's useful to copy the following:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Magic 8 ball</title>
    </head>
    <body>

    </body>
</html>
```

#### What this is

Let's unpack this a little bit. The first line specifies that the file we're writing is indeed an HTML5 document. After that, we open up our HTML file with the `<html>` tag, wherein we also specify the page's language as being `en` -- generalized English. (For more specificity, we could've said `en-us`, for example.)

Inside the `<html>` tag there are only two structures: `<head>`, which specifies the metadata for the document, and `<body>`, which specifies the content that should be shown to the user. Everything in our HTML file should go inside either `<head>` or `<body>`.

Inside our `<head>` we first specify the `charset`, or character set, that our page uses -- `utf-8` is standard nowadays. An alternative charset is `ascii`, which you dealt with a lot in C! We also specify the `<title>` of the page which appears as the name of the tab in your browser (it's also used by Google when indexing webpages).

Inside our `<body>` tag we have...nothing, because we're going to add stuff there momentarily!


### 2. Create `main.css`.

In this problem, and in most cases of web design, we will want to be able to style our HTML. Recall that we store styles in a `Cascading Style Sheets`, or `.css`, file. For now, let's just create a blank file in the same directory as `index.html` called `main.css`.

How can we then include our stylesheet in `index.html`? By adding this line to the inside of our `<head>`:

```html
<link href="main.css" rel="stylesheet">
```

#### What this is

This tells the browser to load up the file at `main.css`, which is of type `stylesheet`.

Recall that there are other ways to style your HTML elements -- you could create a `<style>` element within your head and just write the styles there, for example. Or you could add the attribute `style="..."` to most HTML elements. Those are both possible! But not good practice. You should really only do that when you're making a really quick prototype. For any large project, such ad-hoc styling gets disorganized very quickly, and if you want to reuse styles between HTML files, you'll end up copy-pasting, which is plainly disgusting. So use separate `.css` files and `<link>` whenever possible, as a general rule.


### 3. Create `main.js`.

To execute logic on our webpage, we'll need JavaScript. Create a blank file called `main.js` in the same directory as `index.html`. Then, add this line to the end of the inside of the `<body>` tag in `index.html`:

```html
<script src="main.js"></script>
```

#### What this is

Why at the end of the `<body>` tag? You can put a `<script>` tag in the `<head>` or anywhere in the `<body>`, but I learned to put it at the end of `<body>` so as to slightly improve page display speed (see [here](https://www.w3schools.com/js/js_whereto.asp)). Admittedly, I learned HTML/CSS/JS a *very* long time ago, so there are modern alternatives that may allow you to avoid such display slowdowns but still put the `<script>` tag in the head, specifically by writing `<script async>` which [basically](https://www.w3schools.com/tags/att_script_async.asp) tells the browser to start loading the JS but don't wait for it to be done before you render the rest of the page. For simplicity, though, I still put my `<script>`s at the bottom of the `<body>` tag.

Why a separate file for the JavaScript? Same reasons as CSS re: reusability, separation of types of code, general organization, and browser optimizations related to caching mechanisms.


### 4. Create the HTML structure of the page.

Let's now work inside the `<body>` of `index.html`. Recall that the [`<div>`](https://www.w3schools.com/tags/tag_div.asp) tag in HTML is somewhat of a panacea for all sorts of structuring -- it serves nicely as a container for any element(s) you want, and can be styled with CSS pretty easily.

So, here's what I'm thinking, structure-wise:

- a `<div>` for the Magic 8 ball overall. Inside that:
  - a `<div>` for the blue thing in the middle. Inside that:
    - a `<div>` for the text/emoji of the prediction itself.

It would also be useful to use some classes and IDs to help with the CSS and JavaScript manipulation of this project. Maybe `.ball`, `.blue-center`, `#prediction`?

- *Wait, what? Dots and hashtags, I'm lost.* The dots (e.g., `.ball`) indicate classes -- there can be multiple elements in an HTML document with the same class. The hashtags (e.g., `#prediction`) indicate IDs -- there can only be one element with a particular ID in an HTML document. IDs are unique.

Here's a question you might be asking: why use classes vs. IDs in this case? Like, if we wanted multiple Magic 8 Balls on this page, we'd want `prediction` to be a class, *not* an ID (because there would be multiple in the document). If there's only one, we'd maybe want `ball` and `blue-center` to be IDs. The reason in this case is an arbitrary design decision on my part: maybe I want to reuse the styling from `.ball` and `.blue-center`, so those should be classes. For `#prediction`, I'm just using it to make my JavaScript a little simpler, so a unique ID is just fine. (I also wanted to show how to access by both class and ID in JavaScript, so there's a pedagogical reason at hand as well.)


**Take a second to think about how you'd write this code.**

Ok, now that you've thought about it, here's what I'd write inside the `<body>` tag, before the `<script>` tag:

```html
        <div class="ball">
            <div class="blue-center">
                <div id="prediction"></div>
            </div>
        </div>
```

I've now replicated the structure I mentioned above (but in code) and have the appropriate classes and IDs set where needed. Now, it's time to style it with CSS!


### 5. Style the Magic 8 Ball with CSS.

For the purposes of this problem, we're going to assume we don't care how this page looks on a smartphone. We're going to assume setting widths and heights by pixel were still acceptable practice in 2020, even though it's not. We're going to assume our users are using browsers that are okay with CSS calculations and transforms. We're going to assume our users have access to the Arial or Helvetica font. We're making a lot of assumptions here, because that's what we have to do to keep the problem relatively simple.

For the ball itself, we're going to set the `position` to be `absolute`, so it stays in place on the page. The background should be some dark gray, maybe `#111111` (or `#111` for short). And let's say we want it to have a radius of 300 pixels -- that means we should set the `width` and `height` to be `600px` each and have a `border-radius` of `300px` (300 pixel rounding in each corner) to make a circle like that. In summary:

```css
.ball {
    position: absolute;
    background: #111;
    width: 600px;
    height: 600px;
    border-radius: 300px;
}
```

For the blue center, let's simplify and say it'll be 150 by 150 pixels. To center it within the ball vertically, we'll set its margin from the top `margin-top` to be 50% of the ball's height, minus half the blue thing's height as an adjustment -- in CSS, that's `calc(50% - 75px)`. (If we did a margin of just 50% of the ball's height, then the blue thing would have its top edge at that point and wouldn't be quite centered.) We do the same for `margin-left` to make the blue thing horizontally centered. We want the blue thing to have a blue background, obviously, so we pick out a blue from [a site like this](https://www.webfx.com/web-design/color-picker) and plug in the hexadecimal color representation into our `background` property.

```css
.blue-center {
    height: 150px;
    width: 150px;
    margin-top: calc(50% - 75px);
    margin-left: calc(50% - 75px);
    background: #0c0096;
}
```

Now we work on the `#prediction` div. We want the text to appear in `Arial` or `Helvetica` font, so we add the `font-family` property you see below. (Note that these fonts are searched in order -- the browser will check for `Arial` first and use it if the user has that font; if not, it'll check for `Helvetica`, etc.) We also want it to be white, so we set `color` to be `#ffffff`, or `#fff` for short.

```css
#prediction {
    font-family: Arial, Helvetica, sans-serif;
    color: #fff;
}
```

Now we just need to make the prediction centered horizontally and vertically within the blue thing. I looked it up on Google and found [this page](https://www.w3.org/Style/Examples/007/center.en.html#vertical3) which describes very nicely how to do what I want. For the child element, `#prediction`, I need to make these changes for a vertical alignment:

```css
#prediction {
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    font-family: Arial, Helvetica, sans-serif;
    color: #fff;
}
```

To make a horizontal alignment, I just do the same thing with `left` and change that `0` in `translate` to similarly be a `-50%`:

```css
#prediction {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Arial, Helvetica, sans-serif;
    color: #fff;
}
```

Finally, for the parent element, `.blue-center`, I need to add this:

```css
    position: relative;
```

So `.blue-center` now looks like:

```css
.blue-center {
    position: relative;
    height: 150px;
    width: 150px;
    margin-top: calc(50% - 75px);
    margin-left: calc(50% - 75px);
    background: #0c0096;
}
```

As a finishing touch, I want the ball to make my mouse look like I'm about to click on it, so I add `cursor: pointer;` to `.ball`. I also want it to fade from dark gray to a lighter gray when I hover, so I add `transition: all .5s;` to `.ball` and then add a new styling for `.ball:hover`. In all, our stylesheet should look like this now:

```css
.ball {
    position: absolute;
    background: #111;
    width: 600px;
    height: 600px;
    border-radius: 300px;
    cursor: pointer;
    transition: all .5s;
}

.ball:hover {
    background: #222;
}

.blue-center {
    position: relative;
    height: 150px;
    width: 150px;
    margin-top: calc(50% - 75px);
    margin-left: calc(50% - 75px);
    background: #0c0096;
}

#prediction {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Arial, Helvetica, sans-serif;
    color: #fff;
}
```

### 6. Adding functionality with JavaScript.

Right now, we have a Magic 8 Ball with no words and no meaningful user interaction. JavaScript will help us close that gap.

#### a. Add an array with the possible phrases we may come across.

I'm trusting that [this site](http://www.otcpas.com/advisor-blog/magic-8-ball-messages) gives us a correct listing. Recall that to create an empty JavaScript array, we can just write `let array_name = []`. For simplicity (there are 20 phrases), you can just copy this code to create the array into your own `main.js`:

```js
let phrases = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
];
```

#### b. Store the prediction div and the ball div in JS variables.

The DOM and JavaScript allow us to save individual HTML element objects in variables. (Those objects are retrieved using [`document.getElementById`](https://www.w3schools.com/jsref/met_document_getelementbyid.asp), [`document.getElementsByClassName`](https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp), or other document methods.)

Let's store the `.ball` element and `#prediction` element into variables.

This should look something like:

```js
// use the [0] because this method returns an array (since multiple elements can share a class):
let ball = document.getElementsByClassName("ball")[0];
let prediction_text = document.getElementById("prediction");
```

#### c. Write a function to choose and display a prediction.

Let's write a `function predict()` that will randomly choose a phrase from our array of phrases, and change the `innerText` of `div#prediction` to be that phrase. The W3Schools page on [`Math.random`](https://www.w3schools.com/js/js_random.asp) may be useful. And recall that you can get the size of an array with `array_name.length`.

Ultimately your function should look something like this:

```js
function predict() {
    // Get a random float 0-1, multiply by the number of phrases, and always round down
    let index = Math.floor(Math.random() * phrases.length);

    // Get that phrase
    let phrase = phrases[index];

    // Set the div#prediction to have that phrase as its text
    prediction_text.innerText = phrase;
}
```

#### d. Set event listeners.

Great, now we just need to set some event listeners -- when the page loads and when the ball is clicked, a prediction should be made. You'll want to use [`document.addEventListener`](https://www.w3schools.com/jsref/met_document_addeventlistener.asp) for this.

Probably you'll end up with something like this:

```js
ball.addEventListener("click", predict); // when the ball is clicked, predict
document.addEventListener("DOMContentLoaded", predict); // when the page is done loading, predict
```

And now we have a Magic 8 Ball!


## Profile page

Remember [that exercise](week6.md#hello-section) where you wrote some code to upload some information to a site? Today we expand upon [J50](https://j50.herokuapp.com/html) by uploading HTML profile pages to it.


### The task

Create an HTML page about yourself (or a character you really like). You can include images, text, links, anything really -- keep it appropriate for Harvard and please don't add dangerous JavaScript, but other than that, the idea here is to get practice with HTML and CSS so you feel ready to go on to the pset.

Only real limitation is that you should keep your code contained within a single HTML file, which means you'll want to write all your CSS within a `<style>` element inside the `<head>` of your document.

### Uploading your code

First, download the upload script using this command in your CS50 IDE terminal:

```
wget https://raw.githubusercontent.com/jsarchibald/cs50/2020/fall/exercises/distro/j50.py
```

Then, just run the command like this:

```
python j50.py upload <path-to-html-file>
```

For example, if I downloaded the script to the same folder as my `index.html` file, I'd just run:

```
python j50.py upload index.html
```

As with the exercise from week 6, you're able to delete any uploads you make as well. Just run:

```
python j50.py delete <number_of_submission>
```

Where `<number_of_submission>` comes from the ID number listed on the site.
