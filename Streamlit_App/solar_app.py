import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import base64
import io 

st.set_page_config(layout="wide")    #use for wide view

# Upload logo
def load_logo(image_path):                   
    icon = Image.open(image_path)
    icon = icon.resize((100, 100)) 
    buffered = io.BytesIO()
    icon.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

img_str = load_logo('images/logo.jpeg')
 
# Adjustment of header 
st.markdown(
    f"""
    <style>
    .header {{                             /*Used for top header*/
        width: 100%;
        background-color: #FFFFFF;  
        padding: 10px;
        display: flex;
        align-items: center;
        position: fixed;
        top: 0;
        border-bottom: 2px solid #000000;
        z-index: 1000;
    }}
    .header-title {{                              /*Used for Title Name*/
        font-size: 35px;
        font-weight: bold;
        color: #333333;
        flex: 0.5;  
        text-align: center;
        margin-top: 40px;
        margin-left: 300px;
        
    }}
    .header-logo {{                               /* logo position and alignment*/
        height: 100px; 
        display: flex;
        align-items: center;
        margin-left: 400px; 
        margin-top: 40px;
    }}
    .header-logo img {{                           /*logo size*/
        height: 100%; 
        width: auto;
    }}
    </style>
    <div class="header">
        <div class="header-title">Solar Power Analysis</div>
        <div class="header-logo">
            <img src="data:image/png;base64,{img_str}" alt="Logo">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Adjust the sidebar width
st.markdown(
    """
    <style>
    /* Adjust the width of the sidebar */
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;  /* Set your desired width here */
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
         magrin-left: -100px;margin-right: 100px; /* Set your desired width here */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the dataset
@st.cache_data
def load_data():
    df1 = pd.read_csv('streamlit_app/plant1_cleaned_data_with_day.csv')
    df2 = pd.read_csv('streamlit_app/plant2_cleaned_data_with_day.csv')
    return df1, df2

df1, df2 = load_data()


# Navigation Section
option_dict = {
    'Options': [],
    'Plant 1': ['Summary Statistics',
                'AC and DC Power by day',
                'Ambient and Module Temperature by Day',
                'Power Production vs. Module Temperature',
                'Daily Power Production Distribution'],

    'Plant 2': ['Summary Statistics of AC and DC Power',
                'Correlation between Ambient and Module Temperature',
                'Temperature Distribution',
                'Temperature Relationship',
                'Power Production vs. Module Temperature',
                'Daily Power Production Distribution'],
    
    'Plant 1 vs Plant 2': ['Power Production vs. Ambient Temperature Comparison',
                           'Temperature Comparison',
                           #'Power Production Distribution Comparison',
                           'Daily Power Production Statistics',
                           'Power Production Efficiency Comparison']

}

st.sidebar.title("Navigation")
select_option = st.sidebar.selectbox("Select a Plant:", option_dict.keys(),index=0)
buttons = option_dict.get(select_option, [])

# Select dataset based on user input
df = df1 if select_option == 'Plant 1' else df2

unique_key = f"radio_{select_option}"
selected_button = st.sidebar.radio('Select an Insight', buttons, key=unique_key,)

# Filter Options
st.sidebar.subheader("Filter Options")

# Filter by day
day_filter = st.sidebar.multiselect(
    "Select Days:",
    options=df['DAY'].unique(),
    default=df['DAY'].unique()[:0]  # Select the first 5 days by default
)

# Filter by module temperature
temp_range = st.sidebar.slider(
    "Select Module Temperature Range:",
    min_value=float(df['MODULE_TEMPERATURE'].min()),
    max_value=float(df['MODULE_TEMPERATURE'].max()),
    value=(float(df['MODULE_TEMPERATURE'].min()), float(df['MODULE_TEMPERATURE'].max())),
    format="%.1f°C"
)


if "show_developer_info" not in st.session_state:
    st.session_state.show_developer_info=False

def toggle_developer_info():
    st.session_state.show_developer_info= not st.session_state.show_developer_info
    
# Function to display the devloper info with a button
st.sidebar.header("")
st.sidebar.header("")
st.sidebar.header("")
# st.sidebar.header("")

#Button for developer option
st.sidebar.button('Developer Info', on_click=toggle_developer_info)


if st.session_state.show_developer_info: 
    # developers information 
    developers = [
    
    {
        "name": "Ankita",
        "photo": "images/ankita.png",
        "student_code": "SC002",
        "linkedin": "https://www.linkedin.com/in/person2/",
        "github": "https://github.com/person2"
    },
    { 
        "name": "Yarlagadda Sreeram",
        "photo": "images/shreeram.png",
        "student_code": "ft37_208",
        "linkedin": "https://www.linkedin.com/in/sreeram-yarlagadda-48a7442ab",
        "github": "https://github.com/Sreeram110"
    },
    {
        "name": "Dhandendra",
        "photo": "images/Dhanendra.png",
        "student_code": "ft37_478",
        "linkedin": "https://www.linkedin.com/in/dhanendra-kumar-thedhanendra/",
        "github": "https://github.com/theDhanendra"
    },
    {
        "name": "Ashish Dabas",
        "photo": "images/ashish.png",
        "student_code": "ft37_855",
        "linkedin": "https://www.linkedin.com/in/ashish-dabas-95b4ab267",
        "github": "https://github.com/AshuSingh96"
    },
    {
        "name": "Arafat Khan",
        "photo": "images/arafat.png",
        "student_code": "ft37_850",
        "linkedin": "https://www.linkedin.com/in/arafat-khan-4644b7314/",
        "github": "https://www.linkedin.com/in/arafat-khan-4644b7314/"
    }
    ]
    # used to create a space between title and header
    st.write("")
    # Display Developer Info Title in main page 
    st.title("Developer Information")
    st.write("")
    
    # Define number of columns per row
    num_columns = 2

    # Create rows of developers
    # Center-align the 5th person
    if len(developers) % num_columns != 0:
        
        cols = st.columns([2, 3, 1])
        with cols[1]:
            dev = developers[-1]
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(dev['photo'],width=140)
            
            with col2:
                st.markdown(
                    '<p style="font-size: 24px; text-decoration: underline;font-weight: bold;">Team Lead</p>',
                    unsafe_allow_html=True)
                st.write(f"**Name**: {dev['name']}")
                st.write(f"**Student Code**: {dev['student_code']}")
                st.write(f"**LinkedIn**:[linkedin]({dev['linkedin']})")
                st.write(f"**GitHub**:[GitHub]({dev['github']})")
        st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line before the last person
    for i in range(0, len(developers) - 1, num_columns):
        row_developers = developers[i:i + num_columns]
        cols = st.columns(num_columns)
        
        for j, dev in enumerate(row_developers):
            with cols[j]:
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(dev['photo'], width=140)
                
                with col2:
                    st.write(f"**Name**: {dev['name']}")
                    st.write(f"**Student Code**: {dev['student_code']}")
                    st.write(f"**LinkedIn**:[linkedin]({dev['linkedin']})")
                    st.write(f"**GitHub**:[GitHub]({dev['github']})")
        
        # Add a horizontal line after each row, but not after the last row
        if (i + num_columns) < (len(developers) - 1):
            st.markdown("<hr>", unsafe_allow_html=True)
    # Center-align the 5th person
    if len(developers) % num_columns != 0:
        st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line before the last person
        cols = st.columns([1, 2, 1])
        with cols[1]:
            dev = developers[-1]
            col1, col2 = st.columns([1, 2])
            
            # with col1:
            #     st.image(dev['photo'], width=100)
            
            # with col2:
            #     st.write(f"**Name**: {dev['name']}")
            #     st.write(f"**Student Code**: {dev['student_code']}")
            #     st.write(f"**LinkedIn**:[linkedin]({dev['linkedin']})")
            #     st.write(f"**GitHub**:[GitHub]({dev['github']})")
        
else:
    if select_option == 'Options':     #used for front page discription
        st.text("")
        st.text("")
        st.markdown("<h1 style='text-align: left; font-size: 36px;'>Solar Power Generation Forecast System</h1>", unsafe_allow_html=True)
    
        #image paths
        image_path_1 = "images/solar_power_bg.jpg"
        image_path_2 = "images/solar power _ds.jpg"
        # open images using PIL
        image1 = Image.open(image_path_1)
        image2 = Image.open(image_path_2)
        fixed_width = 400
        fixed_height = 300

        #resize both images
        image1 = image1.resize((fixed_width, fixed_height))
        image2 = image2.resize((fixed_width, fixed_height))

        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image_path_1, caption="Solar Power Plant", use_column_width=True)
        with col2:
            st.image(image_path_2, caption="Process of Solar Power Genration",use_column_width=True)

        st.write("""The project Solar Power Generation Prediction focuses on analyzing data from two differnt solar power plants.
                The project aims to address key concerns at the solar power plant, including predicting power generation for the next few days. 
                In the context of solar power generation, when photons interact with photovoltaic cells, they excite electrons, leading to the production of direct current (DC) energy.
                Subsequently, inverters are utilized to convert this DC power into alternating current (AC) for distribution and use in various networks, aligning with the design of buildings for AC transport and utilization.""")

st.sidebar.header("")
st.sidebar.header("")

# Apply filters to the dataframe
filtered_df = df[(df['DAY'].isin(day_filter)) & 
                 (df['MODULE_TEMPERATURE'] >= temp_range[0]) & 
                 (df['MODULE_TEMPERATURE'] <= temp_range[1])]



# Display different insights based on button selection
st.header(" ")
if selected_button == 'Summary Statistics':
    st.header("Summary Statistics")
    st.write(df.describe())
    st.subheader("Description :")
    st.markdown('This insight provides a summary of basic statistics for the dataset, including mean, median, and standard deviation.')

elif selected_button == 'AC and DC Power by day':
    st.header("AC and DC Power by Day")
    AC_prod = df[["AC_POWER", "DAY"]].groupby("DAY").mean().reset_index()
    DC_prod = df[["DC_POWER", "DAY"]].groupby("DAY").mean().reset_index()
    plt.figure(figsize=(18, 9))
    sns.lineplot(x='DAY', y='AC_POWER', data=AC_prod, marker='o', label='AC Power')
    sns.lineplot(x='DAY', y='DC_POWER', data=DC_prod, marker='o', label='DC Power')
    plt.title('Sum of AC and DC Power by Day')
    plt.xlabel('Day')
    plt.ylabel('Power')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This visualization shows the daily AC and DC power output of the solar plant.')

elif selected_button == 'Ambient and Module Temperature by Day':
    st.header("Ambient and Module Temperature by Day")
    Ambtemp_day = df[['AMBIENT_TEMPERATURE', 'DAY']].groupby('DAY').mean().reset_index()
    Modtemp_day = df[['MODULE_TEMPERATURE', 'DAY']].groupby('DAY').mean().reset_index()
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='DAY', y='AMBIENT_TEMPERATURE', data=Ambtemp_day, marker='o', label='Ambient Temperature')
    sns.lineplot(x='DAY', y='MODULE_TEMPERATURE', data=Modtemp_day, marker='o', label='Module Temperature')
    plt.title('Ambient and Module Temperature by Day')
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This section visualizes the daily average ambient temperature and module temperature. The chart provides a comparison of these two temperatures across different days, helping to understand how they vary over time.')



elif selected_button == 'Power Output for Selected Day':
    st.header("Power Output for Selected Day")
    selected_day = st.selectbox('Select Day', sorted(df['DAY'].unique()))
    filtered_data = df[df['DAY'] == selected_day]
    st.write(f"Data for Day {selected_day}")
    st.write(filtered_data)
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=filtered_data, x='TIME', y='AC_POWER', label='AC Power')
    sns.lineplot(data=filtered_data, x='TIME', y='DC_POWER', label='DC Power')
    plt.title(f"Power Output on Day {selected_day}")
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This section displays the power output for a selected day. You can choose a day from the dropdown, and the chart will show the AC and DC power output over time for that specific day.')


elif selected_button == 'Summary Statistics of AC and DC Power':
    st.header("Summary Statistics of AC and DC Power")
    st.write(df[['AC_POWER', 'DC_POWER']].describe())
    st.subheader("Description :")
    st.markdown('This section displays the summary statistics for AC Power and DC Power, including metrics such as mean, standard deviation, minimum, maximum, and quartiles. This provides a quick overview of the distribution and range of power values in the dataset.')


elif selected_button == 'Correlation between Ambient and Module Temperature':
    st.header("Correlation between Ambient and Module Temperature")
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x='AMBIENT_TEMPERATURE', y='MODULE_TEMPERATURE')
    plt.title('Ambient Temperature vs Module Temperature')
    plt.xlabel('Ambient Temperature')
    plt.ylabel('Module Temperature')
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This chart visualizes the relationship between ambient temperature and module temperature using a scatter plot. It helps in understanding how the module temperature varies with changes in ambient temperature.')


elif selected_button == 'Power Production by Hour':
    st.header("Power Production by Hour")
    df['HOUR'] = pd.to_datetime(df['TIME']).dt.hour
    hourly_power = df.groupby('HOUR')[['AC_POWER', 'DC_POWER']].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hourly_power, x='HOUR', y='AC_POWER', label='AC Power')
    sns.lineplot(data=hourly_power, x='HOUR', y='DC_POWER', label='DC Power')
    plt.title('Average Power Production by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Power')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This chart shows the average AC and DC power production for each hour of the day, allowing users to see how power generation varies over the course of the day.')


elif selected_button == 'Temperature Distribution':
    st.header("Temperature Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(df['MODULE_TEMPERATURE'], kde=True)
    plt.title('Distribution of Module Temperature')
    plt.xlabel('Module Temperature')
    plt.ylabel('Frequency')
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This histogram displays the distribution of module temperatures across the dataset, including a Kernel Density Estimate (KDE) to illustrate the temperature distribution more smoothly.')


elif selected_button == 'Temperature Relationship':
    st.header("Relationship Between Ambient and Module Temperature")
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x='AMBIENT_TEMPERATURE', y='MODULE_TEMPERATURE')
    plt.title('Ambient vs Module Temperature')
    plt.xlabel('Ambient Temperature')
    plt.ylabel('Module Temperature')
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This scatter plot illustrates the relationship between ambient temperature and module temperature, showing how variations in ambient temperature relate to changes in module temperature.')


elif selected_button == 'Power Output Comparison Betwenn Plants':
    st.header("Power Output Comparison Between Plants")
    avg_ac_power = df.groupby('PLANT_ID')['AC_POWER'].mean().reset_index()
    avg_dc_power = df.groupby('PLANT_ID')['DC_POWER'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(x='PLANT_ID', y='AC_POWER', data=avg_ac_power, label='AC Power')
    sns.barplot(x='PLANT_ID', y='DC_POWER', data=avg_dc_power, label='DC Power')
    plt.title('Average Power Output Comparison')
    plt.xlabel('Plant ID')
    plt.ylabel('Average Power')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This bar chart compares the average power output between different plants. It displays the average AC and DC power for each plant, providing insights into the performance differences across plants.')

elif selected_button == 'Peak Power Production Hours':
    st.header("Peak Power Production Hours")
    df['HOUR'] = pd.to_datetime(df['TIME']).dt.hour
    hourly_avg_power = df.groupby('HOUR')[['AC_POWER', 'DC_POWER']].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hourly_avg_power, x='HOUR', y='AC_POWER', label='AC Power')
    sns.lineplot(data=hourly_avg_power, x='HOUR', y='DC_POWER', label='DC Power')
    plt.title('Average Power Production by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Power')
    plt.axvline(hourly_avg_power['AC_POWER'].idxmax(), color='r', linestyle='--', label='Peak AC Power Hour')
    plt.axvline(hourly_avg_power['DC_POWER'].idxmax(), color='g', linestyle='--', label='Peak DC Power Hour')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This line chart illustrates the average power production for AC and DC power by hour of the day. It highlights the peak hours for both AC and DC power production using vertical dashed lines, allowing for easy identification of when the maximum power output occurs.')


elif selected_button == 'Power Production vs. Module Temperature':
    st.header("Power Production vs. Module Temperature")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='MODULE_TEMPERATURE', y='AC_POWER', label='AC Power')
    sns.scatterplot(data=df, x='MODULE_TEMPERATURE', y='DC_POWER', label='DC Power')
    plt.title('Power Production vs Module Temperature')
    plt.xlabel('Module Temperature')
    plt.ylabel('Power')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This scatter plot depicts the relationship between module temperature and power production, showing both AC and DC power outputs. Each point represents the power production at a specific module temperature, helping to visualize how temperature variations affect power output.')

elif selected_button == 'Daily Power Production Distribution':
    st.header("Daily Power Production Distribution")
    plt.figure(figsize=(12, 6))
    sns.histplot(df['AC_POWER'], kde=True, color='blue', label='AC Power')
    sns.histplot(df['DC_POWER'], kde=True, color='green', label='DC Power')
    plt.title('Distribution of Daily Power Production')
    plt.xlabel('Power')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('This histogram shows the distribution of daily power production for both AC and DC power outputs. It includes Kernel Density Estimation (KDE) curves to illustrate the density of power values, providing insights into the frequency and distribution of power production throughout the dataset.')

# Plant 1 vs Plant 2

if selected_button == 'Power Production vs. Ambient Temperature Comparison':
    st.header("Power Production vs Ambient Temperature Comparison")
    
    try:
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=df1, x='AMBIENT_TEMPERATURE', y='AC_POWER', label='Plant 1 AC Power', color='blue')
        sns.scatterplot(data=df2, x='AMBIENT_TEMPERATURE', y='AC_POWER', label='Plant 2 AC Power', color='orange')
        plt.title('AC Power Production vs Ambient Temperature')
        plt.xlabel('Ambient Temperature')
        plt.ylabel('AC Power')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
        
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=df1, x='AMBIENT_TEMPERATURE', y='DC_POWER', label='Plant 1 DC Power', color='blue')
        sns.scatterplot(data=df2, x='AMBIENT_TEMPERATURE', y='DC_POWER', label='Plant 2 DC Power', color='orange')
        plt.title('DC Power Production vs Ambient Temperature')
        plt.xlabel('Ambient Temperature')
        plt.ylabel('DC Power')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
        
        st.subheader("Description :")
        st.markdown('**This visualization compares power production against ambient temperature for two different plants.**\n\n'
            '**AC Power Production vs Ambient Temperature:** Scatter plots show the relationship between ambient temperature and AC power output for both Plant 1 (in blue) and Plant 2 (in orange).\n\n'
            '**DC Power Production vs Ambient Temperature:** Scatter plots illustrate how ambient temperature correlates with DC power output for the same plants, with Plant 1 in blue and Plant 2 in orange.')

    except KeyError as e:
        st.error(f"Column not found: {e}")
        

elif selected_button == 'Temperature Comparison':
    st.header("Temperature Comparison Between Plants")
    
    avg_temp_ambient_plant1 = df1[['AMBIENT_TEMPERATURE']].mean().iloc[0]
    avg_temp_module_plant1 = df1[['MODULE_TEMPERATURE']].mean().iloc[0]
    
    avg_temp_ambient_plant2 = df2[['AMBIENT_TEMPERATURE']].mean().iloc[0]
    avg_temp_module_plant2 = df2[['MODULE_TEMPERATURE']].mean().iloc[0]
    
    comparison_data = pd.DataFrame({
        'Plant': ['Plant 1', 'Plant 2'],
        'Ambient Temperature': [avg_temp_ambient_plant1, avg_temp_ambient_plant2],
        'Module Temperature': [avg_temp_module_plant1, avg_temp_module_plant2]
    })
    
    st.write(comparison_data)
    
    # Plot comparison
    comparison_data.set_index('Plant').plot(kind='bar', figsize=(10, 5))
    plt.title('Temperature Comparison')
    plt.ylabel('Average Temperature')
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('**This section presents a temperature comparison between Plant 1 and Plant 2.**\n\n'
            '**Ambient Temperature:** The average ambient temperature for both plants is displayed in a bar chart to compare the environmental conditions each plant is exposed to.\n\n'
            '**Module Temperature:** The average module temperature for each plant is also compared, providing insights into how temperature management differs between the two locations.')

elif selected_button == 'Daily Power Production Statistics':
    st.header("Daily Power Production Statistics Comparison")
    
    try:
        # Aggregating daily statistics for both plants
        daily_stats_plant1 = df1.groupby('DAY')[['AC_POWER', 'DC_POWER']].agg(['mean', 'median', 'std']).reset_index()
        daily_stats_plant2 = df2.groupby('DAY')[['AC_POWER', 'DC_POWER']].agg(['mean', 'median', 'std']).reset_index()
        
        st.subheader("Plant 1 Daily Power Statistics")
        st.write(daily_stats_plant1)
        
        st.subheader("Plant 2 Daily Power Statistics")
        st.write(daily_stats_plant2)
        
        # Extracting relevant statistics and plotting
        ac_power_mean_plant1 = daily_stats_plant1['AC_POWER']['mean']
        ac_power_mean_plant2 = daily_stats_plant2['AC_POWER']['mean']
        
        dc_power_mean_plant1 = daily_stats_plant1['DC_POWER']['mean']
        dc_power_mean_plant2 = daily_stats_plant2['DC_POWER']['mean']
        
        plt.figure(figsize=(14, 7))
        sns.boxplot(data=[ac_power_mean_plant1, ac_power_mean_plant2], palette='Set2')
        plt.xticks([0, 1], ['Plant 1 AC Power', 'Plant 2 AC Power'])
        plt.title('AC Power Daily Statistics')
        plt.ylabel('Mean AC Power')
        plt.grid(True)
        st.pyplot(plt)
        
        plt.figure(figsize=(14, 7))
        sns.boxplot(data=[dc_power_mean_plant1, dc_power_mean_plant2], palette='Set2')
        plt.xticks([0, 1], ['Plant 1 DC Power', 'Plant 2 DC Power'])
        plt.title('DC Power Daily Statistics')
        plt.ylabel('Mean DC Power')
        plt.grid(True)
        st.pyplot(plt)
        st.subheader("Description :")
        st.markdown('**This section provides a detailed comparison of daily power production statistics between Plant 1 and Plant 2.**\n\n'
            '**Daily Aggregated Statistics:** The daily mean, median, and standard deviation of AC and DC power for both plants are calculated and displayed. This gives a comprehensive overview of the day-to-day power production variability and central tendencies.\n\n'
            '**AC and DC Power Comparison:** The mean AC and DC power statistics for each plant are visualized using boxplots. These plots highlight the distribution of daily power output, making it easier to compare the performance of the two plants.')


    except KeyError as e:
        st.error(f"Column not found: {e}")


elif selected_button == 'Power Production Efficiency Comparison':
    st.header("Power Production Efficiency Comparison")
    
    # Calculate efficiency (AC/DC ratio)
    df1['Efficiency'] = df1['AC_POWER'] / df1['DC_POWER']
    df2['Efficiency'] = df2['AC_POWER'] / df2['DC_POWER']
    
    # Aggregate efficiency by day
    efficiency_by_day_plant1 = df1.groupby('DAY')['Efficiency'].mean().reset_index()
    efficiency_by_day_plant2 = df2.groupby('DAY')['Efficiency'].mean().reset_index()
    
    # Plot efficiency comparison
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=efficiency_by_day_plant1, x='DAY', y='Efficiency', label='Plant 1 Efficiency', marker='o')
    sns.lineplot(data=efficiency_by_day_plant2, x='DAY', y='Efficiency', label='Plant 2 Efficiency', marker='o')
    plt.title('Daily Power Production Efficiency Comparison')
    plt.xlabel('Day')
    plt.ylabel('Efficiency (AC/DC Ratio)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    st.subheader("Description :")
    st.markdown('**This section compares the power production efficiency between Plant 1 and Plant 2, focusing on the ratio of AC power to DC power, which is calculated daily for both plants.**\n\n'
            '1. **Efficiency Calculation:** Efficiency is determined by the ratio of AC power to DC power (AC/DC) for each plant. This metric provides insight into how effectively each plant converts DC power to AC power.\n\n'
            '2. **Daily Efficiency Visualization:** The daily average efficiency is plotted for both Plant 1 and Plant 2, allowing for an easy comparison of the two plants\' performance over time. The line plot with markers clearly shows trends and any fluctuations in efficiency across different days.')
