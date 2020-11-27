# ada-2020-project-milestone-p3-p3_

## Title: Investigating Friendships across Time and Space

### Abstract
While the original publication explored human mobility in building models in respect to social connection and time, the goal of our creative extension is to turn the tables: We want to inspect how properties of friendship networks differ in respect to where an individual resides and the time of the year.  
Similar to milestone 2, we will assign a home location to each user within the *Gowalla* and *Brightkite* datasets that the original publication used. Using these home locations, we are then able to differentiate individuals based on whether they live in a sizeable city or not, and based on which country they reside in. Using this split, we will then investigate different characteristics of each each individual social network; this includes the amount of friend individuals have and the frequency of visiting friends. Additionally, it is our goal to detect certain sub-networks within these huge friendship networks that correspond to a group of friends.
Finally, if time allows it, we want to investigate how strong the interconnection (in respect to inter-country friendships) between countries is, and whether they depend on characteristics such as the spoken languages and the practiced religions. 


### Research Questions
For the following research questions, we are interested in how they behave on a global scale and across different countries/continents:
1. Are inhabitants of cities more likely to have more friends than individuals living in rural areas?
2. How often do users visit each other? Does it depend on whether they live in a city or not or the season of the year?
3. Can we detect certain loosely connected sub-networks which corresponds to a circle of friends or a city? If yes, what is the probability that a user is part such a circle of friends?
4. How does the interconnection between countries/continents differ? Does it depend on the language or religion?

### Proposed dataset

* [Gowalla](https://snap.stanford.edu/data/loc-Gowalla.html) and [Brightkite](https://snap.stanford.edu/data/loc-Brightkite.html) dataset from the paper. We will process them quite similarly to the replication report (Milestone 2): We will first discretize the world and find each user’s estimate home location. Furthermore, we will use the friendship data in order to build social networks.

* The [World Cities](https://simplemaps.com/data/world-cities) data set. This data set yields the GPS coordinates and the population of the 26568 biggest cities of the world. However, it does not contain the extent of each of those cities, which we thus have to determine in a different fashion.

* Use web-scraping on the [Wikipedia list of countries](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population) in order to obtain country specific *lanuages* and *religions*. (Research Question 4)

* Use web-scarping on the [Wikipedia list of cities by country](https://en.wikipedia.org/wiki/Lists_of_cities_by_country) to obtain *city areas* for the cities in the World Cities dataset.

### Methods

Calculating the extend of a city (linked to world cities data set). Here we consider two options, with option 1s eemingly being more precise and effective:
* Gather another dataset, which contains the area for each city (possibly crawl Wikipedia). For each city, we will set a circle around it with its area being the actual area of the city.



### Proposed timeline

Week 1:
  1. For each of the datasets, visualize the corresponding social network geographically.
  2. For each of the cities, determine some way of deciding, whether a coordinate is within its area (i.e. individuals home is part of the city) or not.
  3. Determine properties of the general social networks: How many friends in average? Can we detect loosely connected sub-networks?

Week 2:
  1. Start investigating the differences in friendships inrespect to the users’ home location.
  2. (TODO only if we decide we want and we have theright data) Look at the seasonal difference for thecommunication between friends.
  3. (TODO only if we decide to and have the data)For each friendship, investigate the proportion ofinitiated communications between two friends.

Week 3:
  1. Evaluation of results.
  2. Writing the report.
  3. Creating a video

### Organization within the team

The milestones are the same as in the section above.
- Week 1: Devrim will visualize the friendships, such thatthe resulting figure contains information about theusers’ home location. Carl will deal with a way ofdetermining a cities area, while Nina will investigate properties of the friendship networks.
- Week 2: At this point, much of our next steps will dependon the results of the previous week. For this reason, this week will start by exchanging results we gained from our previously separated tasks. Carl will probably deal with assigning a ”is_in_city” feature to each  user, since he dealt with implementing the areas of cities. Nina and Devrim will at this point deal with whatever is left to do.
- Week 3: We will work together on evaluating all our final results, writing the report and coming up with a good outline for a video.

### Questions for TAs (optional):
We are really excited for this Milestone, our only worry is that our idea is not sufficiently related to the focus of the original paper, mobility. We wanted to integrate mobility more by e.g. by investigating the effect of moving from the countryside to the city (or the other way round) has on the size of people’s friends circles, but we did not find suitable data and hence decided to only investigate static properties of social networks.
