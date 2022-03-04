## Author Information
| Ride Share Web Application ||
| ------------- | ------------- |
| Project Description  | Web application for Data Scientist and \n traders to interact with data too big to send |
| Author  | Jonathan Baptiste  |
| Author Email  | Joey.baptiste@gmail.com  |
| Author Social | [LinkedIn](https://www.linkedin.com/in/baptiste-inc/) |

## Web Applications

### Statistical Analysis

The
[statisitcal analysis app](https://https://ridesharestats.anvil.app/) allows users to select a specific ride type they are interested in learning getting a stastical analysis on very quickly. Powered by Pandas this tool allows users to get a common stastics like mean, sum, std, min and max values and more.

### Chart Builder

The [chart builder app](https://ridesharecharts.anvil.app/) allows user to group, filter and add plotting parameters the subsection of the data and returns an image of the desired chart. By using the drop downs to select different parameters the pressing the respective "morph" button, users can easily generate a query that is sent to the Jupyter notebook. The query is used to build the plot and returns the image back to the users. The parameters correlate with a few of the pandas plot method for a dataframe.

[Chart](https://github.com/Joeybaptiste11/Ride_Share_Analysis_API/blob/main/Chart%20parameters.PNG?raw=true)

## Project Details

There was a lot I wanted to do with this project, given its open nature I could have approached it 100 different ways. I chose to highlight my skills in building functions in python and developing web applications and APIs. I made this decision based on the time allowed for this project, the size of the data, the open nature of the prompt, and the "messiness" of the data.

### Assumptions and Transformations

I decided to only focus on a subset of the data given the constraints listed in the "Constraints" section. First I chose to use a jupyter notebook as I new I would have to look through the data and test out some assumptions I had. The interactive nature of the notebook made this easy to do. Next was the parsing and cleaning aspect. The parsing and cleaning model exclusively matched traditional ride share products (UberX ride, Lyft ride) and ignored many of the other less prominent product types like "Earnings". This was because the formats were very inconsistent or I could not determine what the product description signified. Then I filtered the dataset to focus on orders from 2020 onwards. This was to reduce the size of the data for quicker transformation, more consistency, and faster API requests. Next, I dropped about have the columns as I believed they were irrelevant for the data I selected or too unclear.

### Constraints

The biggest constraint was the "messiness" of the data. Many of the columns were difficult to decypher and "product_desciption" column contained many different types of product is an inconsistent format. Just research all the information in the dataset was difficult so it would have been tough to clean and transform all the information available. In hindsight I believe reading and loading the data in chunks would have helpful for human analysis of the data (will go more in depth in the "What I would have done differently" section). Another big constraint was the time it took to process and clean the data. The "parse_ride_data" function took 10 hours to complete and crashed my laptop a few times. I would like to have optimized the function and make changes to the ftilers I chose but additional multi hour long processes would have slowed down later feature I wanted to add. I aimed to do a few things and have them well documented well rather do a lot in an unclear manner.

### What I would have done differently (given more time)

The first thing I would have done differently was use an supervised machine learning algorithm to perform the categorizing, cleaning, and trend analysis for me. I am currently still in the early stages of building knowledge of machine learning so to implement such an ambitious task would take research into topics I have yet to dive into as wellas the chance that I would not have suceeded in implementing it in the time given. Next I would have read the data with chunks rather than all at one. This is a good practice speed up the reading process as well as having the program run on less powerful machines (less RAM). Another approach I could have taken was to build out a relational database (SQL) in order to better manage the data as well as have a way for others to query with out the large csv file. In all I am happy with my decision and proud of my end result.


