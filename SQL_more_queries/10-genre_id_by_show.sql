-- Lists all shows that have at least one genre linked in the hbtn_0d_tvshows database.
-- Displays the show title and the genre ID.
-- Uses an INNER JOIN to link the shows and their genres.
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
