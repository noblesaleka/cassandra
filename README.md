         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


# E-commerce store
Hello, My name is Saleka and through this project I am excited to present to you
another in a series of web applications on my journey through code institutes Full-Stack web development program. Welcome to fullstack frameworks with django.
This project is an application which allows the user to create a profile, and was intended so the user to be able to  purchase a product from the site using stripe payments. 
This application provides a realistic e-commerce patform that allows for the owner of the site to earn money, 
while the user is able to find the most exciting products at the click of a button.
I created this project in order to produce a functional e-commerce platform that utilizes django and stripe payments to process oders.
Welcome to my portfolio Full-Stack Frameworks with Django!

 
## UX
 
This website is designed for the to be user focused allowing the user to really take advantage of the website, by adding to basket, removing items, and seeing their downloads of high quality photos checkout total in real time. Thus allowing for full crud functionality.


 A list of user Stories:

<a href= "files/Conceptual design cassandra.pdf">Conceptual design pdf</a>
- As a user type, I want to perform an action, so that I can achieve a goal.
- As a user I want to listen to buy photos
- One photo many has many users to buy digital downloads
- A user can create a profile
- A user can buy many photos
- Each profile has a user which stores their downloaded purchased photos
- A user can purchase many photos, but each photo can only be purchesed by one user


## Features

This section describes the different parts of my e-commerce digital download platform:
The all products page allows you to view a single photo or many photos and all the information related to that photo.
The all photos page is simply the combination of all the photos from a broad variety of categories across the website, you can view our enitre library from this page. Also it allows for 
filtering on a high level. Can use the search bar to filter your search results.
The base page is the base template for the websites look and feel which was inspired by <a href= "https://www.chapters.indigo.ca/">Indigo</a>, and <a href= "https://www.chapters.indigo.ca/">Unsplash</a>.
The profile page contains the user registration information where they fill their personal information.
The categories page is further broken down into several different genres that the user can further explore  including abstract, animals, building, food, nature and more.
Users also have the option to purhcase an unlimited plan whereby they have access to unlimited downloads for a monthly fee of $10 USD.
Finally we have the login and logout functionalities which give acces to other options, such as view their previous orders and redownload their files.

### Existing Features
- Feature 1 - allows users to preview photos from various photographers for sale
- Feature 2 allows users to browse and search, for a particular photo throughout various genres
- Feature 3 allows users to update their profile and information 
- Feature 4 allows users to view the price of the current photo they are previewing
- Feature 5 allows users to have an acccount in order to track their purchases 
- Feature 8 A place where superusers can upload photos with easy navigatgion

### Features Left to Implement
- Feature to pay monthly with stripe (TBA)
- Upgraded user interface which impliments  gsap technology animations 
- Add a section where users can favorite a photo and download a watermarked image (similar to amazon.com functionality)
- Form validation to return error message when registration form is not completed properly
- send automatic followup marketing email content to all subscibers, providing deals of the week through a blog page intergration for additinal user engagement

## Technologies Used

- [JQuery](https://jquery.com) library
- HTML, used to dictate the structure of my web application
- python used as the primary backend language inside django framework
- CSS, used to style my pages 
- Heroku, used to deploy the project to the live server for viewing by the public
- The project uses **JQuery** to simplify DOM manipulation.
- Django framework, used as backend framework
- Bootstrap v4.0.0  used for website cross campatibility across devices
- Fontawsome used for fonts
- SQLite3, used to access my database from the console
- JavaScript, used for front end password verification
- Stripe used for payment services 
- Postgres is a relational database management system 



## Testing

The testing process for this project was ongoing throughout, I made use of unit testing in a variety of scenerios.

1. All Product page:
    1. Go to the "Products" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears
2. Login/Logout
    1.Confirm that login works and login validation message is displayed on the home page
    2.Try access profile without logining in
    3.Try to fill out registration form with incomplete fields and verify it does not create a user account
    4.Try to logout and login using and different password but same username and verify that display message is; your password is incorrect!
3.Registration
    1. Try to see if I can register without filling the form and verify its not possible by submiting
    2. Try to register again if I already have an account
4.Photos
    1.Try to submit a incomplete photo form verify it doesn't submit
    2.Try to unsubmit my photo by going back on the page link (browser navigation)
5.Edit profile
    1.Try Django templating form, verify it is updating registration information on click of submit
    2.Try user profile and make sure photo information and user information are the same 
    3.Verify user profile is being saved inside the Django admin panel
6.Search
    1.Try the filtered search feature by category.

I have also tested my project on various screen sizes from a laptop to a desktop.Ensuring that bootstraps intelligent sizing features have adjusted the page size.
Everything is able to collapse neatly when on a phone screen to yield a functional user interface wich cleanly represent the e-commerce brand.

Here is a list of bugs encountered and their solutions during the development process:

1. error - stripe card on membership/payment not rendering correctly - no fix

2. error - loading data in bulk to heroku environment, created a data.json file, and loaded it directly to create records

3. error - index not found, caused by deleting incorrect columns

4. error - major error server 500 in heroku - rolled back to previous checkpoint without functionalities.


## Deployment
Process to deploy:
- This project has been deployed to heroku
- Different values for environment variables/Heroku Configuration varibales were set
- Created requiremnent.txt and procfile in order to host on Heroku  platform
- Deployed to Heroku server for final project viewing 
- This project was deployed to GitHub. It can be accessed via this link: [https://github.com/noblesaleka/cassandra/settings]
- This project was deployed to Heroku. It can be accessed via this link: [https://cassandra-django-milestone.herokuapp.com/]

## Credits
I would like to credit numerous cites for inspiration in ux design as I could 
not have done this without inspiration and at times a little persperation. Cite 
used for application inspiration <a href="https://www.canva.com/">here.</a> 
I would also like to credit the stackoverflow community for any methods and 
code snippets used, it was a really awesome resource to roll up my sleeves and 
learn on the website.
I would also like to credit the Code Institue, which provided the basis of the logic and design.
### Content
- The text for all the paragraphs was inspired by:
- https://www.chapters.indigo.ca/en-ca/

### Media
- Unsplash
- canva


### Acknowledgements

I would like to acknowledge w3schools.com for when I got stuck. Also the use of 
several bootstrap components used to build the framework of my project.
I also searched stackoverflow.com countless
times for more information to solve problems with my application when I was puzzled and challenged
on the harder portions. I am thankful that my project is finally closer to what I 
envisioned. Thank you for viewing this presentation of my 
Full-Stack Frameworks with Django project. 
                                                <a href="#top">Back to top</a>
### This is for educational use.
