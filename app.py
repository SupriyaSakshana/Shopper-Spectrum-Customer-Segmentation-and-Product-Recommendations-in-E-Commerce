import streamlit as st
import pandas as pd
import joblib

# ============================
# Load Saved Models
# ============================

kmeans = joblib.load("G:\Supriya\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\customer_segmentation.pkl")
scaler = joblib.load("G:\Supriya\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\scaler.pkl")
similarity_df = pd.read_pickle("G:\Supriya\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\product_similarity.pkl")

# ============================
# Streamlit Page Configuration
# ============================

st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Shopper Spectrum")
st.markdown("### Customer Segmentation & Product Recommendation System")

# ============================
# Sidebar
# ============================

menu = st.sidebar.selectbox(
    "Choose Module",
    ["Product Recommendation", "Customer Segmentation"]
)

# ============================================================
# PRODUCT RECOMMENDATION MODULE
# ============================================================

if menu == "Product Recommendation":

    st.header("📦 Product Recommendation")

    product = st.text_input("Enter Product Name")

    if st.button("Get Recommendations"):

        if product == "":
            st.warning("Please enter a product name.")

        elif product not in similarity_df.index:
            st.error("❌ Product Not Found")

        else:

            recommendations = similarity_df[product]\
                                .sort_values(ascending=False)[1:6]

            st.success("Top 5 Recommended Products")

            for i, item in enumerate(recommendations.index, start=1):
                st.write(f"{i}. {item}")

# ============================================================
# CUSTOMER SEGMENTATION MODULE
# ============================================================

elif menu == "Customer Segmentation":

    st.header("👥 Customer Segmentation")

    recency = st.number_input(
        "Recency (Days)",
        min_value=0,
        value=10
    )

    frequency = st.number_input(
        "Frequency",
        min_value=1,
        value=5
    )

    monetary = st.number_input(
        "Monetary",
        min_value=0.0,
        value=1000.0
    )

    if st.button("Predict Customer Segment"):

        data = scaler.transform(
            [[recency, frequency, monetary]]
        )

        cluster = kmeans.predict(data)[0]

        segment_map = {
            0: "Occasional",
            1: "At-Risk",
            2: "VIP",
            3: "High-Value",
            4: "Champions"
        }

        st.success(
            f"Predicted Segment : {segment_map[cluster]}"
        )

        if segment_map[cluster] == "Champions":
            st.info("🌟 Highest-value customers. Reward with premium offers.")

        elif segment_map[cluster] == "VIP":
            st.info("💎 Loyal customers. Offer exclusive benefits.")

        elif segment_map[cluster] == "High-Value":
            st.info("🎯 Encourage repeat purchases with personalized recommendations.")

        elif segment_map[cluster] == "Occasional":
            st.info("🛍️ Send discounts and promotional campaigns.")

        elif segment_map[cluster] == "At-Risk":
            st.info("⚠️ Launch customer retention campaigns.")