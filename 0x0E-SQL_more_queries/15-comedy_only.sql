-- Lists all genres and displays the number of shows linked to each
SELECT ts.title 
  FROM tv_genres tg, tv_show_genres tsg, tv_shows ts
 WHERE tg.id = tsg.genre_id AND tsg.show_id = ts.id
   AND tg.name = "Comedy"
 ORDER BY ts.title;
