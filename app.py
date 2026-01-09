import streamlit as st

# ১. দোকানের তথ্য (এখানে আপনার নম্বর দিন)
SHOP_NAME = "My Hardware & Electric Store"
WHATSAPP_NUMBER = "8801XXXXXXXXX" # আপনার সঠিক হোয়াটসঅ্যাপ নম্বর দিন

st.set_page_config(page_title=SHOP_NAME, page_icon="🛠️")
st.title(f"🏠 {SHOP_NAME}")
st.write("পণ্য পছন্দ করে হোয়াটসঅ্যাপে অর্ডার দিন।")

# ২. পণ্যের তালিকা
inventory = {
    "ইলেকট্রিক (Electric)": [
        {"name": "LED Bulb 12W", "price": 150},
        {"name": "Switch Board", "price": 250},
        {"name": "Electric Wire", "price": 1200}
    ],
    "স্যানিটারি (Sanitary)": [
        {"name": "PVC Pipe 4'", "price": 450},
        {"name": "Water Tap", "price": 350}
    ],
    "হার্ডওয়্যার (Hardware)": [
        {"name": "Hammer (হাতুড়ি)", "price": 180},
        {"name": "Door Lock", "price": 850}
    ]
}

category = st.selectbox("ক্যাটাগরি বেছে নিন:", list(inventory.keys()))
order_list = []
total_amount = 0

for item in inventory[category]:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{item['name']}** - {item['price']} টাকা")
    with col2:
        qty = st.number_input("পরিমাণ", min_value=0, step=1, key=item['name'])
    if qty > 0:
        subtotal = qty * item['price']
        total_amount += subtotal
        order_list.append(f"{item['name']} ({qty} টি)")

st.divider()
if order_list:
    st.write(f"### মোট বিল: {total_amount} টাকা")
    if st.button("হোয়াটসঅ্যাপে অর্ডার পাঠান"):
        message = f"অর্ডার লিস্ট:\n" + "\n".join(order_list) + f"\n\nমোট বিল: {total_amount} টাকা"
        wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={message.replace(' ', '%20')}"
        st.markdown(f'<a href="{wa_link}" target="_blank">কনফার্ম করতে এখানে ক্লিক করুন</a>', unsafe_allow_html=True)
