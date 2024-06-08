import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

df = pd.read_csv("Alpha_new.csv")

st.title('Sigma Project EDA Dashboard')
st.write("""
### Trend Analysis
""")

Plot_Name = st.sidebar.selectbox("Select Trend Analysis Method" , ("Popular Product Categories" ,"Number of Sellers by Region", "Product Condition Distribution" , "Popular Brands" , "Product Pricing Distribution" , "Product Gender Target Distribution" , "Product Likes vs. Price" , "Geographical Distribution of Sellers")) 
st.write(Plot_Name)

def plot_product_likes_vs_price():
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x=df['product_like_count'], y=df['price_usd'], ax=ax)
    ax.set_title('Product Likes vs. Price')
    ax.set_xlabel('Product Likes')
    ax.set_ylabel('Price (USD)')
    st.pyplot(fig) 

def plot_product_likes_vs_price():
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x=df['product_like_count'], y=df['price_usd'], ax=ax)
    ax.set_title('Product Likes vs. Price')
    ax.set_xlabel('Product Likes')
    ax.set_ylabel('Price (USD)')
    st.pyplot(fig)

def plot_gender_target_distribution():
    fig, ax = plt.subplots(figsize=(12, 6))
    gender_target_counts = df['product_gender_target'].value_counts()
    sns.barplot(x=gender_target_counts.index, y=gender_target_counts.values, ax=ax)
    ax.set_title('Product Gender Target Distribution')
    ax.set_xlabel('Gender Target')
    ax.set_ylabel('Count')
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

def plot_geographical_distribution_of_sellers():
    # Define country to region mapping
    country_to_region = {
        'USA': 'North America',
        'Canada': 'North America',
        'Mexico': 'North America',
        'Brazil': 'South America',
        'Argentina': 'South America',
        'Germany': 'Europe',
        'France': 'Europe',
        'China': 'Asia',
        'Japan': 'Asia',
        'Australia': 'Oceania',
    }
    
    # Apply the mapping to create a new column for regions
    df['seller_region'] = df['seller_country'].map(country_to_region)
    
    # Drop rows where region is not mapped
    df_clean = df.dropna(subset=['seller_region'])
    
    # Load geographical data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    # Count the number of sellers in each country
    country_counts = df_clean['seller_country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    
    # Merge with world data
    world = world.merge(country_counts, how='left', left_on='name', right_on='country')
    
    # Plot the geographical distribution of sellers
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax)
    world.plot(column='count', ax=ax, legend=True,
               legend_kwds={'label': "Number of Sellers by Country",
                            'orientation': "horizontal"},
               missing_kwds={"color": "lightgrey"})
    
    ax.set_title('Geographical Distribution of Sellers')
    st.pyplot(fig)

def plot_number_of_sellers_by_region():
    # Define country to region mapping
    country_to_region = {
        'USA': 'North America',
        'Canada': 'North America',
        'Mexico': 'North America',
        'Brazil': 'South America',
        'Argentina': 'South America',
        'Germany': 'Europe',
        'France': 'Europe',
        'China': 'Asia',
        'Japan': 'Asia',
        'Australia': 'Oceania',
    }
    
    # Apply the mapping to create a new column for regions
    df['seller_region'] = df['seller_country'].map(country_to_region)
    
    # Drop rows where region is not mapped
    df_clean = df.dropna(subset=['seller_region'])
    
    # Count the number of sellers in each region
    region_counts = df_clean['seller_region'].value_counts()
    
    # Plot regional counts
    fig, ax = plt.subplots(figsize=(12, 6))
    region_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of Sellers by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Number of Sellers')
    st.pyplot(fig)

def plot_product_pricing_distribution():
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df['price_usd'], bins=50, kde=True, ax=ax)
    ax.set_title('Product Pricing Distribution (Without Outliers)')
    ax.set_xlabel('Price (USD)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

def plot_popular_brands():
    fig, ax = plt.subplots(figsize=(12, 6))
    brand_counts = df['brand_name'].value_counts().head(10)
    sns.barplot(x=brand_counts.index, y=brand_counts.values, ax=ax)
    ax.set_title('Popular Brands')
    ax.set_xlabel('Brand Name')
    ax.set_ylabel('Count')
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

def plot_product_condition_distribution():
    fig, ax = plt.subplots(figsize=(12, 6))
    product_condition_counts = df['product_condition'].value_counts()
    sns.barplot(x=product_condition_counts.index, y=product_condition_counts.values, ax=ax)
    ax.set_title('Product Condition Distribution')
    ax.set_xlabel('Product Condition')
    ax.set_ylabel('Count')
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

def plot_popular_product_categories():
    fig, ax = plt.subplots(figsize=(12, 6))
    product_category_counts = df['product_category'].value_counts()
    sns.barplot(x=product_category_counts.index, y=product_category_counts.values, ax=ax)
    ax.set_title('Popular Product Categories')
    ax.set_xlabel('Product Category')
    ax.set_ylabel('Count')
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

plot_dict = {
    "Popular Product Categories": plot_popular_product_categories,
    "Product Condition Distribution": plot_product_condition_distribution,
    "Popular Brands": plot_popular_brands,
    "Product Pricing Distribution": plot_product_pricing_distribution,
    "Product Gender Target Distribution": plot_gender_target_distribution,
    "Number of Sellers by Region": plot_number_of_sellers_by_region,
    "Product Likes vs. Price": plot_product_likes_vs_price,
    "Geographical Distribution of Sellers": plot_geographical_distribution_of_sellers,
}

if Plot_Name:
    plot_dict[Plot_Name]()