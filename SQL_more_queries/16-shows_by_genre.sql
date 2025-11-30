-- Lists all shows and all genres linked to that show from the hbtn_0d_tvshows database.
-- Uses a LEFT JOIN to ensure all shows are listed, displaying NULL for the genre if none is linked.
SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
    tv_shows.title ASC,
    tv_genres.name ASC;
