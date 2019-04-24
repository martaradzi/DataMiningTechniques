# Assignment 2 Expedia Kaggle Competition Notes

You'll need to submit a single file, which ranks the properties belonging to a user search on the likeliness that the property will be booked. Here, you should start with listing the property most likely to be booked. An example of part of such a file is shown below:

| srch_id  |  prop_id | 
|----------|----------| 
| 2        |  7771    | 
| 2        |  26540   | 
| 2        |  25579   | 
| 2        |  7374    | 
| 2        |  131173  | 
| 2        |  37331   | 
| 2        |  27090   | 
| 2        |  12938   | 
| 2        |  78858   | 
| 2        |  30434   | 
| 2        |  91899   | 
| 2        |  3105    | 
| 2        |  6399    | 
| 3        |  130729  | 
| 3        |  103937  | 
| 3        |  556881  |  

#### The following features are only provided in the training data, not the test data:

- position (on the search results page)
- click_bool (if user clicked on it)
- booking_bool (if the user booked it)
- gross_booking_usd (transaction cost)

We could come up with a way to predict these values in the test set...

---

### Approach 1 (using Pandas)
- read train data
   - set data types

- chunk the data
   - group by id, cluster, isbooking
   - reset_index and append (???)

- compute total bookings over the chunks
- compute # clicks for the bookings
- compute relevance of the clusters
   - compute weighted sum of bookings and clicks

- find most popular hotels for each destination group
   - e.g. by using nlargest() series (this was slow; they found a better way)

- find most popular hotel for all hotel groups above

- read in the test data
   - merge with most popular hotel clusters (above)
   - check the null values
      - fill these with most popular overall hotel clusters

- save submission as .csv
