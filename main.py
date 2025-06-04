import streamlit as st
import os
import pandas as pd
st.write({"key":"Value"})
st.write("Hello World")
3+4
pressed = st.button("press me")
print(pressed)
st.title("Stream lit workproject")
st.header("Py workbook")
st.subheader("Subheader")
st.markdown("_Markdown_")
st.caption("Small texts")
code_ex = """ 
def greet(name):
    print("Welcome", name)
"""
st.code(code_ex, language="python")
st.image(os.path.join(os.getcwd(),"static","lzi.jpg"))
st.divider()
st.title("Streamlit Interface")

text_input = st.text_input("Enter text:")

number_input = st.number_input("Enter a number:", value=0)

checkbox = st.checkbox("Show additional input")

if checkbox:
    conditional_text_input = st.text_input("Enter additional text:")

options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Select an option:", options)

date_input = st.date_input("Select a date:")

st.write("You entered:")
st.write(f"Text: {text_input}")
st.write(f"Number: {number_input}")
if checkbox:
    st.write(f"Additional Text: {conditional_text_input}")
st.write(f"Selected Option: {selected_option}")
st.write(f"Date: {date_input}")
st.divider()


# Text Elements
st.write("Hello, Streamlit!")  # Displays text, dataframes, plots, etc. (very versatile)
st.title("My App Title")      # Displays a large, prominent title
st.header("Section Header")    # Displays a medium-sized header
st.subheader("Sub-section")   # Displays a smaller subheader
st.text("Plain text content") # Displays fixed-width text
st.markdown("## Markdown **Bold**") # Renders Markdown formatted text
st.latex(r"E=mc^2")            # Displays LaTeX mathematical expressions
st.code("print('Hello')", language='python') # Displays code block with syntax highlighting

# Data Display Elements
st.dataframe(df)              # Displays an interactive table (pandas DataFrame)
st.table(data)                # Displays a static table (list of lists, dicts, df)
st.json({'key': 'value'})     # Displays a JSON object
st.metric("Temperature", "25°C", "2°C") # Displays a key metric with an optional indicator

# Media Elements
st.image("path/to/image.png", caption="My Image") # Displays an image
st.audio("path/to/audio.mp3") # Displays an audio player
st.video("path/to/video.mp4") # Displays a video player

# Chart Elements (simplified for common chart types)
st.line_chart(data)           # Displays a simple line chart
st.area_chart(data)           # Displays a simple area chart
st.bar_chart(data)            # Displays a simple bar chart
# For more complex charts, use libraries like Plotly, Matplotlib, Altair with st.pyplot(), st.plotly_chart(), etc.

# Input Widgets (User Interaction)
st.button("Click Me")         # Displays a button
st.checkbox("Agree?")         # Displays a checkbox
st.radio("Choose one", options=['A', 'B']) # Displays radio buttons
st.selectbox("Select an option", options=['1', '2']) # Displays a dropdown select box
st.multiselect("Select multiple", options=['X', 'Y']) # Displays a multi-select dropdown
st.slider("Select a value", min_value=0, max_value=100) # Displays a slider
st.text_input("Enter text")   # Displays a single-line text input
st.number_input("Enter a number") # Displays a numerical input
st.text_area("Enter long text") # Displays a multi-line text area
st.date_input("Select a date") # Displays a date picker
st.time_input("Select a time") # Displays a time picker
st.file_uploader("Upload a file") # Displays a file uploader
st.camera_input("Take a picture") # Captures an image from the user's camera

# Layout and Status Elements
st.sidebar("Content for sidebar") # Places elements in the sidebar
st.columns(2)                 # Creates columns for side-by-side layout
st.expander("Click to expand") # Creates an expandable/collapsible section
st.tabs(["Tab 1", "Tab 2"])   # Creates tabs for organizing content
st.empty()                    # Creates a placeholder that can be updated later
st.spinner("Loading...")      # Displays a temporary loading spinner
st.success("Task completed!") # Displays a success message
st.error("Something went wrong!") # Displays an error message
st.warning("Proceed with caution.") # Displays a warning message
st.info("Here's some info.")  # Displays an informational message
st.progress(value)            # Displays a progress bar
st.status("Running task", expanded=True) # Displays a collapsible status container

# Control Flow / Optimization
st.session_state              # Accesses the session state dictionary for persistent data
st.cache_data(func)           # Caches data returned by a function to avoid re-computation
st.cache_resource(func)       # Caches a resource (like a model or database connection)

# Helper for external plots (e.g., Matplotlib, Seaborn)
st.pyplot(fig)                # Displays a Matplotlib figure
st.plotly_chart(fig)          # Displays a Plotly figure
st.altair_chart(chart)        # Displays an Altair chart