-- Lists all shows that belong to the genre 'Comedy' in the hbtn_0d_tvshows database.
-- Uses INNER JOINs to connect the three necessary tables: tv_shows, tv_show_genres, and tv_genres.
SELECT
    tv_shows.title
FROM
    tv_shows
JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE
    tv_genres.name = 'Comedy'
ORDER BY
    tv_shows.title ASC;
