
![logo-full](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/c90b600b-032f-4f06-a45d-83f5c9c7b58e)

# MiniFolio

Welcome to MiniFolio, an online platform that brings together the vibrant worlds of board game miniatures and Warhammer figurines. MiniFolio empowers enthusiasts and artists to proudly showcase their meticulously painted creations, engage with a community, and find inspiration in the artistry of miniature gaming.
<br>
Live Site <a href="https://minifolioapp-b0e53ffaa426.herokuapp.com/">MiniFolio</a> 
<br>


## Site-Goals

The primary goal of the site is to empower users to proudly showcase their meticulously painted board game miniatures and Warhammer creations.

It also aims to create a space where artists of all skill levels can display their work and receive recognition for their dedication and creativity.

The site also provides a seamless and intuitive user experience. It is designed to be user-friendly, ensuring that both newcomers and experienced hobbiests can engage with ease.


## Site Epics

**Epic 1: Basic Setup**

The "Basic Setup" epic involves the foundational steps to prepare the MiniFolio platform for users. This includes configuring the essential infrastructure and database components necessary to support the core functionalities. Basic setup sets the stage for user engagement and the seamless display of board game and Warhammer miniatures.


#### Initial Implentation setup:

As a developer, I need to **set up the project** so that **it is ready for implementation**

**Acceptance Criteria**

- Django installed
- Project created
- Environment variables set up
- Settings.py set with the correct variables and dependencies
- Soft Deploy to Heroku

This story was for getting setup correct for the implemenation  of Minifolio

#### Database Setup:

As a **developer** I need to **map out and build the database**  so that **the site can store user data and posts**

**Acceptance Criteria"" 

- Create a workflow of the database and the columns
- Build out the basic models in a models.py files.


Here is my custom DB for Minifolio: 

![minifoliodb](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/1b90d2cc-7e3c-4a4b-9795-aee9752fe485)

This story was for the initial set up of the database ready for implmentaion


#### Landing Page

As a **Developer** I need to **create a landing page**  so that **users know they have arrived at the site**

**Acceptance Criteria**

- Create an index.html
- Style index.html
- Add a login button
- Add a register button

This story was for me as a developer to create a landing page so that the users know they have reached MiniFolio.
The landing page has been built to bring in users to the site: 

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/9a924d72-0ecc-4bf1-b39a-37f84fb800dc)



**Epic 2: User Registration and Profile Setup**

In the "User Registration and Profile Setup" epic, users are provided with a seamless onboarding experience. They can register using their email and password, creating personalized accounts. This epic also encompasses the development of profile customization features, allowing users to add profile pictures, bios, and specify their interests within the realm of miniature art.

#### Account Creation & Custom User Profile

##### Account creation
As a **developer** I can **create a user registration form**  so that **so that users can create accounts using their email and password**

**Acceptance Criteria:**
- Users can input their email and password.
- Allauth used for signup

##### Custom User Profile
As a **user** I can **customise my profile** so that it **so it displays my a little bio and all my posts.**

**Acceptance Criteria**

- Create a user profile page and style.
- The user can upload a profile photo and change the photo
- The user can create and edit a bio 


The storys come hand in hand as when the user registers with us this takes them straight to the create profile page. 

The user starts with signing up where they create a username with a password and if they want to use an email they can. 
Once this is created they then get taken to the create profile where they can set there bio and profile picture.

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/be3df7bb-bb3b-44d4-872d-3ccc3de56955)

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/f2d3931f-d1df-402a-b6a0-62931a35cb5e)

The user can then click on the profile linke in the nav where this will take them to their personal profile. 
If the user click edit profile this will load the edit profile form.
In the profile page as well the user will see all of there posts they a created. 

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/048f3184-7a49-416b-a520-de554316e7ae)


#### Login/Logout 

As a **developer** I need to **create a login /Logout button**  so that **when a user comes back to the site they can login and out**

**Acceptance Criteria**

- Create a login/logout button 
-  Use AllAuth for user authentication

The user is able to login and out via the nav bar or via the landing page Login button.
The login auithentication used for this was Allauth. 

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/47251497-a6c7-4d09-bd50-5d29bd829a1a)

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/4c7c140b-e8e8-4878-b8aa-36ee3a05811b)



**Epic 3: Displaying Miniatures**

The "Displaying Miniatures" epic revolves around enabling users to showcase their board game and Warhammer miniatures. This involves building the functionality for users to upload images, add titles and descriptions. The epic emphasizes creating an appealing and organized display for users' miniature collections.

#### Viewing Posts

As a **user** I can **view other users posts** so that **I can view images and details of posts**

**Acceptance Criteria:**

- Users can see a feed of posts from other users.
- Each post displays the image, description, and author information.

#### Adding Captions to Posts

As a **developer** I want users **to add a description to their post**  so that **they can describe and instruct others**.

**Acceptance Criteria:**

- Users can enter a text caption for each post.
- Captions should only be a 500 characters long.

#### Image Upload

As a **developer** I want to **enable users to upload images**  so that **they can showcase their miniatures**

**Acceptance Criteria:**
- Users can upload image files.
- Uploaded images should be properly stored and associated with the user's account.


This epic and story was built around a user being able to upload a post to Minifolio and view other peoples posts.
The main core objectives were to allow the user to upload a photo and add a captions to them. 
The user can initiate the upload with the upload button in the footer: <br>


![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/7597739b-b53f-4c3c-83cc-e64c7fcc6b67)

Or click Create in the Nav:

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/cad1a1e7-3b48-4c1d-86f5-a16056d542b8)

This will then take them to the pload form where the user can create a header, upload an image, select a category and write a caption for the post.

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/9a448312-a160-4689-93f2-bf801e115a01)

Once the post has been created they then are directed to the home page where they will see everyones posts. <br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/334bfe1a-5fc0-41f4-8531-02d6240486aa)


**Epic 4: Interacting with Miniatures**

Within the "Interacting with Miniatures" epic, the focus shifts to user engagement. Users are granted the ability to view, comment on, and like posts by fellow enthusiasts. These interactive features foster a sense of community, allowing users to connect, provide feedback, and appreciate the miniature artistry of others.

#### View a Game Specific Category

As a **user** I can **search for game specific category's** so that **I can search look at specific miniatures**

**Acceptance Criteria**

- User is able to see category based posts
- Create a category's page

When a user is creating a post the have to select a category for the post to go into. 
The posts the all link together and the users are able to go to the categorys page and look at posts in that one category. 
The user also cal click the category on the post and this will dircet the to that category. <br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/b0013b24-c302-404d-9a4d-35073f8c704b)

<br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/2baa10e3-912c-4c59-bb10-ee2d954a3225)
<br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/d91fc9b9-7ad0-44b4-9fcf-8e82a09434f2)

#### Commenting on Posts

As a **user** I can **comment on posts**  so that **I can interact with posts and the community**.

**Acceptance Criteria:**

- Users can write and submit comments on posts.
- Comments should be displayed with the author's name


Users are able to interact with each other by commenting on each others posts. 
They are able to do this by clicking on the Show Comments drop down link which revealse the comment button 
<br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/91fe1f1f-6aee-4309-b187-a15d97555af2)

For the user to post a comment they need to click the comment buttong which will take them to the comment form where they can create their comment, <br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/d7be034c-eda0-4515-9f76-c0acfe7000b2)

This will then display on the post. 

#### Liking Posts

As a **developer** I want users to be able to  **like, super like and dislike posts** so that **the user can interact with the community**.

**Acceptance Criteria:**
- Users can click a "like" button on posts.
-  Users can click a "dislike" button on posts.
-  User can click a "super like" button on posts
- The total number of likes should be displayed for each post.

The users are able to Up vote, down vote and super like a post how ever due to issues in development in this sprint we were unable to add a unlike function.
The like function works and adds to the tally which covers this story but it has been moved to blocker till we are able to implement the un like function. <br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/bb943a9f-d6fe-407b-96fe-8ec3e956e65a)





**Epic 5: Editing and Deleting my Miniatures**

The "Editing and Deleting my Miniatures" epic empowers users with control over their showcased content. Users can edit post details such as titles and descriptions to reflect their growth and refinement as miniature artists. Additionally, users can opt to delete posts that no longer align with their preferences or skill levels, ensuring the quality of their showcased portfolio.

#### Editing Posts

As a **user** I can **edit my post** so that **I can update my posts**

**Acceptance Criteria:**
- Users can edit the title and description fields of their own posts.
- Changes are saved and reflected in the post details.

The user is able to edit their posts by clicking the edit link in the post, this takes the user to the edit for where they can edit there post.  <br>


![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/b0fd0782-3f48-4d1c-9306-286348ff7750)


#### Deleting Posts

As a **user** I can **delete my posts**  so that **I can remove my posts if I don't like them any more**

**Acceptance Criteria:**
- Users can initiate the deletion of a post.
- Warning pop up before deletion

The user is able to delete their post by click on the delete linke on the post itself.
Once they have clicked that they will be taken to a confimation page where they will be asked are they sure the want to delete. <br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/22ae8598-cc95-45b6-8ecf-ffdb097ee5e5)


Together, these 5 epics contribute to the creation of MiniFolio as an engaging and community-driven platform for miniature enthusiasts, providing a space to display, appreciate, and interact with board game and Warhammer miniatures.


### Layout & Design:

Minifolio was built mobile first but is responsive on all devices.

#### Skelton Layouts:

Landing Page : <br> 

![landing page](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/69c8d51f-fa23-46dc-8e86-7a3f1eadcc15)

Home Page : <br>

![blogScroll](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/184d7e6c-20af-4360-a44e-5fe9be224f4a)


Login & Register: <br>

![login register](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/cb767e95-adcc-41fa-a1fa-326c706601f7)


Profile and Posts: <br>

![profile post](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/3032cb27-893b-4441-82fd-c21ef62aabb2)


## Testing 

### Creating an Account

* Is the user directed to the registration form upon clicking the "Register" button?
   * Yes, clicking the Register button successfully navigates the user to the registration form.
   * I have tested this by clicking on the Register button.

* Can the user input their registration details?
    * Yes, the user is able to enter their registration details successfully.
    * I have tested this by adding details to the form

* Does clicking the Sign up button after entering details redirect the user to the profile creation page?
   * Yes, clicking the Sign up button after entering details takes the user to the profile creation page.
   * I have tested this by clicking the Sign up button

* Can the user upload a profile photo during profile creation?
   * Yes, the user can successfully upload a profile photo.
   * I have tested this by adding a image from my phone and computer

* Can the user include a bio in their profile?
   * Yes, the user can successfully add a bio to their profile.
   * I have tested this by entering a bio

* Is the user directed to the home page after clicking the Submit button on the profile creation page?
   * Yes, clicking the Submit button on the profile creation page successfully navigates the user to the home page.
   * I have tested this.

### Edit Profile

* Is the user directed to the profile editing form page?
    * Yes, clicking "Edit" on the profile page successfully directs the user to the profile editing form.
    * I have tested this by clicking the "Edit" button on the profile page.

* Can the user edit their profile image and bio?
    * Yes, the user can edit their profile image and bio successfully.
    * I have tested this by making changes to the profile image and bio in the edit form.

* Is the user directed to the home page after clicking the Submit button on the profile creation page?
    * Yes, clicking the "Submit" button on the profile editing page successfully directs the user to the home page.
    * I have tested this by clicking the "Submit" button after making profile edits.

* Does the user's profile display the updated information after editing?
    * Yes, the user's profile reflects the updated information.
    * I have tested this by checking the profile page for the changes made during editing.

* Is the user directed to the home page after clicking the "Cancel" link on the profile editing page?
    * Yes, clicking the "Cancel" link on the profile editing page successfully directs the user to the home page.
    * I have tested this by clicking the "Cancel" link during the profile editing process.

### Creating a Post

* Is the user directed to the post form upon clicking the Create link and icon.
    * Yes, clicking the "Create" button successfully navigates the user to the post form.
    * I have tested this by clicking on the "Create" button.


* Can enter header, image, category, and caption.

    * Yes, the user can enter the header, image, category, and caption successfully.
    * I have tested this by entering the respective details into the form.


* User clicks "Post" and posts image, then redirects home, and can see the post in the home view.

    * Yes, when the user clicks the "Post" button, the image is posted, and the user is redirected to the home page where they can see the post.
    * I have tested this by posting an image and verifying its presence in the home view.
    * The user can also see the post in a specific category and in their profile.
 
 ### Editing a Post

* Can the user click "Edit" on a post?
    * Yes, the user is able to click the "Edit" option on a post.
    * I have tested this by clicking the "Edit" button associated with a post.

* Does clicking "Edit" direct the user to the edit form?
    * Yes, clicking "Edit" directs the user to the edit form where they can change the image, header, and caption.
    * I have tested this by clicking "Edit" and verifying that the edit form is displayed.

* Can the user modify the image, header, and caption in the edit form?
    * Yes, the user is able to change the image, header, and caption in the edit form.
    * I have tested this by making modifications to each of these elements in the edit form.

* Can the user submit the edited post?
    * Yes, the user can successfully submit the edited post.
    * I have tested this by clicking the "Submit" button in the edit form and verifying that the post is updated.

* Does clicking "Submit" take the user back to the home page after post update?
    * Yes, clicking "Submit" redirects the user to the home page after successfully updating the post.
    * I have tested this by clicking "Submit" and confirming that I am taken back to the home page.

* Can the user cancel the edit process by clicking a cancel link?
    * Yes, the user can cancel the edit process by clicking a cancel link that takes them back to the home page.
    * I have tested this by clicking the cancel link during the edit process and confirming that I am returned to the home page

### Deleting a Post

* Can the user click the "Delete" option on the post.
    * Yes, the user is able to initiate the deletion process successfully.
    * I have tested this by clicking the "Delete" option on a post.

* Does the user get directed to confirmation page.
    * Yes, after clicking "Delete," the user is redirected to a confirmation page.
    * I have tested this by clicking the "Delete" option and observing the subsequent page.

* Can the user click "Submit" on the confirmation page.
    * Yes, clicking "Submit" on the confirmation page effectively deletes the post.
    * I have tested this by clicking "Submit" after being directed to the confirmation page.


* Does the user return to the home page.
    *Yes, after successfully deleting the post, the user is returned to the home page.
    *I have tested this by deleting a post and checking that I am on the home page afterward.


* Can the user see their post in their profile?.
    * The deleted post is not present in the user's profile.
    * I have tested this by verifying the absence of the deleted post in the user's profile.

* Can the user click the "Cancel" link on the confirmation page.
    * Yes, clicking the "Cancel" link on the confirmation page effectively cancels the deletion process and returns the user to the home page.
    * I have tested this by clicking the "Cancel" link on the confirmation page.
 
  ### Viewing a User

* Is the user directed to the Creators profile?
    * Yes, the user is directed to the Post Creator's profile page.
    * I have tested this by clicking on anothers creator's name in a post.

* Is the user able to see all posts by that Creator?
    * Yes the user is able to see only posts by that creator.


### Commenting on a post

* Is the user able to click "Show Comments" in a post?
    * Yes, the user is able to click "Show Comments" in a post.
    * I have tested this by clicking on the "Show Comments" button within a post.


* Does the dropdown work and show comments if there are any?
    * Yes, the dropdown works and shows comments if there are any.
    * I have tested this by clicking on the dropdown icon and verifying that comments are displayed when available.

* Is the user able to post a comment?
    * Yes, the user is able to post a comment.
    * I have tested this by clicking the "Comment" button within the post.

* Is the user directed to the comment form after clicking the "Comment" button?
    * Yes, the user is directed to the comment form after clicking the "Comment" button.
    * I have tested this by clicking the "Comment" button and confirming that the comment form is displayed.

* Is there an option to cancel the comment and return to the home page?
    * Yes, there is an option to cancel the comment and return to the home page.
    * I have tested this by clicking the "Cancel" link within the comment form and confirming that it takes the user back to the home page.

### Superlike, Upvote, and Downvote

* Can the user superlike a post?
    * Yes, the user can superlike a post successfully.
    * I have tested this by clicking the superlike button on a post.
  
* Can the user upvote a post?
    * Yes, the user can upvote a post successfully.
    * I have tested this by clicking the upvote button on a post.

* Can the user downvote a post?
    * Yes, the user can downvote a post successfully.
    * I have tested this by clicking the downvote button on a post.

* Can a user unlike a post?
    * Currently not, this was due to problems during development building this feature.
    * I will be looking to implement in the next availble sprint.


### Categories

* Can the user view different board game categories?
    * Yes, the user can view different board game categories.
    * I have tested this by clicking on each category.

* Do all the related posts display when clicking on a category?
    * Yes, when clicking on a board game category, all related posts are displayed.
    * I have tested this by selecting different categories and verifying the post listings.

* Can the user access a category by clicking the link in a post?
    * Yes, the user can access a category by clicking the link in a post.
    * I have tested this by clicking on category links within various posts.

### Validator Testing

* Lighthouse Testing: <br>

![image](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/5d09756e-3951-4015-be32-ed7f66b72035)

* W3 Validator :
Because of the Django templating language code integrated into the HTML files, they cannot be directly copied and pasted into the validator.
Additionally, secured views, which include pages requiring login or have restricted access, cannot undergo validation via direct URI entry.

To validate these files, you can follow these steps:

* Open the page you wish to validate.
* Right-click and select "View Page Source." This will display the raw HTML code.
* Copy the raw HTML code.
* Paste this code into the validator. This will ensure that only the HTML rendered code is validated. 

I did get two errors that I havent been able to resolve, first one I got the exact same error on the edit-post.html and edit-profile.html. <br>


![editpost](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/c810426d-f518-48d5-a7ff-979ad9442063)

I believe the issue is due to passing the post.pk throught the forms action giving me the error.
Resolution - Would need to pass through the primary key in a different way to clear the error. 

Second Error: <br>

![Upload-Post-Error](https://github.com/JamieB92/MiniFolio-PP4/assets/117354147/eed64383-a1c7-4581-b4b5-1f50ed0c03f2)

Means that I can't set a max length because it is a select field which is a dropdown and user can't enter text so the values are populated.
Resolution - Would need create a choice field in the form and the add each individual category to the model.py.
Unfortunetly I ran out of time to fix this. 


* CI Python Linter:
  Everyhting has passed but staticstorage and authpassword in settings.py as they were too long but I was unable to find a fix for that.
  Also in env.py the cloudinary url was too long also which I also couldnt find a fix. 

## Deployment:

### ElephantSQL:

* Navigate to https://www.elephantsql.com/
* Click Login/Creat a account.
* Click "Create New Instance".
* Create a name for the instance.
* Select Tiny Turtle.
* Leave Tags empty and click "Select Region".
* Select your region.
* Click Review in the bottom right corner.
* Click Create instance.
* Click on your newly created instance.
* Copy the URL and paste into your project and Heroku

### Heroku:

* Navigate to Heroku and create an account if not already registered.
* Click the "New" button.
* Select "Create New App."
* Provide an app name.
* Choose a region and click "Create App."
* Go to the "Settings" tab and click "Reveal Config Vars."
* Add the following configuration variables:
    * SECRET_KEY: (Your secret key)
    * DATABASE_URL: (You should already have this if you created an elephantSQL PostGresdb)
    * CLOUNDINARY_URL: (Cloudinary API URL)
    * PORT: 8000
    * Click the "Deploy" tab.
* Scroll down to "Connect to GitHub" and sign in/authorize when prompted.
* In the search box, locate the repository you wish to deploy and click "Connect."
* Scroll down to "Manual Deploy" and select the main branch.
* Click "Deploy."
* The app should now be successfully deployed.
* <a href="https://minifolioapp-b0e53ffaa426.herokuapp.com/">Live Site</a> 


## Technolgies Used

* HTML
* CSS
* Python
* Github
* CodeAnywhere (IDE)
* Git
* Font Awesome(Logo)
* Adobe Express
* Bootstrap(Navbar & Carosel)
* Cloudinary (Static File Hosting)
* Postgres SQL (Database)
* Elephant SQL (DataBase Hosting) 
* Heroku (Site Hosting)
* DbVisualizer

## Dependancies installed

* Django 3.2
* gunicorn
* dj_database_url==0.5.0
* psycopg2
* dj3-cloudinary-storage
* urllib3==1.26.15
* AllAuth
* django-summernote
* Crispy Forms

## Credit's

* Buttons - https://uiverse.io/simontheonlyone/loud-husky-59
* Form input - https://uiverse.io/Yaseen549/stale-frog-25
* Imgaes For Carosel:
    * Erik Swison - Instagram
    * Napking Workshop - Instagram
    * Nomad Paintworks - Instagram
* Nemesis Post Image:
    * Creaking Sheleves Review
* Tutorial
    * Codemy - Django blog was referenced for categories and liking a post
    * Code Institute - Blog walk through 
