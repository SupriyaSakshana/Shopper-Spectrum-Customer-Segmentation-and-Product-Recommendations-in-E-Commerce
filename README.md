# Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce



<img width="901" height="338" alt="image" src="https://github.com/user-attachments/assets/7b9a15f4-08a8-4805-8049-321fe29c727b" />




Two real business problems for an e-commerce company:

1. Customer Segmentation (Who are our customers?)

Using transaction history, you'll calculate:

Recency (R): How recently a customer purchased.
Frequency (F): How often they purchase.
Monetary (M): How much money they spend.

Then you'll apply clustering (typically K-Means) to group customers into segments such as:

Segment	Meaning
High-Value	Buy recently, frequently, and spend a lot
Regular	Purchase consistently but spend moderately
Occasional	Purchase infrequently
At-Risk	Haven't purchased in a long time
Business Value

A company can:

Give premium offers to High-Value customers.
Encourage Regular customers to spend more.
Re-engage At-Risk customers with discounts.
Avoid spending marketing budget on inactive customers unnecessarily.
2. Product Recommendation System (What should we recommend?)

The project uses Item-Based Collaborative Filtering.

The idea is:

"Customers who bought Product A often also bought Product B."

For example:

Customer	Products Purchased
C1	Laptop, Mouse
C2	Laptop, Keyboard
C3	Laptop, Mouse, Keyboard

The model learns that:

Laptop is similar to Mouse.
Laptop is similar to Keyboard.

So if a user searches for "Laptop", the system might recommend:

Mouse
Keyboard
Laptop Bag
USB Hub
Webcam
Business Value

This helps:

Increase sales through cross-selling.
Improve customer experience.
Increase average order value.
Final Output (Streamlit App)

The app has two independent modules:

Module 1: Product Recommendation

User enters:

WHITE HANGING HEART T-LIGHT HOLDER

Output:

Recommended Products:
1. RED HANGING HEART T-LIGHT HOLDER
2. HEART DECORATION
3. WHITE METAL LANTERN
4. ...
5. ...
Module 2: Customer Segmentation

User enters:

Recency = 10
Frequency = 25
Monetary = 15000

Output:

Segment: High-Value Customer
What interviewers will expect you to explain


"I analyzed e-commerce transaction data, performed RFM analysis to understand customer behavior, and used K-Means clustering to segment customers into business-friendly groups such as High-Value, Regular, Occasional, and At-Risk customers. Additionally, I built an item-based collaborative filtering recommendation system using cosine similarity to recommend products based on historical purchase patterns. Finally, I deployed both functionalities in a Streamlit application for real-time predictions and recommendations."

In short, this project answers two key business questions:

Who are our customers? → Customer Segmentation.
What should we recommend to them? → Product Recommendation System.
