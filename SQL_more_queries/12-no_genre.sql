-- Lists all shows in the hbtn_0d_tvshows database that do NOT have a genre linked.
-- Uses a LEFT JOIN to include all shows, and then filters for NULL genre_id.
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE
    tv_show_genres.genre_id IS NULL
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
