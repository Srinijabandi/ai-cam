import streamlit as st

st.set_page_config(page_title="Sri Bhama", layout="wide")

# ---------------------- CSS ----------------------
st.markdown("""
<style>
body {background-color:#fafafa;}
.navbar {display:flex;justify-content:space-between;padding:10px 20px;background:white;box-shadow:0 2px 5px rgba(0,0,0,0.1);}
.logo {font-size:28px;font-weight:bold;color:#ff3f6c;}
.menu {font-size:16px;color:#333;}
.card {border-radius:12px;background:white;padding:10px;box-shadow:0 2px 10px rgba(0,0,0,0.1);transition:0.3s;}
.card:hover {transform:scale(1.03);}
.price {color:#ff3f6c;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------------------- NAVBAR ----------------------
st.markdown("""
<div class='navbar'>
<div class='logo'>Sri Bhama</div>
<div class='menu'>Home | Categories | Cart | Wishlist</div>
</div>
""", unsafe_allow_html=True)

# ---------------------- DATA ----------------------
products = [
    {"name":"Silk Saree","cat":"Saree","price":4999,"rating":4.8,"img":"https://images.unsplash.com/photo-1610030469983-98e550d6193c"},
    {"name":"Bridal Lehenga","cat":"Lehenga","price":8999,"rating":4.7,"img":"https://images.unsplash.com/photo-1603252109303-2751441dd157"},
    {"name":"Kurta Set","cat":"Kurta","price":2499,"rating":4.5,"img":"https://images.unsplash.com/photo-1593032465171-8b35d7f3a2c7"},
    {"name":"Stylish Top","cat":"Tops","price":1299,"rating":4.3,"img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab"},
    {"name":"Elegant Pants","cat":"Pants","price":1599,"rating":4.2,"img":"https://images.unsplash.com/photo-1584370848010-d7fe6bc767ec"},
    {"name":"Gold Necklace","cat":"Jewellery","price":2999,"rating":4.6,"img":"https://images.unsplash.com/photo-1611599537845-1c4b8c8d3b5f"},
    {"name":"Hand Bag","cat":"Handbags","price":1999,"rating":4.4,"img":"https://images.unsplash.com/photo-1584917865442-de89df76afd3"}
]

# ---------------------- FILTER ----------------------
st.sidebar.title("Filters")
category = st.sidebar.selectbox("Category", ["All","Saree","Lehenga","Kurta","Tops","Pants","Jewellery","Handbags"])
price = st.sidebar.slider("Max Price", 1000, 10000, 10000)

# ---------------------- STATE ----------------------
if "cart" not in st.session_state:
    st.session_state.cart = []
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# ---------------------- FILTER LOGIC ----------------------
filtered = [p for p in products if (category=="All" or p["cat"]==category) and p["price"]<=price]

# ---------------------- PRODUCTS ----------------------
st.subheader("✨ Latest Collection")
cols = st.columns(4)

for i,p in enumerate(filtered):
    with cols[i%4]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(p["img"], use_container_width=True)
        st.write(f"**{p['name']}**")
        st.caption(p["cat"])
        st.markdown(f"<div class='price'>₹{p['price']}</div>", unsafe_allow_html=True)
        st.write(f"⭐ {p['rating']}")

        c1,c2 = st.columns(2)
        if c1.button(f"🛒 {i}"):
            st.session_state.cart.append(p)
        if c2.button(f"❤️ {i}"):
            st.session_state.wishlist.append(p)

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- CART ----------------------
st.markdown("---")
st.subheader("🛒 Cart")

if st.session_state.cart:
    total=sum(x['price'] for x in st.session_state.cart)
    for x in st.session_state.cart:
        st.write(x['name'],"- ₹",x['price'])
    st.write("**Total: ₹",total,"**")
else:
    st.write("Cart is empty")

# ---------------------- WISHLIST ----------------------
st.markdown("---")
st.subheader("❤️ Wishlist")

if st.session_state.wishlist:
    for x in st.session_state.wishlist:
        st.write(x['name'],"- ₹",x['price'])
else:
    st.write("Wishlist is empty")

# ---------------------- FOOTER ----------------------
st.markdown("---")
st.write(" Sri Bhama | Elegant Fashion Store")