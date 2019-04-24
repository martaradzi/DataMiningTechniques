# Assignment 2 Expedia Kaggle Competition Notes

## Approach 1 (using Pandas)
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
