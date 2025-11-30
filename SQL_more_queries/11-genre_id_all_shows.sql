-- Lists all shows in the hbtn_0d_tvshows database, displaying their genre ID or NULL if no genre is linked.
-- Uses a LEFT JOIN to ensure all shows from tv_shows are included.
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
