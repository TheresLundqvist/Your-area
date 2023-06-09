# Testing

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2F) | ![screenshot](documentation/html-validation.png) | Pass: No error |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/html-validation-products.png) | Pass: No error |
| Gallery | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Fgallery%2F) | ![screenshot](documentation/html-validation-gallery.png) | Pass: No Errors |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/html-validation-about.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/html-validation-contact.png) | Pass: No Errors |
| Newsletter | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Fnewsletter%2F) | ![screenshot](documentation/html-validation-newsletter.png) | Pass: No Errors |
| FAQ | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Ffaqs%2F) | ![screenshot](documentation/html-validation-faqs.png) | Pass: No Errors |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/html-validation-register.png) | Pass: No Errors |
| Log in | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/html-validation-login.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fyour-area.herokuapp.com%2Fbag%2F) | ![screenshot](documentation/html-validation-bag.png) | Pass: No Errors |
| Product Management | W3C | ![screenshot](documentation/html-validation-addproduct.png) | 2 Errors due to the widget on the form |
| Profile | W3C | ![screenshot](documentation/html-validation-profile.png) | Pass: No Errors |
| Checkout Success | W3C | ![screenshot](documentation/html-validation-checkoutsuccess.png) | Pass: No Error |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css, profile.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fyour-area.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) | ![screenshot](documentation/css-validation-style.png) | Pass: No Errors or warnings for custom CSS |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/jshint-stripe-elements.png) | Pass: No Errors, igonore Stripe variable warning |
| countryfield.js | ![screenshot](documentation/jhint-countryfield.png) | Pass: No Errors |

### Python Validation - Pycodestyle

Python testing was done using Pycodestyle to ensure there were no syntax errors.

The only errors displayed (as per below screenshot) is due to auto generated migration files with lines to long. These files can be ignored.

| File | Screenshot | Notes |
| --- | --- | --- |
| All *py files | ![screenshot](documentation/pep8-validation.png) | Pass: No errors (except auto-generated migrations) |

I have also used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| App | File | CI PEP8 URL |
| --- | --- | --- |
| about | | |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/about/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/about/views.py) |
| bag | | |
| | contexts | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/bag/contexts.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/bag/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/bag/views.py) |
| checkout | | |
| | admin | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/admin.py) |
| | forms | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/forms.py) |
| | models | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/models.py) |
| | signals | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/signals.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/views.py) |
| | webhook_handler | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/webhook_handler.py) |
| | webhooks | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/checkout/webhooks.py) |
| contact | | |
| | admin | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/contact/admin.py) |
| | forms | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/contact/forms.py) |
| | models | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/contact/models.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/contact/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/contact/views.py) |
| faqs | | |
| | admin | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/faqs/admin.py) |
| | models | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/faqs/models.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/faqs/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/faqs/views.py) |
| gallery | | |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/gallery/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/gallery/views.py) |
| home | | |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/home/urls.py) |
| newsletter | | |
| | admin | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/newsletter/admin.py) |
| | forms | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/newsletter/forms.py) |
| | models | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/newsletter/models.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/newsletter/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/newsletter/views.py) |
| products | | |
| | admin | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/products/admin.py) |
| | forms | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/products/forms.py) |
| | models | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/products/models.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/products/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/products/views.py) |
| | widgets | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/products/widgets.py) |
| profiles | | |
| | forms | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/profiles/forms.py) |
| | models | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/profiles/models.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/profiles/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/profiles/views.py) |
| your_area_store | | |
| | settings | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/your_area_store/settings.py) |
| | urls | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/your_area_store/urls.py) |
| | views | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/your_area_store/views.py) |
| root-level | | |
| | manage.py | [URL](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TheresLundqvist/Your-area/main/manage.py) |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-browser.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-browser.png) | Works as expected |
| Edge | ![screenshot](documentation/edge-browser.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/mobile-responsive-devtools.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/ipad-mini-responsive-devtools.png) | Works as expected |
| Desktop | ![screenshot](documentation/desktop-responsive.png) | Works as expected |
| Huawei P30 (Manual test) | ![screenshot](documentation/mobile-responsive.png.jpg) | Added some margin-right to bag icon due to some x-overflow. |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/home-mobile-lighthouse.png) | Slow Performance |
| Home | Desktop | ![screenshot](documentation/home-desktop-lighthouse.png) |  |
| Products | Mobile | ![screenshot](documentation/products-mobile-lighthouse.png) | Bad Performance |
| Products | Desktop | ![screenshot](documentation/products-desktop-lighthouse.png) | Slow Performance |
| Gallery | Mobile | ![screenshot](documentation/gallery-mobile-lighthouse.png) | Slow Performance |
| Gallery | Desktop | ![screenshot](documentation/gallery-desktop-lighthouse.png) | Slow Performance |
| About | Mobile | ![screenshot](documentation/about-mobile-lighthouse.png) | Slow Performance |
| About | Desktop | ![screenshot](documentation/about-desktop-lighthouse.png) |  |
| Contact | Mobile | ![screenshot](documentation/contact-mobile-lighthouse.png) | Slow Performance |
| Contact | Desktop | ![screenshot](documentation/contact-desktop-lighthouse.png) |  |
| Newsletter | Mobile | ![screenshot](documentation/newsletter-mobile-lighthouse.png) | Slow Performance |
| Newsletter | Desktop | ![screenshot](documentation/newsletter-desktop-lighthouse.png) |  |
| FAQ | Mobile | ![screenshot](documentation/faqs-mobile-lighthouse.png) | Slow Performance |
| FAQ | Desktop | ![screenshot](documentation/faqs-desktop-lighthouse.png) |  |
| Bag | Mobile | ![screenshot](documentation/bag-mobile-lighthouse.png) | Slow Performance |
| Bag | Desktop | ![screenshot](documentation/bag-desktop-lighthouse.png) |  |
| Checkout | Mobile | ![screenshot](documentation/checkout-mobile-lighthouse.png) | Slow Performance |
| Checkout | Desktop | ![screenshot](documentation/checkout-desktop-lighthouse.png) | Slow Performance |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Searchbar in navigation | Performs search | Pass | |
| | Try to perform a blank search | Throws error message | Pass | |
| | Click on bag icon | Redirection to shopping bag | Pass | |
| | Click on shop now button | Redirection to products page | Pass | |
| | Click on View Inspiration Gallery | Redirection to Gallery page | Pass | |
| | Click on Contact in dropdown 'about' menu | Redirection to Contact page | Pass | |
| | Click on About in dropdown 'about' menu | Redirection to About page | Pass | |
| | Click on FAQ in dropdown 'about' menu | Redirection to FAQ page | Pass | |
| | Click on Newsletter in dropdown 'about' menu | Redirection to Newsletter page | Pass | |
| | Click on Product Management in 'user' menu | Redirection to add products page | Pass | |
| | Try to access Product Management via URL as a guest| Redirects to sign in page | Pass | |
| | Click on Profile in 'user' menu | Redirection to profile page | Pass | |
| | Try to access Profile via URL as a guest| Redirects to sign in page | Pass | |
| | Click on Register in 'user' menu | Redirection to sign in page | Pass | |
| | Click on Login in 'user' menu | Redirection to login page | Pass | |
| | Click on Logout in 'user' menu | Redirection to sign out page | Pass | |
| Products Page | | | | |
| | Click on Product image | Redirection to Products details page | Pass | |
| | Click on Edit link | Redirection to Edit Product page | Pass | |
| | Click on Delete link | Deletes products | Pass | |
| Product Details Page | | | | |
| | Click on Add to bag button | Add product to bag | Pass | |
| | Try to enter -1 or +99 with buttons | -/+ button disabled | Pass | |
| | Try to manually type and add -1 or +99 | Throws error message | Pass | |
| | Click on Keep shopping button | Redirects to product page | Pass | |
| | Click on Edit link | Redirection to Edit Product page | Pass | |
| | Click on Delete link | Deletes products | Pass | |
| | Try to Edit product via URL as a guest| Shows 404 page | Pass | |
| | Try to Delete product via URL as a guest| Shows 404 page  | Pass | |
| Contact Page | | | | |
| | Try to submit form with all fields blank | Throws error message | Pass | |
| | Try to submit form with invalid email format | Throws error message | Pass | |
| | Try to submit form with various blank fields | Throws error message | Pass | |
| Newsletter Page | | | | |
| | Try to submit form with blank field | Throws error message | Pass | |
| | Try to submit form with invalid email format | Throws error message | Pass | |
| Checkout Page | | | | |
| | Try to submit form with all fields blank | Throws error message | Pass | |
| | Try to submit form with invalid email format | Throws error message | Pass | |
| | Try to submit form with various blank fields | Throws error message | Pass | |
| | Try to access checkout page with empty bag | Throws error and redirects to products page | Pass | |
| | Press on 'Complete order' | Send order confirmation email | Pass | |
| Invalid URL | | | | |
| | Try to access invalid URL page | Redirects to 404 page | Pass | |
| Sign in page | | | | |
| | Try to submit form with invalid username | Throws error message | Pass | |
| | Try to submit form with blank fields | Throws error message | Pass | |
| | Try to access login page when already logged in | Redirects to home page | Pass | |
| | Click on home button | Redirects to home page | Pass | |
| | Click on Sign in button | Redirects to home page and shows success message | Pass | |
| Sign out page | | | | |
| | Try to access logout page when already logged out | Redirects to home page | Pass | |
| Sign up page | | | | |
| | Try to submit form with invalid username | Throws error message | Pass | |
| | Try to submit form with blank fields | Throws error message | Pass | |
| | Try to submit form with invalid email field | Throws error message | Pass | |
| | Click on sign in link | Redirects to login page | Pass | |
| | Click on sign up after filling in form | Send verification email | Pass | |
| Product Management page | | | | |
| | Try to submit form marked with * blank | Throws error message | Pass | |
| | Try to submit form with excessive price | Throws error message | Fail | Pass: Add a max value of 99999 to product model price|
| Profile page | | | | |
| | Try to submit form with all fields blank | Updates form to blank | Pass | |
| | Click on update information button | Updates information and shows success message | Pass | |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a store owner I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents. | ![screenshot](documentation/edit-delete-superuser.png) |
| As a Site user I can sign up for the website's newsletter so that I can keep up to date with new products and promotions. | ![screenshot](documentation/newsletter-userstory.png) |
| - As a Site user I can immediately understand the purpose of the site so that I can decide if it meets my needs.| ![screenshot](documentation/site-purpose.png) |
| As a Site user I can sort all products so that I can view products based on price or title. | ![screenshot](documentation/sort.png) |
| As a Site user I can search all products so that I can find what I am looking for. | ![screenshot](documentation/searchbar.png) |
| As a Site user I can click on a product so that I can read the full product details. | ![screenshot](documentation/product-detail-userstory.png) |
| As a Site user I can view a list of products so that I can select a product to view. | ![screenshot](documentation/list-products.png) |
| As a Site user I can intuitively navigate around the site so that find content. | ![screenshot](documentation/header.png) |
| As a Site user I can recover my password in case I forget it so that I can regain access to my account. | ![screenshot](documentation/reset-password.png) |
| As a Site user I can save my personal details in my user profile so that I do not have to fill them out for future orders. | ![screenshot](documentation/delivery-info.png) |
| As a Site user I can view my order history so that I can remember what purchases I've made | ![screenshot](documentation/order-history.png) |
| As a Site user I can see my login status so that I know if I'm logged in or out. | ![screenshot](documentation/logged-in-user.png) ![screenshot](documentation/logged-out-user.png) |
| As a Site user I can register a account so that I can have a personal account. | ![screenshot](documentation/sign-up.png) |
| As a Site User I can log in and out of my account so that I can keep my account secure. | ![screenshot](documentation/logged-in-user.png) ![screenshot](documentation/logged-out-user.png) |
| As a Site user I can view and recieve a order confirmation after checkout so that I know my purchase was successful. | ![screenshot](documentation/order-confirm-page.png) |
| As a Site user I can checkout as a guest so that I don't have to sign up for an account. | ![screenshot](documentation/checkout.png) |
| As a Site user I can view a the contents of my shopping cart at any time so that I can see what is included and the total cost. | ![screenshot](documentation/shopping-bag.png) |
| As a Site user I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues. | ![screenshot](documentation/stripe-payments.png) |
| As a Site user I can adjust the quantity of individual products in my cart so that I can easily make changes before I purchase. | ![screenshot](documentation/update-remove.png) |
| As a Site user I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing. | ![screenshot](documentation/checkout.png) |
| As a Site user, I can view a running total of my shopping cart as I am shopping so that I can see how much it costs in total. | ![screenshot](documentation/bag-toast.png) |
| As a Site user I can add several products in different quantities to my shopping cart so that I can purchase them all together when I am ready.| ![screenshot](documentation/multiple-items.png) |
| As a Site user I can save my personal details in my user profile so that I don't have to fill them out for future orders. | ![screenshot](documentation/prefilled-details.png) |
| As a Site user I can view my order history so that I can keep track of my orders. | ![screenshot](documentation/order-history.png) |
| As a Site user I can view a specific category of products so that I can browse the type of products I'm looking for. | ![screenshot](documentation/shop-products.png) |

## Bugs

| Bug | Status | Comment |
| --- | --- | --- |
| Footer and about section stacked on top of main image in deployed version | Resolved | Deployed again and issue resolved |
| Overflow-X | Resolved | Forgot `container-fluid` Bootstrap class on a section |

## Close Issues/User Stories

All previously closed Issues/User Stories issues can be found [here](https://github.com/TheresLundqvist/Your-area/issues?q=is%3Aissue+is%3Aclosed).

| Issue | Label |
| --- | --- |
| [USER STORY: Log in and out](https://github.com/TheresLundqvist/Your-area/issues/1) | Must Have |
| [USER STORY: Register account](https://github.com/TheresLundqvist/Your-area/issues/4) | Must Have |
| [USER STORY: Site navigation](https://github.com/TheresLundqvist/Your-area/issues/5) | Must Have |
| [USER STORY: Product list view](https://github.com/TheresLundqvist/Your-area/issues/6) | Must Have |
| [USER STORY: Product details](https://github.com/TheresLundqvist/Your-area/issues/7) | Must Have |
| [USER STORY: Product category](https://github.com/TheresLundqvist/Your-area/issues/8) | Should Have |
| [USER STORY: Search products](https://github.com/TheresLundqvist/Your-area/issues/9) | Could Have |
| [USER STORY: Sort products](https://github.com/TheresLundqvist/Your-area/issues/10) | Should Have |
| [USER STORY: Login status](https://github.com/TheresLundqvist/Your-area/issues/12) | Should Have |
| [USER STORY: Order history](https://github.com/TheresLundqvist/Your-area/issues/13) | Should Have |
| [USER STORY: Prefilled personal details](https://github.com/TheresLundqvist/Your-area/issues/14) | Could Have |
| [USER STORY: View order history](https://github.com/TheresLundqvist/Your-area/issues/15) | Could Have |
| [USER STORY: Save personal details in user profile](https://github.com/TheresLundqvist/Your-area/issues/16) | Could Have |
| [USER STORY: Password reset](https://github.com/TheresLundqvist/Your-area/issues/17) | Must Have |
| [USER STORY: Add products to shopping cart](https://github.com/TheresLundqvist/Your-area/issues/18) | Must Have |
| [USER STORY: Shopping cart running total](https://github.com/TheresLundqvist/Your-area/issues/19) | Should Have |
| [USER STORY: Cart summery](https://github.com/TheresLundqvist/Your-area/issues/20) | Must Have |
| [USER STORY: Adjust product quantity](https://github.com/TheresLundqvist/Your-area/issues/21) | Should Have |
| [USER STORY: Payment details](https://github.com/TheresLundqvist/Your-area/issues/22) | Must Have |
| [USER STORY: View shopping cart](https://github.com/TheresLundqvist/Your-area/issues/23) | Must Have |
| [USER STORY: Guest checkout](https://github.com/TheresLundqvist/Your-area/issues/24) | Must Have |
| [USER STORY: Order confirmation](https://github.com/TheresLundqvist/Your-area/issues/25) | Must Have |
| [USER STORY: Product management](https://github.com/TheresLundqvist/Your-area/issues/26) | Must Have |
| [USER STORY: Newsletter signup](https://github.com/TheresLundqvist/Your-area/issues/28) | Could Have |
| [USER STORY: Site declaration](https://github.com/TheresLundqvist/Your-area/issues/31) | Should Have |

## Open Issues/User Stories

Any remaining open Issues/User Stories issues can be tracked [here](https://github.com/TheresLundqvist/Your-area/issues).

| Issue | Label |
| --- | --- |
| [USER STORY: Product review](https://github.com/TheresLundqvist/Your-area/issues/30) | Could Have |
| [USER STORY: Approve user comments](https://github.com/TheresLundqvist/Your-area/issues/29) | Could Have |
| [USER STORY: Save product for later](https://github.com/TheresLundqvist/Your-area/issues/27) | Won't Have |

## Unfixed Bugs

There are no remaining bugs that I am aware of.
