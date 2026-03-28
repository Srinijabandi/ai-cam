import streamlit as st

st.set_page_config(page_title="Sri Bhama", layout="wide")

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>
body {
    background-color: #f8f4f0;
}
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #6b2d2d;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #8b5e3c;
    margin-bottom: 20px;
}
.card {
    padding: 15px;
    border-radius: 15px;
    background-color: #fffaf5;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.price {
    color: green;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown('<div class="title">🌸✨ Sri Bhama ✨🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Where Tradition Meets Grace 💫</div>', unsafe_allow_html=True)

# Traditional painting banner
st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Rajasthani_miniature_painting.jpg", use_container_width=True)

# Decorative stickers
st.markdown("<center>🪔 🌺 🧵 👗 🌼 🪷</center>", unsafe_allow_html=True)

# ---------------------- PRODUCTS ----------------------
products = [
    {
        "name": "Silk Saree",
        "price": "₹4,999",
        "rating": 4.8,
        "desc": "Handwoven silk saree with traditional motifs.",
        "img": "https://images.unsplash.com/photo-1610030469983-98e550d6193c"
    },
    {
        "name": "Designer Lehenga",
        "price": "₹8,999",
        "rating": 4.7,
        "desc": "Elegant bridal lehenga with embroidery.",
        "img": "https://images.unsplash.com/photo-1603252109303-2751441dd157"
    },
    {
        "name": "Kurta Set",
        "price": "₹2,499",
        "rating": 4.5,
        "desc": "Comfortable festive kurta set.",
        "img": "https://images.unsplash.com/photo-1593032465171-8b35d7f3a2c7"
    },
    {
        "name": "Anarkali Dress",
        "price": "₹3,999",
        "rating": 4.6,
        "desc": "Flowy anarkali with ethnic prints.",
        "img": "https://images.unsplash.com/photo-1623609163859-ca93c959b8d5"
    }
]

st.markdown("---")
st.subheader("🛍️ Collection")

cols = st.columns(2)

cart = st.session_state.get("cart", [])

for i, product in enumerate(products):
    with cols[i % 2]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(product["img"], use_container_width=True)
        st.subheader(product["name"])
        st.write(product["desc"])
        st.markdown(f'<div class="price">{product["price"]}</div>', unsafe_allow_html=True)
        st.write(f"⭐ Rating: {product['rating']}")
        
        if st.button(f"Add to Cart - {product['name']}"):
            cart.append(product)
            st.session_state.cart = cart
            st.success("Added to cart! 🛒")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- CART ----------------------
st.markdown("---")
st.subheader("🛒 Your Cart")

if "cart" in st.session_state and st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"{item['name']} - {item['price']}")
        total += int(item['price'].replace("₹", "").replace(",", ""))

    st.write(f"**Total: ₹{total}**")

    if st.button("Proceed to Buy"):
        st.success("Order placed successfully! 🎉")
        st.session_state.cart = []
else:
    st.write("Cart is empty")

# ---------------------- REVIEWS ----------------------
st.markdown("---")
st.subheader("💬 Customer Reviews")

reviews = [
    "Absolutely loved the saree quality! 😍",
    "Very elegant and traditional designs. 🌸",
    "Worth the price. Fabric is premium. 👌",
    "Perfect for festivals and weddings! 💃"
]

for r in reviews:
    st.write(f"📝 {r}")

# ---------------------- FOOTER ----------------------
st.markdown("---")
st.markdown("<center>© 2026 Sri Bhama | Crafted with Tradition ❤️</center>", unsafe_allow_html=True)
