#
# Hello everybody I've developed a back-end e-commerce app for learning purposes.
### I am using Render to deploy my project.

When you request any endpoint in the server for the first time and find the website is slow and takes 1 minute to respond because the server shuts itself and there were no requests for the last 15 minutes but after this if you request many times you find the server faster.

#
# Let's know more about my e-commerce app.
### Sign up and Sign in using JWT Authentication.

To sign up for an account:

Link: https://e-commerce-render-platform-app.onrender.com/auth/users/

To sign in account:

Link: https://e-commerce-render-platform-app.onrender.com/auth/jwt/create/

#
### The following endpoints allow any user.

To get collections:

Link: https://e-commerce-render-platform-app.onrender.com/store/collections/

To get a collection you should assign the ID of the collection:

Link: https://e-commerce-render-platform-app.onrender.com/store/collections/{collectionID}/

To get products:

Link: https://e-commerce-render-platform-app.onrender.com/store/products/

To get the product you should assign the ID of the product:

Link: https://e-commerce-render-platform-app.onrender.com/store/products/{productID}/

To post a cart:

Link: https://e-commerce-render-platform-app.onrender.com/store/carts/

To get, and delete a cart you should assign the ID of the cart:

Link: https://e-commerce-render-platform-app.onrender.com/store/carts/{cartID}/

To post a cartItem you should assign the ID of the cart:

Link: https://e-commerce-render-platform-app.onrender.com/store/carts/{cartID}/items/

To get, patch, and delete a cartItem you should assign the ID of the cart and the ID of the card item:

Link: https://e-commerce-render-platform-app.onrender.com/store/carts/{cartID}/items/cardItemID/

#
### The following endpoints require to be an Authenticated user.

To get the current user:

Link: https://e-commerce-render-platform-app.onrender.com/store/customers/me/

To post, update, and delete a product you should assign the ID of the product:

Link: https://e-commerce-render-platform-app.onrender.com/store/products/{productID}/

To get, and post an orders:

Link: https://e-commerce-render-platform-app.onrender.com/store/orders/

#
### The following endpoints require to be an Admin user.

To post, update, and delete a collection you should assign the ID of the collection:

Link: https://e-commerce-render-platform-app.onrender.com/store/collections/{collectionID}/

To get customers:

Link: https://e-commerce-render-platform-app.onrender.com/store/customers/

To get the user you should assign the ID of the customer:

Link: https://e-commerce-render-platform-app.onrender.com/store/customers/{customerID}/

To patch, and delete an order you should assign the ID of the order:

Link: https://e-commerce-render-platform-app.onrender.com/store/orders/{orderID}/

#