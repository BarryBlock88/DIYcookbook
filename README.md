# Milestone_Project_Three_
### Developer/Author - Barry Cullen
 ![Home page](static/img/wireframes_milestone_one/BarryBlock88.png)

## This project (Milestone Three) was completed as part of Code Institute's Full Stack Web Development course in 2020/21-

## Project Requirements:
1. Data handling: Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. 
2. Database structure: Designing a database structure well-suited for your website. Making sure to put some thought into the nesting relationships between records of different entities. 
3. User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality). 
4. Use of technologies: Use HTML and custom CSS Sfor the website's front-end
5. Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap to accomplish this). 
6. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users. 
7. Version control: Use Git & GitHub for version control. 
8. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README. 
9. Deployment: Deploy the final version of your code to a hosting platform such as Heroku. 
	Make sure to not include any passwords or secret keys in the project repository. 

## Project Outline:
#### A beer recipe website with a searchable database and the ability to add your own recipes– Brew Book!
#####Project Goals -
-Create a minimialist, clearly-designed website for a user to easily navigate . 

-Be consistent with the theme of the website throughout all pages of the site. 

-Integrate MongoDB + Flask +python into the website using a database, the database will hold data on beer recipes, categories for searching and sensitive user information. 
-Create functionality to allow users to edit specific parts of the site related to the database.

-Create a project which is inline with nessarcy project requirements as per Code Institude project guidelines as listed above in Project Requirements .

-The site will use a simple warm pleasant colour palatte, with other elements such as the Buttons and the heading in a contrasting but complemetary colour.


- The Website begins as a straightforward presentation of photos of glorious beers, asking one single question, “sign up”. To help keep the eye focused, the site only uses 4 colours and the simple primary company logo with one line of text. So the Home page acts as 'Call to Action page'. 

- Each page will feature the company logo and a nav bar to other pages.

Every page will contain a footer with four social link icons.

-There are 3-page links located on the Navbar for un-registered user
-There are 6-page links located on the Navbar for registered user

 -Home page that contains the company name, and sign up button  and a photo carousel
 -Login page for returning users and a link on this page to sign up page if you are currantly not a user.
-Sign up page  for new users to sign up for the advanced features of the site, these nav abr links will become visible once the user signs up.
-Brews page  includes photos of  all recipes and a search bar for searching the datatbase.(planning to use a a review system in future versions)
-Add Brew page consists of a form for adding new recipes to the database if your are a registered user already and will not be accessable to a new site vistor.
-Edit Brew page consists of a form for updateing your own recipes (not that of other users) to the database if your are a registered user already and will not be accessable to a new site vistor.
-Categories page consists of a list of categories and buttons for adding new categories and for editing or deleting current categories to the database if your are a registered user already and will not be accessable to a new site vistor.



## *UX*
#### Who is the target audience of this site?

The website is targeted at current home brewers and poeple new to home brewing and also the average beer-lovers looking to discover more about the beers they love.
I imagine modern users visiting the site through there phone and laptop primarily.



“As a [persona], I [want to], [so that].” 
### User Stories

 As a first time user of the Website, I want everything visible immediatly and easy to use.
 As a first time user of the Website, I want be promted to sign up easily if its my first time using the site, to have use of the full features of the site.
 As a registerd user of the Website,  I want to easily find a recipe for various beer recipes from beginner to avanced level of diffculty, so that i can more quickly find the right recipe. 
As a registerd user of the Website,  I want to be able to share some of my favourite beer recipes and also ones i have created my self with others users of the website. 
As a  registerd user of the site, I want to edit a beer recipes that I added to the site on a previous visits.
As a  registerd user of the site, I want to delete a beer recipes that I added to the site on a previous visits.
 As a registerd user of the Website, I want to search for the right category of beer for my next brewing project from the database of recipes. 
As a  registerd user of the site, I want to add my own unique categories of beer to the categories page. 
As a  registerd user of the site, I want to edit a categories of beer on the categories page.
As a  registerd user of the site, I want to delete categories of beer on the categories page.
As a  registerd user of the site, I want to be able to login easily with my personal password and username.
##Design process

#### Links to wireframes
#### Mobile


#### Desktop 


### Colour design
For the colour palette, from here https://coolors.co/ , I chose the colours to give it a warm welcoming feel. My home is the a new user will assosate the site with beer through its color pallate provoke a positive response from the user.
The other colours black and beige colours where used to create a clear contrast in the buttons and titles and flash messages to help readability and ease of engagment. 

#### Colour palette :

- #Darkgoldrod as the primary background colour to provide a warm colour and a nice contrast to help readability.
- #Black as a darker color to help clearly show for the other buttons in the game against the warm background, 
- #Beige for  as a ligher gray to clearly show when start taking orders button is hoovered, the majority of the text and the main game title.
- #Darkolivegreen for border color of the sign up/login button tiles.
- #Red is the colour used sparingly in the project for contrast in add category button text to improve readability.

### Typography

 The font were imported from Google Fonts.
https://fonts.google.com/specimen/Sunflower?query=flow
I used this font as it is simple pleasant and easy to read,
as i wanted to give the site a	easygoing appeal.

### Images
https://s3.amazonaws.com/images.ecwid.com/images/32880331/1605861747.jpg
https://www.globexs.com/wp-content/uploads/2020/06/breweries_antwerp.jpg
https://www.zettpoint.com/wp-content/uploads/2017/08/beertap.jpg
https://images.askmen.com/1080x540/2019/03/29-062407-10_amazing_ways_to_drink_beer.jpg



## Database Design and structure
Brew Book (brew_book_block) database consists 4 collections. 
Hosted in MongoDB. 
#### (brews.db) Structure
1. _id - ObjectId – randomly generated in mongoDB
2. brew_name : str
3. category_name : str
4. difficulty : str
5. quantity : str 
6. brew_time : str
7. ingredients : str
8. description : str 
9. brew_image : str 
10. created_by : str 
#### (categories.db) Structure
1. _id - ObjectId - (generated by mongoDB) 
2. category_name : “Porter”
3. category_name : “Lager”
4. category_name : “Saison”
#### (difficulties.db) Structure
1. _id - ObjectId - (generated by mongoDB) 
2. difficulty : “Novice Brewer”
3. difficulty : ”Seasoned Brewer”
4. difficulty : ”Weekend Warrior”
5. difficulty : ”Brew Master”
#### (users.db) Structure
1. _id - ObjectId - (generated by mongoDB) 
2. email : str
3. username : str 
4. password : str - (password hash generated via werkzeug.security) 

## *Features*


### Current Features

1. The game will prompt the player/user instructions via messages that will allow intutive game play.
2. The 'ON/OFF' button activates/deactivates the Game.
3. The 'NORMAL/HARD' button allows the player/user to select a greater in game difficulty.
4. Player/user can activate a popup window of the rules of the game by clicking the 'TUTORIAL' button. 
5. Game button tiles flash and play a sound when selected by the player/user.
6. Game button tiles flash and play a sound when activated as part of the computer sequence.
7. Game button tiles all animate, flash a border and play a sound when error is made or if they win the game
8. The level counter allows the player/user to follow there current level, with each success a sound is played and counter increases by one.
9.  Remember The Order! is responsive on various devices including smaller mobile devices.


### Additional features in future versions

1. Add search recipe feature to the navbar. 
2. Users to add comments to recipes. 
3. Create a profile page for registered users, which acks as a dashboard with a profile picture.

### Technologies Used
#### Languages Used
      1. HTML5 
2. CSS3
3. Javascript (jQuery)
4. Python

### Frameworks, Libraries & Programs
    
1. Code Institute Template - (https://github.com/Code-Institute-Org/gitpod-full-template)
2. Bootstrap 4 (https://getbootstrap.com/) was used to assist with the responsiveness and the Website's grid system.
3. Google Fonts (https://fonts.google.com/)were used to import the 'VT323' font into the style.css file which is used on all pages throughout the project. 
4. Font Awesome (https://fontawesome.com/) for the website icons for UX ease of use.
5. JQuery (https://jquery.com/) used along side the vanilla JS elements in script.js for html / style changes and as a DOM selector for some functions.
6. Gitpod (https://gitpod.io/) was used as a code development environment.
7. Git was used for version control by using the Gitpod terminal to commit to Git and Push to GitHub.
8. GitHub (https://github.com/) is used to store all the code for this project after pushing from Gitpod.
9. GIMP (https://www.gimp.org/fr/) was used to edit photos for the Website.
10. Balsamiq (https://balsamiq.com/) was used to create the wireframes during the design process.
11. Table generator(https://www.tablesgenerator.com/markdown_tables) for the table in the README
12. Carosuel from (https://kenwheeler.github.io/slick/)

# *Testing*

### ***Code validation***
In the project, no syntax errors were detected, as validated by -
#### W3C Markup Validator - 
- [Image-html](static/img/testing_images/Screenshot 2021-06-25 at 12-27-53 Showing results for https brew-book-block88 herokuapp com - Nu Html Checker.png)

#### W3C CSS Validator -
- [Image-css](static/img/testing_images/Screenshot 2021-06-25 at 12-22-07 W3C CSS Validator results for TextArea (CSS level 3 + SVG).png)

#### Lighthouse report -
- [Image-lighthouse-report-screenshot](static/img/testing_images/Screenshot 2021-06-25 at 12-43-57 Lighthouse Report Viewer.png)


### User Story testing
Number
User Story
Validation
Result 
1 

Confirmed by having all elements nessacary to play the game visble onload
Pass
2 
As a player/user of this app, I want there to be enough time for audio and aniamtion to engage with me.
The javascript has been updated to allow the enough time to have the audio play
Pass 
3 
As a player/user of this app, I want the game to be easy initally but to become gradually more challenging and I want the option to make it more difficult.
Confirmed through the addtional items to remember as each level progresses
Pass 
4 

As a  player/user of this app, I want the game to have a visually appealing theme, be simple, engaging and humourous.
Confirmed through the use of colours, cartoon images and humourous audio
Pass 
5 
As a player/user of this app, I want the game to initeate the directions for game play. 
Confirmed through the use of regular prompt messages which coax the player into action
Pass 
6 
As a  player/user of this app, I want to know when I've clicked on a button by having a responding audio or visual cue or both.
Confirmed by the player triggered javascript events changing various styles on the page and playing sound effects and but the hover elemenst in the css file
Pass 
7 

As a player/user of this app, I want to be able to play this on my phone or laptop.
Resposiveness functionality tested throughly on various phone screens to allow for better UX.
Pass 



###Manual Testing

Test Case
Description of feature
Result
1
When the site loads on a laptop the user should see a title, 4 image tiles and 4 buttons
Pass
2
Hovering over 'Start taking orders' button with the mouse cursor, the text turns from light shades to darker shades
Pass
3
Clicking on the 'Start taking orders' button changes the prompt message to alert the user to turn on the game
Pass
4
Clicking on the game button tiles when the game is OFF will trigger no affect
Pass
5
Normal/Hard button will always change text color to show it is active or not
Pass
6
On/off button will always change text color to show it is active or not
Pass
7
Clicking on the game button tiles when the game is ON  will trigger javascript events
Pass
8
Hovering over game tiles changes with the mouse cursor the background color and removes it when mouse leaves
Pass
9
Clicking on the Edit button will trigger a pop up window
Pass
10
Clicking on the tutorial pop up window will will trigger the window to close
Pass
11
Winning the game triggers a pop up modal
Pass
12
Clicking on the delete button will trigger a pop up window
Pass

















##Responsiveness Testing
#### Responsiveness
The Website was viewed on devices such as Desktop, Laptop, Huawei Y6, iPhone 5/6, iPhone 7/8, Samsung A1. 
######Screenshot – responsive design (proof of concept)

### *Using inspect elements on firefox i checked responsiveness for the following*
#### Phones -
Galaxy Note 3Android 4.3
Galaxy S5Android 5.0
Galaxy S9/S9+Android 7.0
iPhone 5/SEiOS 10.3.1
iPhone 6/7/8iOS 11
iPhone 6/7/8 PlusiOS 11
#### Tablets -
iPad
#### Laptops -
Laptop with HiDPI screen


## *Browser Testing*
The Website was tested on Firefox, Google Chrome, Microsoft Edge and Safari browsers. 
#### Issues Found -
- Had difficuly styling the Materialise css initialiy, but with the use of inspect element in the browser i found ways around problems i had.
#### Issues Found & Bugs -
-Many bugs with in the python/flask templates, often to do routes or speling/ indentation errors , this was also solved through hours of trial and error. To which i know have a better understanding of how these frameworks interact with each other and python with in a database and throughout a website with CRUD functionality.
-The text on the main page did not look good on some devices.
-The category page lists the cards in various sizes but i am still working on that one 
-The pop up modals in categorys section did not show up well on mobile devices on the main page did not look good on some devices.


## *Deployment*
The site was developed in GitPod and pushed to the following remote GitHub repository - (https://github.com/BarryBlock88/Insecure-Dangereux_site)
##### The following GIT commands were used throughout deployment:

1. git add. -to move files to the stage before commit. 
2. git commit - to commit the files in Gitpod, insert text on the main terminal instead of in brackets as in previous versions.
3. git push - to push the files to the master branch of your GitHub repository. 
4. git pull - on occasion when the push showed an error.

###Hosting on Heroku
The following steps were taken to complete the hosting process. 
Set debug=False in the app.py file. 
Created a requirements.txt file from the terminal, using pip3 freeze --local > requirements.txt, to allow Heroku to detect this project as a python app and any required package dependencies. 
Created a Procfile using echo web: python app.py > Procfile from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project. 
Created a new Heroku app and set its region to central Europe (or whereever is nearist to you). 
Automatic deployment was set up on Heroku - On the app dashboard, in the deploy menu. Connect to GitHub section. The GitHub repository was searched for and connected to the app. 
In the settings tab on the app dashboard, 'Reveal Config Vars' was used to tell Heroku which variableS are required to run the app. The following config vars were added: 
IP 
PORT 
SECRET_KEY 
MONGO_URI 
In GitPod, a check was completed to ensure the master branch was up to date and all commits had been pushed to GitHub, ready for Heroku to deploy. 
Clicked the Enable Automatic Deploys button located in the Deploy section of Heroku to allow for automatic deploys. 
Clicked the Deploy Branch button located in the Deploy section of Heroku to finally deploy this project. 
Clicked the View button to launch this project's app. 
The deployed site on Heroku will update automatically upon new commits to the master branch in the GitHub Repo.

# *Credits*


### Acknowledgements


##### Websites/Online services used for the project:

MongoDB - used to host user, recipe, comments and category data for the site in the form of databases/collections
Flask framework – for rendering and templates.
Gitpod - used as IDE for this project. 
Git - used for version control. 
Github - used to host repository. 
Heroku – for hosting website
Balsamiq - used to develop initial scratch wireframes. 
Firefox DevTools - used for testing and debugging the site. 
w3 html validator - used to test and validate my html code. 
w3 css validator - used to test and validate my CSS code. 
Materialise CSS – for grid system and Nav bar




## *Advice and support*

-Stack Overflow  for helping me understand problems i had from various angles
- All the lovely people who helped advise on Slack Community from past and present (various students and tutors) 
- My Mentor Caleb Mbakwe
- Code Institute - videos
- W3school for helping my understand bootstrap documentation

##Received inspiration for this project from: 
The following projects, websites and tutorials that I learned from to complete my project.
 ####Past Code Institue MS3 projects for inspiration, and snippets of  heroku deployment such as -
https://github.com/jamie120/ms3-eat-vegan-recipes.git 

https://deevdz-milestone-3.herokuapp.com/index/1

https://github.com/Code-Institute-Submissions/Nicola2309-MS3


####Websites, such as  -
https://www.brewersfriend.com/


 ####Tutorial -

https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/textIndexCommands.md

This mini project served as my main inspiration for creating my project and acted somewhat as a guide to help me understand how best to create the game and understand the underlining Python elements involved. The python/flask structure of the project is based on this video I modified the definitions, colours, themes, functions to show a different version other than the one id learned through the tutoiral. I watched the video several times over several days following the instructions to replicate the code, I then changed elements. The goal was to learn how to develop a similar database website application, understanding and modifing the python code as i went along, not plagurise the code from this tutorial without any knowledge of how it worked.(In fact several elements did not work for me initaly so I had quite alot of trial and error changing certain functions and booleans to understand the frameworks and the python used and to fix bugs that had been generated).
