def get_response(message):

 msg = message.lower().strip()

# =========================
# GREETING
# =========================
 if any(word in msg for word in [
    "hi", "hello", "hey", "salam", "assalam"
]):
    return (
        "🍽️ Welcome to ZAIQA Restaurant!\n\n"
        "I can help you with:\n"
        "📋 Menu & Prices\n"
        "🚚 Delivery Information\n"
        "🪑 Table Reservations\n"
        "🕒 Opening Hours\n"
        "💳 Payment Methods\n"
        "🎉 Deals & Discounts\n"
        "📦 Order Tracking\n\n"
        "How may I assist you today?"
    )

# =========================
# MENU / FOOD
# =========================
 elif any(word in msg for word in [
    "menu", "food", "dish", "khaana", "item", "items"
]):
    return (
        "📋 ZAIQA MENU\n\n"
        "🍛 Desi Mains\n"
        "Karahi, Nihari, Haleem, Sajji\n"
        "PKR 800 – 2,500\n\n"
        "🔥 Grills & BBQ\n"
        "Seekh Kebab, Chicken Tikka, Malai Boti\n"
        "PKR 600 – 1,800\n\n"
        "🍔 Burgers & Wraps\n"
        "Zaiqa Special Burger, Crispy Wrap, Club Sandwich\n"
        "PKR 400 – 900\n\n"
        "🍚 Rice Dishes\n"
        "Biryani, Pulao, Fried Rice\n"
        "PKR 350 – 1,200\n\n"
        "🎉 Deals & Combos\n"
        "Family Deal, Couple Deal, Student Special\n"
        "PKR 1,200 – 4,500\n\n"
        "🥤 Beverages & Desserts\n"
        "Lassi, Shakes, Zarda, Gulab Jamun\n"
        "PKR 150 – 500"
    )

# =========================
# PRICING
# =========================
 elif any(word in msg for word in [
    "price", "cost", "rate", "kitna", "how much", "pkr", "rupee"
]):
    return (
        "💰 PRICE GUIDE\n\n"
        "🍛 Desi Mains: PKR 800 – 2,500\n"
        "🔥 Grills & BBQ: PKR 600 – 1,800\n"
        "🍔 Burgers & Wraps: PKR 400 – 900\n"
        "🍚 Rice Dishes: PKR 350 – 1,200\n"
        "🎉 Deals & Combos: PKR 1,200 – 4,500\n"
        "🥤 Beverages & Desserts: PKR 150 – 500"
    )

# =========================
# DELIVERY
# =========================
 elif any(word in msg for word in [
    "deliver", "delivery", "ship", "ghar", "home", "area"
]):
    return (
        "🚚 DELIVERY INFORMATION\n\n"
        "📍 Lahore, Karachi & Islamabad:\n"
        "30–45 minutes\n\n"
        "📍 Other Cities:\n"
        "60–90 minutes\n\n"
        "💵 Delivery Charge: PKR 100\n"
        "✅ FREE Delivery on orders above PKR 1,500"
    )

# =========================
# RESERVATION
# =========================
 elif any(word in msg for word in [
    "book", "reserve", "table", "seat", "dine", "reservation"
]):
    return (
        "🪑 TABLE RESERVATIONS\n\n"
        "✅ Tables available for 2–20 guests\n"
        "✅ Book at least 2 hours in advance\n"
        "✅ DM or call to confirm reservation\n"
        "✅ Deposit required for groups above 10 guests"
    )

# =========================
# OPENING HOURS
# =========================
 elif any(word in msg for word in [
    "open", "close", "time", "hours", "kab", "timing"
]):
    return (
        "🕒 OPENING HOURS\n\n"
        "Monday – Thursday\n"
        "12:00 PM – 12:00 AM\n\n"
        "Friday\n"
        "1:00 PM – 1:00 AM\n\n"
        "Saturday – Sunday\n"
        "11:00 AM – 1:00 AM"
    )

# =========================
# PAYMENT
# =========================
 elif any(word in msg for word in [
    "pay", "payment", "jazzcash", "easypaisa",
    "cod", "cash", "card"
]):
    return (
        "💳 PAYMENT METHODS\n\n"
        "✅ JazzCash\n"
        "✅ EasyPaisa\n"
        "✅ Bank Transfer\n"
        "✅ Debit / Credit Card\n"
        "✅ Cash on Delivery (COD)\n\n"
        "COD is available in all major cities."
    )

# =========================
# DEALS
# =========================
 elif any(word in msg for word in [
    "deal", "discount", "offer", "combo",
    "special", "promo"
]):
    return (
        "🎉 SPECIAL DEALS & OFFERS\n\n"
        "🔥 Family Deals\n"
        "🔥 Couple Deals\n"
        "🔥 Student Specials\n\n"
        "Deals are updated every Monday.\n\n"
        "Follow @zaiqaeats and turn on notifications for the latest offers."
    )

# =========================
# ORDER STATUS
# =========================
 elif any(word in msg for word in [
    "order", "track", "status", "where is",
    "kitna time"
]):
    return (
        "📦 ORDER TRACKING\n\n"
        "Please share:\n"
        "• Order ID\n"
        "OR\n"
        "• Registered Phone Number\n\n"
        "Our team will provide the latest order status."
    )

# =========================
# CANCELLATION
# =========================
 elif any(word in msg for word in [
    "cancel", "cancellation", "refund"
]):
    return (
        "❌ ORDER CANCELLATION\n\n"
        "Online orders can be cancelled within 5 minutes of placing the order.\n\n"
        "For urgent changes please call the restaurant directly."
    )

# =========================
# FALLBACK
# =========================
 return (
    "Thank you for contacting ZAIQA Restaurant. 🍽️\n\n"
    "Our team will follow up shortly.\n\n"
    "For updates and offers follow:\n"
    "@zaiqaeats"
)