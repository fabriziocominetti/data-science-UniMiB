# Foundations of Computer Science

## Overview

You have to work on the files:

- Books
- Book ratings
- Users
- Goodbooks books
- Goodbooks ratings

## Notes

It is mandatory to use GitHub for developing the project.

The project must be a jupyter notebook.

There is no restriction on the libraries that can be used, nor on the Python version.

To read those files, you need to use the encoding = 'latin-1' option.

All questions on the project must be asked in a public channel on Zulip, otherwise no answer will be given.

## Project

| Index | Description | Status | 
| :--- | :---------- | :----: |
| 1 | Normalize the location field of Users dataset, splitting into city, region, country. | &#10004; |
| 2 | For each book in the Books dataset, compute its average rating. | &#10004; |
| 3 | For each book in the GoodBooks dataset, compute its average rating. | &#10004; |
| 4 | Merge together all rows sharing the same book title, author and publisher. We will call the resulting datset merged books. The books that have not been merged together will not appear in merged books. | &#10004; |
| 5 | For each book in merged books compute its average rating. | &#10004; |
| 6 | For each book in merged books compute the minimum and maximum of the average ratings over all corresponding books in the books dataset. | &#10004; |
| 7 | For each book in goodbooks, compute the list of its authors. Assuming that the number of reviews with a text (column work_text_reviews_count) is split equally among all authors, find for each authors the total number of reviews with a text. We will call this quantity the shared number of reviews with a text. | &#10004; |
| 8 | For each year of publication, determine the author that has the largest value of the shared number of reviews with a text. | &#10004; |
| 9 | Assuming that there are no errors in the ISBN fields, find the books in both datasets, and compute the difference of average rating according to the ratings and the goodratings datasets | &#10004; |
| 10 | Split the users dataset according to the age. One dataset contains the users with unknown age, one with age 0-14, one with age 15-24, one with age 25-34, and so on. | &#10004; |
| 11 | Find the books that appear only in the goodbooks datasets. | &#10004; |
| 12 | Assuming that each pair (author, title) identifies a book, for each book find the number of times it appears in the books dataset. Which books appear the most times? | &#10004; |
| 13 | Find the author with the highest average rating according to the goodbooks datasets. | &#10004; |