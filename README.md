# Gwilym Llywelyn

## Introduction


Link to deployed site can be found [Here]()


# Purpose

To create a functional website for the documentary photographer Gwilym Llywelyn to showcase his previous project work. The website will have distinct portfolio and shop sections as this follows the design layout of many artist's websites.


# UX
## User stories
## As Admin:
* I can manage users' accounts so that I can make any required changes to them if needed
* I can make new galleries and upload new images to the galleries
* I can manage products in the shop (add , update or delete products)
* I can view created orders to fulfil or edit them
* I can view messages sent via contact form and can act upon them

## As a site user:
* Before logging in:
	* I can browse photo galleries
	* I can search for products so that I can find specific products
	* I can sort products on criteria such as price and category so that I can I have a method of ordering the products products as I prefer
	* I can browse through products so that I can decide what I may be interested in buying
	* I can look at product details to find out more about the product
	* I can easily add products I want to purchase to a basket
	* I can view the contents of my shopping basket so that I can be able to make any adjustments
	* I can update my bag by adding more or remove products so that I can decide on the number of products I intend to buy
	* I can view my order summary so that I can verify it before confirming
	* I can checkout securely so that I can I maintain the level of trust on the site
	* I can use the contact form so that I can contact the site owners
* After logging in:
	* I can add gallery images to my favouries
	* I can save my personal details after making a purchase
	* I can create or edit my account to update my details
	* I can login in my account so that I can view my order history


## Architecture



## Database

#### __Database Plan__

| Key | Name | Type |
| --- | --- | --- |

|  | `Bag` |

| | `Checkout` |
|  | `Order` |  |
| ForeignKey | user_profile | UserProfile |
|  | date | DateTimeField |
|  | order_number | CharField |
|  | delivery_cost | DecimalField |
|  | order_total | DecimalField |
|  | grand_total | DecimalField |
|  | full_name | CharField |
|  | email = | EmailField |
|  | phone_number | CharField |
|  | street_address1 | CharField |
|  | street_address2 | CharField |
|  | city_or_town | CharField |    
|  | postcode = | CharField |
|  | county = | CharField |
|  | country | CountryField |
|  | original_bag | TextField |
|  | stripe_pid | CharField |
|  | `OrderLineItem` |
| ForeignKey | order | Order |
| ForeignKey | prints | Prints |
|  | prints_size | CharField |
|  | quantity | IntegerField |
|  | lineitem_total | DecimalField |
|  | `Profiles` |
|  | `UserProfile` |
| OneToOneField | user | User |
|  | default_email | EmailField |
|  | default_phone_number | CharField |
|  | default_street_address1 | CharField |
|  | default_street_address2 | CharField |
|  | default_city_or_town | CharField |  
|  | default_postcode | CharField |
|  | default_county | CharField |
|  | default_country | CountryField |
|  | `Superuser` |
|  | Username | TextInput |
|  | Email address | TextInput |
|  | Password | TextInput |
| `Projects` |
|  | `Project` |
|  | Name(unique) | TextInput|
|  | Description | TextInput |
|  | Where | TextInput |
|  | When | DateTimeField |
| `Photos` |
| ForeignKey | project | Project |
|  | name | CharField |
|  | friendly_name | CharField |
|  | image_url | URLField |
|  | image | ImageField |
|  | description | TextField |
|  | Name(unique) | TextInput |
|  | Image |  |
| ForeignKey | project_name | Project Model |
| `Shop` |
|  | `Category` |
| ForeignKey | name | Project |
|  | `Prints` |
| ForeignKey | name(unique) | Photo |
| ForeignKey | category |  Category |
|  | sku | CharField |
|  | friendly_name | CharField |
|  | image_url | URLField |
|  | image | ImageField |
|  | description | TextField |
|  | a4_price | DecimalField |
|  | a5_price | DecimalField |
|  | `PriceSelectionForm`|
|  | selected_price | ChoiceField |


## Design

### Color Scheme

I have chosen to keep the webpage mostly white like gallery walls. This is to draw attention to the work and not to distract the user. This was a joint decision with the artist. I chose the dark earthy green for the logo as I felt this would compliment the earthy tones in his landscape pictures.


### Font Choices 

I wanted to contrast a modern font, which I've used for the headings with traditional fonts for the logo and the paragraphs. 

!(logo)[media/docs/logo-font.png]
!(heading)[media/docs/heading-font.png]
!(paragraph)[media/docs/paragraph-font.png]


### Wireframes

<details>
  <summary>Click here to view Wireframes:</summary>
	![home](media/docs/wireframes/home.png)
	![register](media/docs/wireframes/register.png)
	![login](media/docs/wireframes/login.png)
	![profile](media/docs/wireframes/profile.png)
	![about](media/docs/wireframes/about.png)
	![projects](media/docs/wireframes/projects.png)
	![contact](media/docs/wireframes/contact.png)
</details>


## Navigation


  ![]()



# Features
## Homepage

### Header

![header]()

### The home page

![home]()

### Register/Sign up

![register]()

### Sign in


![login]()

### Logout


![logout]()

## Gallery

### Gallery Menu

### View Project

###

## All products


![products]()

 ### Sort by price

 ![logout]()

 ### Sort by project category
 
 ![category]()

 ### Product detail/ add to bag


 ![detail]()

 ![add to bag]()

 ### The shopping bag

![bag]()

### Checkout

![checkout](static/images/checkout.jpg)

![checkout bottom](static/images/checkout2.jpg)

### Checkout success

![order confirm]()

### Order confirmation email

![confirmation email]()

### Product detail- super user


![detail]()

### Product management- add product

![add product]()

### Product management- edit product

![edit]()

### Product management- delete product

![delete]()

### New Arrivals

![arrivals]()

# Footer

![footer]()

## About

![about]()

# My Profile

![profile]()

# 404 page

![error handling]()

### Future features


### Future Implementations

- 
- 
- 

### Accessibility

I used accessability features to make the website accessible for a variety of users. Features include:
- Use of semantic HTML
- Aria-labels on all buttons and links
- All pages of a suitable contrast as advised by WebAIM
- Descriptive alt attributes
- providing aria labels for icons without text

- - -

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python

- - -

### Databases Used

[PostgreSQL](https://www.postgresql.org/) 

[ElephantSQL](https://www.elephantsql.com/) - Database hosting for deployed site

- - -

### Frameworks Used

[Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap4](https://getbootstrap.com/) - A css framework

[Fancybox](https://fancyapps.com/fancybox/) - A JS framework

- - -

### Libraries & Packages Used

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) - Database abstraction library, used to interact with PostgreSQL.

[Font Awesome](https://fontawesome.com/) - Was used to add icons for my social media links.

- - -

### Programs Used

[Heroku](https://www.heroku.com/) - is a cloud platform service  I used to deploy and host the project

[Pip](https://pypi.org/project/pip/) - Tool for installing python packages.

[Stripe](https://stripe.com/en-ie) - was used for checkout functionality and facilitate online payments

[AWS](https://aws.amazon.com/s3/) - for  object storage through a web service interface.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Figma](https://www.figma.com/) - To make flow charts.

[Git](https://git-scm.com/) - For version control.

[Github](https://github.com/) - To save and store the files for the website.

[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

[Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

[Tiny PNG](https://tinypng.com/) To compress images for use in the readme.

[Any webP](https://www.anywebp.com/) To resize images and convert to webP format for the site.

[Favicon.io](https://favicon.io/) To create the favicon.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

### Error Handling

### Defensive Programming

#### User

I have used "@login_required" to prevent users from accessing some pages. This prevents those not logged in from accessing the admin pages.

#### Admin User

I have used if statements in the templates to prevent non-superusers from accessing the admin pages.

I have set up AWS to prevent others from accessing keys and being able to write to the media and static buckets.

# Deployment

### Forking 

### Cloning

## Credits

### Acknowledgement and support
