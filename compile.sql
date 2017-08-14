--将数据转换成更加方便切片的格式
/**
1.更新 r.name_zh
**/
UPDATE r
SET name_zh=id_name.pathname
FROM
(SELECT r.id,r_lname.route_id,r_name.pathname FROM r
INNER JOIN r_lname
ON r_lname.id=r.id
INNER JOIN r_name
ON r_lname.route_id=r_name.route_id
WHERE r_name.route_kind='0' and r_name.language='1') AS id_name
WHERE r.id = id_name.id;
/**
2.更新 r.name_en
**/
UPDATE r
SET name_en=id_name.pathname
FROM
(SELECT r.id,r_lname.route_id,r_name.pathname FROM r
INNER JOIN r_lname
ON r_lname.id=r.id
INNER JOIN r_name
ON r_lname.route_id=r_name.route_id
WHERE r_name.route_kind='0' and r_name.language='3') AS id_name
WHERE r.id = id_name.id;
/**
3.更新 r.name_id_en
**/
UPDATE r
SET name_id_en=id_name.pathname
FROM
(SELECT r.id,r_lname.route_id,r_name.pathname FROM r
INNER JOIN r_lname
ON r_lname.id=r.id
INNER JOIN r_name
ON r_lname.route_id=r_name.route_id
WHERE r_name.route_kind!='0' and r_name.language='3') AS id_name
WHERE r.id = id_name.id;
/**
4.更新 r.name_id_zh
**/
UPDATE r
SET name_id_zh=id_name.pathname
FROM
(SELECT r.id,r_lname.route_id,r_name.pathname FROM r
INNER JOIN r_lname
ON r_lname.id=r.id
INNER JOIN r_name
ON r_lname.route_id=r_name.route_id
WHERE r_name.route_kind!='0' and r_name.language='1') AS id_name
WHERE r.id = id_name.id;

/**
5.更新 poi.name_zh
**/
UPDATE poi
SET name_zh=pname_new.name
FROM
(SELECT * from pname WHERE nametype='9' and language='1' AND nameflag='1' ) AS pname_new
WHERE pname_new.featid=poi.poi_id
/**
6.更新 poi.name_en
**/
UPDATE poi
SET name_en=pname_new.name
FROM
(SELECT * from pname WHERE nametype='9' and language='3' AND nameflag='1' ) AS pname_new
WHERE pname_new.featid=poi.poi_id
/**
7.更新 poi.name_alias_zh
**/
UPDATE poi
SET name_alias_zh=pname_new.name
FROM
(SELECT * from pname WHERE nametype='9' and language='1' AND nameflag='2' ) AS pname_new
WHERE pname_new.featid=poi.poi_id
/**
8.更新 poi.name_en
**/
UPDATE poi
SET name_alias_en=pname_new.name
FROM
(SELECT * from pname WHERE nametype='9' and language='3' AND nameflag='2' ) AS pname_new
WHERE pname_new.featid=poi.poi_id
/**
9.更新 bl.name_zh
**/
UPDATE bl
SET name_zh=fname_new.name
FROM
(SELECT * from fname WHERE nametype='5' and language='1' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=bl.id
/**
10.更新 bl.name_en
**/
UPDATE bl
SET name_en=fname_new.name
FROM
(SELECT * from fname WHERE nametype='5' and language='3' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=bl.id
/**
11.更新 bl.name_alias_zh
**/
UPDATE bl
SET name_alias_zh=fname_new.name
FROM
(SELECT * from fname WHERE nametype='5' and language='1' AND nameflag='2' ) AS fname_new
WHERE fname_new.featid=bl.id
/**
12.更新 bl.name_alias_en
**/
UPDATE bl
SET name_alias_en=fname_new.name
FROM
(SELECT * from fname WHERE nametype='5' and language='3' AND nameflag='2' ) AS fname_new
WHERE fname_new.featid=bl.id
/**
13.更新 bp.name_zh
**/
UPDATE bp
SET name_zh=fname_new.name
FROM
(SELECT * from fname WHERE nametype='6' and language='1' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=bp.id;
/**
14.更新 bp.name_en
**/
UPDATE bp
SET name_en=fname_new.name
FROM
(SELECT * from fname WHERE nametype='6' and language='3' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=bp.id;
/**
15.更新 bp.name_alias_zh
**/
UPDATE bp
SET name_alias_zh=fname_new.name
FROM
(SELECT * from fname WHERE nametype='6' and language='1' AND nameflag='2' ) AS fname_new
WHERE fname_new.featid=bp.id;
/**
16.更新 bp.name_alias_en
**/
UPDATE bp
SET name_alias_en=fname_new.name
FROM
(SELECT * from fname WHERE nametype='6' and language='3' AND nameflag='2' ) AS fname_new
WHERE fname_new.featid=bp.id;
/**
13.更新 hamlet.name_zh
**/
UPDATE hamlet
SET name_zh=hmname_new.name
FROM
(SELECT * from hmname WHERE nametype='9' AND language='1' AND nameflag='1' ) AS hmname_new
WHERE hmname_new.featid=hamlet.poi_id;
/**
14.更新 bp.name_en
**/
UPDATE hamlet
SET name_en=hmname_new.name
FROM
(SELECT * from hmname WHERE nametype='9' AND language='3' AND nameflag='1' ) AS hmname_new
WHERE hmname_new.featid=hamlet.poi_id;
/**
13.更新 hamlet.name_alias_zh
**/
UPDATE hamlet
SET name_alias_zh=hmname_new.name
FROM
(SELECT * from hmname WHERE nametype='15' AND language='1' AND nameflag='1' ) AS hmname_new
WHERE hmname_new.featid=hamlet.poi_id;
/**
14.更新 bp.name_en
**/
UPDATE hamlet
SET name_alias_en=hmname_new.name
FROM
(SELECT * from hmname WHERE nametype='15' AND language='3' AND nameflag='1' ) AS hmname_new
WHERE hmname_new.featid=hamlet.poi_id;

/**
15.更新 r.ramp
**/
﻿update r set ramp=true where  substring(kind from 3 for 2)='0b' or substring(kind from 8 for 2)='0b' or substring(kind from 13 for 2)='0b'
or substring(kind from 18 for 2)='0b' or substring(kind from 23 for 2)='0b'/**
16.更新 r.tunnel
**/
﻿update r set tunnel=true where  substring(kind from 3 for 2)='0f' or substring(kind from 8 for 2)='0f' or substring(kind from 13 for 2)='0f'
or substring(kind from 18 for 2)='0f' or substring(kind from 23 for 2)='0f'
17.更新 r.tunnel
**/
﻿update r set tunnel=true where  substring(kind from 3 for 2)='0f' or substring(kind from 8 for 2)='0f' or substring(kind from 13 for 2)='0f'
or substring(kind from 18 for 2)='0f' or substring(kind from 23 for 2)='0f'

/**
18.更新 t.name_zh
**/
UPDATE t
SET name_zh=fname_new.name
FROM
(SELECT * from fname WHERE nametype='8' and language='1' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=t.id
/**
19.更新 t.name_en
**/
UPDATE t
SET name_en=fname_new.name
FROM
(SELECT * from fname WHERE nametype='8' and language='3' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=t.id;
/**
19.更新 d.name_zh
**/
UPDATE d
SET name_zh=fname_new.name
FROM
(SELECT * from fname WHERE nametype='14' and language='1' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=d.admincode
/**
20.更新 d.name_en
**/
UPDATE d
SET name_en=fname_new.name
FROM
(SELECT * from fname WHERE nametype='14' and language='3' AND nameflag='1' ) AS fname_new
WHERE fname_new.featid=d.admincode;

