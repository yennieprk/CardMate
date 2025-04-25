from flask import Flask, render_template, request, jsonify, abort, redirect, url_for

app = Flask(__name__)

# Sample dataset of credit cards
credit_cards = [
    {"id": 1, "name": "Chase Sapphire Preferred",
     "issuer": "Chase/Visa",
     "reward_type": "Travel",
     "annual_fee": 95,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "16.99% - 23.99%",
     "image": "https://media.chase.com/content/dam/chase/media-center/pr/card-sapphire-preferred.png",
     "apply_link": "https://creditcards.chase.com/rewards-credit-cards/sapphire/preferred",
     "benefits": ["Earn 60,000 bonus points", "2% points on dining & travel", "No foreign transaction fees"]},

    {"id": 2, "name": "Amex Platinum Card",
     "issuer": "American Express",
     "reward_type": "Luxury Travel",
     "annual_fee": 695,
     "credit_score_required": "Excellent",
     "interest_rate": "See Pay Over Time APR",
     "image": "https://icm.aexp-static.com/acquisition/card-art/NUS000000237_480x304_straight_withname.png",
     "apply_link": "https://www.americanexpress.com/us/credit-cards/card/platinum/",
     "benefits": ["Airport lounge access", "5X points on flights & hotels", "Uber & Saks Fifth Avenue credits"]},

    {"id": 3, "name": "Discover it",
     "issuer": "Discover",
     "reward_type": "Cashback",
     "annual_fee": 0,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "13.99% - 24.99%",
     "image": "https://www.discover.com/content/dam/discover/en_us/credit-cards/card-acquisitions/grey-redesign/global/images/cardart/cardart-cash-it-blue-390-243.png",
     "apply_link": "https://www.discover.com/credit-cards/cash-back/",
     "benefits": ["5% cashback in rotating categories", "1% unlimited cashback", "Friendly to students, great starter card!"]},

         {"id": 4, "name": "Capital One Savor Rewards",
     "issuer": "Capital One",
     "reward_type": "Cashback",
     "annual_fee": 95,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "19.99% - 29.99%",
     "image": "https://ecm.capitalone.com/WCM/card/products/new-savor-card-art/mobile.png",
     "apply_link": "https://www.capitalone.com/credit-cards/savor/",
     "benefits": ["Unlimited 4% cashback on dining, entertainment, and streaming", 
                  "2% cashback at grocery stores", "No foreign transaction fees"]},

    {"id": 5,
    "name": "Chase Ink Business Cash",
    "issuer": "Chase",
    "reward_type": "Cashback",
    "annual_fee": 0,
    "credit_score_required": "Good - Excellent",
    "interest_rate": "16.99% - 27.99%",
    "image": "https://creditcards.chase.com/content/dam/jpmc-marketplace/card-art/ink_cash_card.png",
    "apply_link": "https://creditcards.chase.com/business-credit-cards/ink/cash",
    "benefits": [
        "5% cashback on office supplies and internet, cable & phone services (up to $25,000 annually)",
        "2% cashback on gas stations and restaurants (up to $25,000 annually)",
        "1% unlimited cashback on all other purchases",
        "$750 bonus cash back after spending $6,000 in the first 3 months"]},

    {"id": 6, "name": "Capital One Venture Rewards Credit Card",
     "issuer": "Capital One",
     "reward_type": "Travel",
     "annual_fee": 95,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "20.99% - 28.99%",
     "image": "https://ecm.capitalone.com/WCM/card/products/venture_cardart_prim_323x203-1.png",
     "apply_link": "https://www.capitalone.com/credit-cards/venture/",
     "benefits": ["Earn 2X miles per dollar on every purchase", 
                  "5X miles on hotels and rental cars booked through Capital One Travel",
                  "Global Entry/TSA PreCheck credit"]},

    {"id": 7, "name": "Chase Freedom Unlimited",
     "issuer": "Chase/Visa",
     "reward_type": "Cashback",
     "annual_fee": 0,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "18.99% - 27.99%",
     "image": "https://www.chase.com/content/dam/chase-ux/heroimage/primary/personal/credit-cards/freedom/freedom-unlimited-credit-card.png",
     "apply_link": "https://creditcards.chase.com/cash-back-credit-cards/freedom/unlimited",
     "benefits": ["Unlimited 1.5% cashback on all purchases", 
                  "3% on dining & drugstores", 
                  "5% on travel through Chase Ultimate Rewards"]},

    {"id": 8, "name": "Amex Blue Cash Preferred",
     "issuer": "American Express",
     "reward_type": "Cashback",
     "annual_fee": 95,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "19.99% - 29.99%",
     "image": "https://icm.aexp-static.com/acquisition/card-art/NUS000000264_480x304_straight_withname.png",
     "apply_link": "https://www.americanexpress.com/us/credit-cards/card/blue-cash-preferred/",
     "benefits": ["6% cashback on groceries (up to $6,000 annually)", 
                  "6% cashback on select streaming services", 
                  "3% cashback on transit and gas stations"]},

    {"id": 9, "name": "Amex Gold Card",
     "issuer": "American Express",
     "reward_type": "Dining & Travel",
     "annual_fee": 250,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "See Pay Over Time APR",
     "image": "https://cdn.prod.website-files.com/64ee95ef77ace14bdf5a049f/672cf23c0016d96c86f2827c_Amex%20Gold%20Card.png",
     "apply_link": "https://www.americanexpress.com/us/credit-cards/card/gold/",
     "benefits": ["4X Membership Rewards points at restaurants & U.S. supermarkets",
                  "3X points on flights booked directly with airlines",
                  "$120 Uber Cash & $120 dining credit annually"]},

    {"id": 10, "name": "Citi Double Cash Card",
     "issuer": "Citi/Mastercard",
     "reward_type": "Cashback",
     "annual_fee": 0,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "18.49% - 28.49%",
     "image": "https://www.citi.com/CRD/images/citi-double-cash/citi-double-cash_222x140.png",
     "apply_link": "https://www.citi.com/credit-cards/citi-double-cash-credit-card",
     "benefits": ["Earn 2% cashback on all purchases (1% when you buy, 1% when you pay)", 
                  "No caps or category restrictions",
                  "0% intro APR on balance transfers for 18 months"]},

    {"id": 11, "name": "Wells Fargo Active Cash Card",
     "issuer": "Wells Fargo",
     "reward_type": "Cashback",
     "annual_fee": 0,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "18.99% - 29.99%",
     "image": "https://creditcards.wellsfargo.com/W-Card-MarketPlace/v2-19-25/images/Products/ActiveCash/WF_ActiveCash_VS_Collateral_Front_RGB.png",
     "apply_link": "https://www.wellsfargo.com/credit-cards/active-cash/",
     "benefits": ["Earn unlimited 2% cashback on purchases",
                  "$200 welcome bonus after spending $1,000 in first 3 months",
                  "0% intro APR for 15 months on purchases and balance transfers"]},

    {"id": 12, "name": "Amex Blue Cash Everyday Card",
     "issuer": "American Express",
     "reward_type": "Cashback",
     "annual_fee": 0,
     "credit_score_required": "Good - Excellent",
     "interest_rate": "18.99% - 28.99%",
     "image": "https://icm.aexp-static.com/acquisition/card-art/NUS000000305_480x304_straight_withname.png",
     "apply_link": "https://www.americanexpress.com/us/credit-cards/card/blue-cash-everyday/",
     "benefits": ["3% cashback at U.S. supermarkets (up to $6,000 annually)", 
                  "3% cashback on U.S. online retail purchases", 
                  "3% cashback on gas stations"]},
]
current_id = len(credit_cards) + 1

# 🔹 Homepage Route - Display Top 6 Credit Cards
@app.route("/")
def homepage():
    # Select top 6 cards for featured section
    featured_cards = [
        card for card in credit_cards 
        if card["id"] in [1, 2, 3, 9, 10, 11]  # Chase Sapphire, Amex Platinum, Discover it, Amex Gold, Citi Double Cash, Wells Fargo Active Cash
    ]
    # Pass both featured cards and all cards (for comparison dropdown)
    return render_template("index.html", featured_cards=featured_cards, credit_cards=credit_cards)

# 🔹 Search Route
@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    if query:
        for card in credit_cards:
            # Search in name, issuer, and reward_type (case insensitive)
            if (query in card["name"].lower() or 
                query in card["issuer"].lower() or 
                query in card["reward_type"].lower()):
                results.append(card)
    
    return render_template(
        "search.html",
        results=results,
        query=query,
        result_count=len(results)
    )

# 🔹 Add New Credit Card Page - GET route
@app.route("/add", methods=["GET"])
def add_card_page():
    return render_template("add.html")

# 🔹 Add New Credit Card - POST route
@app.route("/add", methods=["POST"])
def add_card():
    global current_id

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    # Validate all required fields
    required_fields = ["name", "issuer", "reward_type", "annual_fee", "credit_score_required", "interest_rate", "image", "apply_link", "benefits"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"}), 400

    try:
        data["annual_fee"] = int(data["annual_fee"])
    except ValueError:
        return jsonify({"error": "Annual Fee must be a number"}), 400

    new_card = {
        "id": current_id,
        "name": data["name"],
        "issuer": data["issuer"],
        "reward_type": data["reward_type"],
        "annual_fee": data["annual_fee"],
        "credit_score_required": data["credit_score_required"],
        "interest_rate": data["interest_rate"],
        "image": data["image"],
        "apply_link": data["apply_link"],
        "benefits": [b.strip() for b in data["benefits"].split("\n")]  # Handle multi-line benefits properly
    }

    credit_cards.append(new_card)
    current_id += 1

    return jsonify({"message": "New item successfully created", "card": new_card})

# 🔹 Edit Credit Card Page - GET route
@app.route("/edit/<int:card_id>", methods=["GET"])
def edit_card_page(card_id):
    card = next((card for card in credit_cards if card["id"] == card_id), None)
    if not card:
        abort(404)
    return render_template("edit.html", card=card)

# 🔹 Edit Credit Card - POST route
@app.route("/edit/<int:card_id>", methods=["POST"])
def edit_card(card_id):
    card = next((card for card in credit_cards if card["id"] == card_id), None)
    if not card:
        return jsonify({"error": "Credit Card not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    # Validate required fields
    required_fields = ["name", "issuer", "reward_type", "annual_fee", "credit_score_required", "interest_rate", "image", "apply_link", "benefits"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"}), 400

    try:
        data["annual_fee"] = int(data["annual_fee"])
        if data["annual_fee"] < 0:
            return jsonify({"error": "Annual Fee must be a positive number"}), 400
    except ValueError:
        return jsonify({"error": "Annual Fee must be a number"}), 400

    # Update the card
    card.update({
        "name": data["name"].strip(),
        "issuer": data["issuer"].strip(),
        "reward_type": data["reward_type"].strip(),
        "annual_fee": data["annual_fee"],
        "credit_score_required": data["credit_score_required"].strip(),
        "interest_rate": data["interest_rate"].strip(),
        "image": data["image"].strip(),
        "apply_link": data["apply_link"].strip(),
        "benefits": [b.strip() for b in data["benefits"].split("\n") if b.strip()]
    })

    return jsonify({"message": "Card successfully updated", "card": card})

@app.route("/view/<int:card_id>")
def view_card(card_id):
    print(f"Trying to load card with ID: {card_id}")
    card = next((card for card in credit_cards if card["id"] == card_id), None)
    if not card:
        print("Card not found!")
        return "Credit Card not found", 404
    
    # Find similar cards (same reward type, excluding current card)
    similar_cards = [
        c for c in credit_cards 
        if c["reward_type"] == card["reward_type"] and c["id"] != card["id"]
    ]
    
    # Sort similar cards by annual fee to show most relevant first
    similar_cards.sort(key=lambda x: abs(x["annual_fee"] - card["annual_fee"]))
    
    # Limit to top 3 similar cards
    similar_cards = similar_cards[:3]
    
    return render_template("view.html", card=card, similar_cards=similar_cards)

# 🔹 Delete Credit Card Route
@app.route("/delete/<int:card_id>", methods=["POST"])
def delete_card(card_id):
    global credit_cards
    card = next((card for card in credit_cards if card["id"] == card_id), None)
    if not card:
        return jsonify({"error": "Credit Card not found"}), 404
    
    credit_cards = [c for c in credit_cards if c["id"] != card_id]
    return jsonify({"message": "Card successfully deleted"})

@app.route("/compare/<int:card1_id>/<int:card2_id>")
def compare_cards(card1_id, card2_id):
    card1 = next((card for card in credit_cards if card["id"] == card1_id), None)
    card2 = next((card for card in credit_cards if card["id"] == card2_id), None)
    
    if not card1 or not card2:
        return "One or both cards not found", 404
        
    return render_template("compare.html", card1=card1, card2=card2)

if __name__ == "__main__":
    app.run(debug=True, port=5001)