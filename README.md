# ada-2020-project-milestone-p3-p3_
Title: Detecting an influence of urban life on people's social network sizes


Abstract:
	While the original paper explores human mobility by build-ing a model that incorporates social networks, we want to turn the tables and investigate social networks in regard to their geographical background. First we visualise the friendship network in the Gowalla, Brighkite dataset geographically. 
  In order to determine for each user whether he/she is living either in a city or in the countryside, we will compare their estimated home location with data from the world cities data set. Relative to each cities population, we approximate its extension to decide whether a user lives in a city or not. Furthermore, we are interested in complexion of the general social network and the social networks of each user; especially we want to determine different properties of said networks in respect to their estimated home location and season of the year. This will allow us to understand the influence of a person’s home location on her social network size and can help in further understanding the effect of living in a city or not has on a person’s mental health (if e.g. the size of someone’s friends network correlates with personal happiness).
		
	
Research Questions:
  1. We want to compare continents:
  2. Given a social network whose nodes are spaced according to the respective user’s estimated home location, can we detect certain loosely connected subnetworks which corresponds to a circle of friends or a city?
  3. Are people in cities more likely to have more friends in the social network than people living in rural areas?
  4. How does the frequency of contacts between friends correlate with the fact that they are in the city versus in the rural areas?
  5. Does the frequency of communication between friends depend on the season of the year? (TODO just came tomind, but we didnt talk about this once in the abstract.bit unsure how to include this and the following questioninto the main topic, i.e. the first 4 questions)

	
Proposed dataset:	
	- Gowalla and Brightkite dataset from the paper 
		[https://snap.stanford.edu/data/loc-Gowalla.html]
		[https://snap.stanford.edu/data/loc-Brightkite.html]
		 We will process them quite similarly to the replication report (Milestone 2): We will first discretize the world and find each user’s estimate home location. Furthermore, we will use the friendship data in order to build social networks. 
		
	- The World Cities data set 
		[https://simplemaps.com/data/world-cities]
		-> This data set yield the GPS coordinates and the population of the 26568 biggest cities of the world. However, it does not contain the extent of each of those cities, which we thus have to determine in a different fashion.
	

Methods: 
Calculating the extend of a city (linked to world cities data set). Here we consider two options, with option 1s eemingly being more precise and effective: 
- Option 1: Gather another dataset, which contains the area for each city (possibly crawl Wikipedia). For each city, we will set a circle around it with its area being the actual area of the city.
- Option 2: Set the area of effect of cities in proportion to the number of inhabitants. Building a 3D social graph from the 2D coordinates of users’ home location that preserves the distances between them: Here we opt for a simple but effective approach: We will map each of the 2D coordinates onto a 3D global.
	
Proposed timeline:
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

Organization within the team:
	The milestones are the same as in the section above.
Week 1: Devrim will visualize the friendships, such thatthe resulting figure contains information about theusers’ home location. Carl will deal with a way ofdetermining a cities area, while Nina will investigate properties of the friendship networks.
Week 2: At this point, much of our next steps will dependon the results of the previous week. For this reason, this week will start by exchanging results we gained from our previously separated tasks. Carl will probably deal with assigning a ”is_in_city” feature to each  user, since he dealt with implementing the areas of cities. Nina and Devrim will at this point deal with whatever is left to do. 
Week 3: We will work together on evaluating all our final results, writing the report and coming up with a good outline for a video.
	
Questions for TAs (optional):
We are really excited for this Milestone, our only worry is that our idea is not sufficiently related to the focus of the original paper, mobility. We wanted to integrate mobility more by e.g. by investigating the effect of moving from the countryside to the city (or the other way round) has on the size of people’s friends circles, but we did not find suitable data and hence decided to only investigate static properties of social networks.







------------------------------------------------------------------
NOT USED: 

	To see whether an emerging difference in friend network sizes is significant, we introduce the Social circles data set which consists of 'friends lists' from Google+, Facebook and Twitter. Utilising this data, we will inspect the average size of a user's soial network in order to have a reference of how large a person's social network is in gerneral. 
	- The Social circles data set 
		[https://snap.stanford.edu/data/egonets-Gplus.html] 
		[https://snap.stanford.edu/data/egonets-Facebook.html]
		[https://snap.stanford.edu/data/egonets-Twitter.html]
	-> We will mainly focus on the edge	
