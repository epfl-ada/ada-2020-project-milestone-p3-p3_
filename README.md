# ada-2020-project-milestone-p3-p3_

## Title: Investigating Friendships across Time and Space

### Abstract
While the original publication explored human mobility in building models in respect to social connection and time, the goal of our creative extension is to turn the tables: We want to inspect how properties of friendship networks differ in respect to where an individual resides and the time of the year.  
Similar to milestone 2, we will assign a home location to each user within the **Gowalla** and **Brightkite** datasets that the original publication used. Using these home locations, we are then able to differentiate individuals based on whether they live in a sizeable city or not, and based on which country they reside in. Using this split, we will investigate different characteristics of each individual social network; this includes the amount of friends individuals have and the frequency of visiting friends. Additionally, it is our goal to detect certain sub-networks within these huge friendship networks that correspond to a group of friends.  
Finally, if time allows it, we want to investigate how strong the interconnection (in respect to inter-country friendships) between countries is, and whether they depend on characteristics such as the spoken languages and the practiced religions.


### Research Questions
For the following research questions, we are interested in how they behave on a global scale and across different countries/continents:
1. Are inhabitants of cities more likely to have more friends than individuals living in rural areas?
2. How often do users visit each other? Does it depend on whether they live in a city or not or on the season of the year?
3. Can we detect certain loosely connected sub-networks which corresponds to a circle of friends or a city? If yes, what is the probability that a user is part of such a circle of friends?
4. How does the interconnection between countries/continents differ? Does it depend on the language or religion?

### Proposed dataset

* [Gowalla](https://snap.stanford.edu/data/loc-Gowalla.html) and [Brightkite](https://snap.stanford.edu/data/loc-Brightkite.html) dataset from the paper. We will process them quite similarly to the replication report (Milestone 2): We will first discretize the world and find each user’s estimate home location. Furthermore, we will use the friendship data in order to build social networks.

* The [World Cities](https://simplemaps.com/data/world-cities) data set. This data set yields the GPS coordinates and the population of the 26568 biggest cities of the world. However, it does not contain the extent of each of those cities, which we thus have to determine in a different fashion.

* Use web-scraping on the [Wikipedia list of cities by country](https://en.wikipedia.org/wiki/Lists_of_cities_by_country) to obtain **city areas** for the cities in the World Cities dataset.

* Use web-scraping on the [Wikipedia list of countries](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population) in order to obtain country specific **languages** and **religions** (research question 4).

### Methods

#### Data aggregation:
Since the World Cities data set only contains the GPS location of a city we need an estimate of how far a users home can be from this location. This is achieved by scraping Wikipedia for the area of these cities. Then we will calculate the home of a user with the same method used in the original paper (dividing the world into 25x25 km grid and taking average location in the cell with the most checkins) and check if it falls within this distance.

For our fourth research question we also need to know the language and religion of the countries. This will also be retrieved by scraping.

#### Analysis:
To determine the frequency of visits between friends we will use the same method as in the original paper. That is, count check-ins that fall within a certain distance of a friend's home.

We will use the `networkx` library to explore different community detection algorithms in order to answer question 3. The resulting communities will then be analyzed with respect to their location. We will check if they correspond to a particular city, and how many of the users in that city they include. We might also visualize the communities on a global/country scale for a clearer picture of the structure of the communities across the world. The chosen scale will will depend on the size and structure of the communities we end up with.

Interconnection between countries will be based on how many edges in the social network graph have nodes in both countries.

In order to determine whether an user is living in a city or not, we will check if the user's home location is within a radius of a major city; where the radius is determined by the area of the corresponding city. To be exact, we draw circles around cities, such that the area occupied by the circle is identical to the real area of the city. Mathematically, this yields for the radius of the circle:

`r = sqrt(A/pi)`

### Proposed timeline

* Week 1:
	* web-scraping tasks
	* determine country/continent of user's home location
	* determine if user's home is within the are of a major city
	* build data-flow for splitting friendship network by country / continent / season
		* also filter by cross-country friendships (for research question 4)
* Week 2:
	* build functionality to detect sub-networks in friendship graphs and determine if users a part of any (and possibly how many) friend groups
	* now that data is prepared, investigate the research questions
* Week 3:
	* evaluation of results
	* writing the report
	* creating a video
	* rest of the time serves as a time-buffer for unexpected complications that may arise during week 1 and week 2


### Organization within the team

The milestones are the same as in the section above.
* Devrim:
	* Week 1: Will deal with web-scraping in the first weeks
	* Week 2: Investigates research questions together with Nina
	* Week 3: Focus on video, but generally participation in all due tasks for week 3
* Nina:
	* Week 1: Programs function to determine the the country/continent of coordinates
	* Week 2: Investigates research questions together with Devrim
	* Week 3: Focus on evaluating the results, but generally participation in all due tasks for week 3
* Carl:
	* Week 1: Programs function for determining, whether a location is withing a city. Also deals with splitting the data.
	* Week 2: Programs function to detect sub-networks within a friendship network.
	* Week 3: Main focus will lie on writing the report, generally participation in all due tasks for week 3

### Questions for TAs (optional):
We were really unsure to determine the amount of time each task would take, which is why we included research question 4, just in case that we have the time for it. We hope that this is not a problem. Rather than not stating it all, we wanted to state it with the condition of doing it if we have time to spare.
