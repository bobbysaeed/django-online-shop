class Cart:
    def __init__(self, request):
        """
            initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']
        self.cart = cart

    def add(self, product, quantity=1):
        """
            Add the specified product to the cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """
            Mark session as modified to save changes
        """
        self.session.modified = True

    def remove(self, product):
        """
        remove product from the cart

        """

        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session['cart']
        self.save()