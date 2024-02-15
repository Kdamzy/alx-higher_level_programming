-- cript that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY tv_shows.title ASC;