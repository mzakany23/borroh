var handler = StripeCheckout.configure({
    key: 'pk_test_G0K67FwSKkcdKKLDcwTjrXzy',
    image: '/img/documentation/checkout/marketplace.png',
    token: function(token) {
      // Use the token to create the charge with a server-side script.
      // You can access the token ID with `token.id`
    }
  });

  $('#customButton').on('click', function(e) {
    // Open Checkout with further options
    handler.open({
      name: 'Demo Site',
      description: '2 widgets',
      amount: 2000
    });
    e.preventDefault();
  });

  // Close Checkout on page navigation
  $(window).on('popstate', function() {
    handler.close();
  });