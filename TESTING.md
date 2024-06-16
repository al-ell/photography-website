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
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| enter an existing username into form | user is informed username is taken via message, form won't submit | entering an exisiting username | user is informed username is taken via flash message, form won't submit | pass |
| enter a password that doesn't match criteria | user is informed of password criteria, form won't submit | entering invalid details | user is informed of password criteria, form won't submit | pass |
| `Log in Page` |
| enter pre registered valid details into form | form submits | clicking on submit | taken to home page | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| enter an incorrect username or password into form | user is informed username or password is incorred via flash message, form won't submit | entering invalid details | user is informed username or password is incorred via flash message, form won't submit | pass |

| `Manage Portfolio` |
| Click on "add project" button | taken to add project page | clicking on button | taken to add project page | pass |
| Click on "edit project" button | taken to edit project page, prepopulated with selected project | clicking on button | taken to  edit project page | pass |
| Click on "add photo" button | taken to add photo page | clicking on button | taken to add photo page | pass |
| Click on "edit photo" button | taken to edit photo page, prepopulated with selected photo info | clicking on button | taken to  edit photo page, prepopulated with selected photo info | pass |
| Click on "delete" buttons | taken to delete confirmation page | clicking on delete button | taken to delete confirmation page | pass |
| `Add Project Page`|

| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| leave any details blank or only contains a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing project name into form | user is informed project name is taken via flash message, form won't submit | entering an exisiting existing project | user is informed project name is taken via flash message, form won't submit | pass |
| `Edit Project Page` |

| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on trips page | form is pre-populated | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing trip name into form | user is informed trip name is taken via flash message, form won't submit | entering an exisiting existing trip | user is informed trip name is taken via flash message, form won't submit | pass |

| `Add Photo Page`|
| `Edit Photo Page`|


| `Manage Shop Page`|
| `Add Category Page`|
| `Edit Category Page`|
| `Add Print Page`|
| `Edit Print Page`|

| `Bag Page`|
| `Checkout Page`|
| `Profile Page`|

| `About Page`|






| `Delete Confirmation Page` |
| click on the "cancel" button | taken back to previous page | clicking cancel | taken back to previous page | pass |
|click on the "delete" button | item is deleted, taken back to previous page | clicking delete | item is deleted, taken back to previous page | pass |
| `Accessability`  |
| title, alt text or aria features for all non-text media | text appears/screenreader will read out                                            | hovering over media     | text appears/screenreader will read out | pass      |

 - - -

## BUGS

### Solved Bugs

| Bug | How I solved the issue | Image |
| :--- | :--- | :--- |



- - -

### Known Bugs

| Bug | |
| :--- | :--- | |