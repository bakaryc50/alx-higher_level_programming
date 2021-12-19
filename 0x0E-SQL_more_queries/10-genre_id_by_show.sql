-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked
SELECT ts.title, tsg.genre_id
  FROM tv_shows ts, tv_show_genres tsg, tv_genres tg
 WHERE tg.id = tsg.genre_id
   AND ts.id = tsg.show_id
   AND tsg.genre_id > 0
 ORDER BY ts.title, tsg.genre_id ASC;
