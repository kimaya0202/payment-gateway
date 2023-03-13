import stripe
from flask import Flask, redirect

app = Flask(__name__,static_url_path="",static_folder="public")

stripe.api_key = "sk_test_51Mf5iMSHP7cyCBSwbnncFvTrRnH4J0rwq5WJQklUaTtMnPK3KOA2v08cRX457eu1GY4nY67Yst9SXegWba4wc11L00b5LLpjmB"

YOUR_DOMAIN = "http://localhost:5000"

@app.route('/create-checkout-session',methods=["POST"])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    "price":"price_1Ml2d7SHP7cyCBSw8UJ4Fvxw",
                    "quantity":1
                }
            ],
            mode="subscription",
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url = YOUR_DOMAIN + "/cancel.html"
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url,code=303)

if __name__ == "__main__":
    app.run(port=5000,debug=True)


