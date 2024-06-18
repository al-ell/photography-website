# GL Photography -  Testing

[Am I Responsive?]()

Visit the deployed site: [Gwilym Llywelyn]()

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Python Validator](#python-validator)
  * [Lighthouse](#lighthouse)
  * [WAVE Testing](#wave-testing)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

- - -

## AUTOMATED TESTING

### W3C HTML Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website.


- - -

### W3C Jigsaw  Validator

[Jigsaw W3C](https://jigsaw.w3.org/css-validator/) was used to validate the CSS stylesheet.


- - -

### JS Hint Linter

[JSHint](https://jshint.com//) usded to validate Javascript.



- - -

### Python Validator

[PEP8](http://pep8online.com/) Inbuilt PEP8 checker used on Python files.



- - -

### Lighthouse

### Home Page
![homepage](/)

### Login Page
![login](/)

### Portfoilio/Wales Page
![portfolio - Wales]()

### Portfoilio/Discovery Page
![portfolio - Discovery]()


### Portfoilio Admin Page
![portfolio admin]()

### Add Project Page
![add project]()

### Edit Project Page
![edit project]()

### Add Photo Page
![add photo]()

### Edit Photo Page
![edit photo]()

### All Prints Page
![all prints]()

### Edit Photo Page
![edit photo]()

### Shop Admin Page
![shop admin]()

### Add Category Page
![add category]()

### Edit Category Page
![edit category]()

### Add Size Page
![add size]()

### Add Print Page
![add print]()

### Edit Print Page
![edit print]()

- - -

### WAVE Testing

Wave testing completed on all pages. No contrast errors, aria labels present on all features.

![Wave font to background result]()

- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? |
| :--- | :--- |
|`Admin User` |
| Manage products in the shop (add , update or delete products) | print and category admin pages |
| View created orders to fulfil or edit them | Admin back end allows the admin to see order details |
| View messages sent via contact form and can act upon them | contact form linked to site email address |
| `Website Visitors` |
| Register | Redirection to register page to allow signin, verification user exists |
| Login | Redirection to login page to allow signin, verification user exists |
| Browse photo galleries | Two pages of galleries linked to the projects |
| Search for products so that I can find specific products | Shop searchbar in nav |
| Sort products on criteria such as name and category | Sort input on prints page will sort by category or name |
| Browse through products so that I can decide what I may be interested in buying | Shop page for prints |
| Look at product details to find out more about the product | clicking on print card to get print details |
| Easily add products I want to purchase to a basket | Add to basket and quantity input |
| View the contents of my shopping basket so that I can be able to make any adjustments | Bag link in top nav |
| Update my bag by adding more or remove products so that I can decide on the number of products I intend to buy | Quantity adjustor with update and remove functions in the bag |
| View my order summary so that I can verify it before confirming | Order summary on page for customer details |
| Checkout securely so that I can I maintain the level of trust on the site | Use of stripe |
| Use the contact form so that I can contact the site owners | Contact form linked to website email address |
| Save my personal details after making a purchase | Option to save if checking out when signed in |
| Create or edit my account to update my details | Registration, login and profile pages |
| Login in my account so that I can view my order history | Links on profile page to order history summary |

#### Future Implementation

* Manage users' accounts so that I can make any required changes to them if needed
* Make new galleries and upload new images to the galleries 
* Users can add gallery images to favouries

- - -

### Full Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ----- | --- | --- | --- | --- |
| `Navbar` |
| Click on home page nav link | index page loads | clicking on link   | taken to page | pass      |
| Click on portfolio/wales page nav link | wales gallery page loads | clicking on link        | taken to page | pass      |
| Click on portfolio/discovery page nav link | discovery gallery page loads | clicking on link        | taken to page | pass      |
| Click on contact page nav link  | contact page loads | clicking on link        | taken to page   | pass      |
| Click on search nav link | searchbar loads | clicking on link        | taken to page | pass      |
| Click on shopping bag nav link | shopping bag page loads | clicking on link        | taken to page | pass      |
| Click on profile page nav link   | profile page loads  | clicking on link        | taken to page    | pass      |
| Click on login nav link  | User is taken to login page  | clicking on link        | taken to homepage and pages that can only be accessed when logged in |
| Click on signup nav link  | User is taken to signup page  | clicking on link        | taken to signup page |
| Click on logout nav link  | User is logged out  | clicking on link        | taken to homepage and pages that can only be accessed when logged out are shown | pass      |
| `Home Page` |
| Click on carousel arrows and buttons | skips to next or selected image | clicking on button |skips to next or selected image | pass 
| `Register Page` |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| enter an existing username into form | user is informed username is taken via message, form won't submit | entering an exisiting username | user is informed username is taken via flash message, form won't submit | pass |
| enter a password that doesn't match criteria | user is informed of password criteria, form won't submit | entering invalid details | user is informed of password criteria, form won't submit | pass |
| `Log in Page` |
| enter pre registered valid details into form | form submits | clicking on submit | taken to home page | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| enter an incorrect username or password into form | user is informed username or password is incorred via flash message, form won't submit | entering invalid details | user is informed username or password is incorred via flash message, form won't submit | pass |
| `Manage Portfolio` |
| Click on "add project" button | taken to add project page | clicking on button | taken to add project page | pass |
| Click on "edit project" button | taken to edit project page, prepopulated with selected project | clicking on button | taken to  edit project page | pass |
| Click on "add photo" button | taken to add photo page | clicking on button | taken to add photo page | pass |
| Click on "edit photo" button | taken to edit photo page, prepopulated with selected photo info | clicking on button | taken to  edit photo page, prepopulated with selected photo info | pass |
| Click on "delete" buttons | taken to delete confirmation page | clicking on delete button | taken to delete confirmation page | pass |
| `Add Project Page`|
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only contains a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing project name into form | user is informed project name is taken via flash message, form won't submit | entering an exisiting existing project | user is informed project name is taken via flash message, form won't submit | pass |
| `Edit Project Page` |
| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on portfolio admin page | form is pre-populated | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing project name into form | user is informed project name is taken via flash message, form won't submit | entering an exisiting existing project | user is informed project name is taken via flash message, form won't submit | pass |
| `Add Photo Page`|
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only contains a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing photo name into form | user is informed photo name is taken via flash message, form won't submit | entering an exisiting existing photo | user is informed photo name is taken via flash message, form won't submit | pass |
| `Edit Photo Page` |
| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on portfolio admin page | form is pre-populated | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing photo name into form | user is informed photo name is taken via flash message, form won't submit | entering an exisiting existing photo | user is informed photo name is taken via flash message, form won't submit | pass |
| `Manage Shop Page`|
| Click on "add category" button | taken to add category page | clicking on button | taken to add category page | pass |
| Click on "edit category" button | taken to edit category page, prepopulated with selected category | clicking on button | taken to  edit category page | pass |
| Click on "add photo" button | taken to add photo page | clicking on button | taken to add photo page | pass |
| Click on "edit photo" button | taken to edit photo page, prepopulated with selected photo info | clicking on button | taken to  edit photo page, prepopulated with selected photo info | pass |
| Click on "delete" buttons | taken to delete confirmation page | clicking on delete button | taken to delete confirmation page | pass |
| `Add Category Page`|
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only contains a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing category name into form | user is informed category name is taken via flash message, form won't submit | entering an exisiting existing category | user is informed category name is taken via flash message, form won't submit | pass |
| `Edit Category Page` |
| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on shop admin page | form is pre-populated | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing category name into form | user is informed category name is taken via flash message, form won't submit | entering an exisiting existing category | user is informed category name is taken via flash message, form won't submit | pass |
| `Add Print Page`|
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only contains a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing print name into form | user is informed print name is taken via flash message, form won't submit | entering an exisiting existing print | user is informed print name is taken via flash message, form won't submit | pass |
| `Edit Print Page` |
| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on shop admin page | form is pre-populated | pass |
| enter invalid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing print name into form | user is informed print name is taken via flash message, form won't submit | entering an exisiting existing print | user is informed print name is taken via flash message, form won't submit | pass |
| `Bag Page`|
| Update the quantity of items in the bag using quantity adjuster | quantity will go up or down depending on buttons pressed | clicking on up and down buttons and update | quantity will go up or down depending on buttons pressed | pass |
| remove an item from the bag using remove button| item is removed | clicking on up and down buttons and update | item is removed | pass |
| Click back to prints button | taken back to all prints | clicking button | taken back to all prints | pass |
| Click checkout button | taken to checkout | clicking button | taken to checkout | pass |
| `Checkout Page`|
| enter invalid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter invalid details into Stripe payment | user is informed data not valid, form won't submit | entering invalid details |  messages tell the user data is not valid | pass |
| Click back to bag button | taken back to bag | clicking button | taken back to bag | pass |
| Click complete purchase button | taken to checkout success, order processes and payment taken | clicking button | taken to checkout success, order processes and payment taken | pass |
| `Profile Page`|
| enter invalid details into form | user is informed data not valid, form won't submit | entering invalid details | messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| click update details button | form updates | entering invalid details | form updates | pass |
| click on order history link (order no.) | taken to order history page | clicking on link | taken to order history page | pass |
| `Delete Confirmation Page` |
| click on the "cancel" button | taken back to previous page | clicking cancel | taken back to previous page | pass |
|click on the "delete" button | item is deleted, taken back to previous page | clicking delete | item is deleted, taken back to previous page | pass |
| `Portfolio Project Pages` |
| click on image | Fancybox gallery pops up | clicking on any image | Fancybox gallery pops up | pass |
| `All Prints Page` |
| click on image in card | Print info page loads | clicking on any image | Print info page loads | pass |
| sort print name ascending | prints sort A - Z | selecting the option in the dropdown | prints sort A - Z | pass |
| sort print name descending | prints sort Z - A | selecting the option in the dropdown | prints sort Z - A | pass |
| sort category name ascending | sort by category name A - Z | selecting the option in the dropdown | sort by category name A - Z | pass |
| sort category name ascending | sort by category name Z - A | selecting the option in the dropdown | sort by category name Z - A | pass |
| filter to project name | only prints from that project will show | clicking filter link | only prints from that project show | pass |
| clear filter to view all prints | all prints now show | clicking filter link | all prints now show | pass |
| `Print Info` |
| choose a print size to display price | using size dropdown, displayed price will change | selecting option in dropdown | price changes depending on selected size | pass |
| Adjust quantity to add to the bag using adjuster | quantity adjusts | clicking on buttons | quantity adjusts | pass |
| Click back to prints button | taken back to all prints | clicking button | taken back to all prints | pass |
| Click add to bag button | added to bag, success message, bag total updates in nav | clicking button | added to bag, success message, bag total updates in nav | pass |
| `Contact Page` |

| `Accessability`  |
| title, alt text or aria features for all non-text media | text appears/screenreader will read out                                            | hovering over media     | text appears/screenreader will read out | pass      |

 - - -

## BUGS

### Solved Bugs

| Bug | How I solved the issue | Image |
| :--- | :--- | :--- |
|


- - -

### Known Bugs

| Bug | |
| :--- | :--- | |