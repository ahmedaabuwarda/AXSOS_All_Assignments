/*
Forward engineer the friendships_schema from the previous chapter
Query: Create 6 new users
*/

SELECT * FROM Friendships.users;

insert into users (first_name, last_name) 
values ("ahmed", "abuwarda"),("Mohammed","Ashi"),("Nor", "Nasser"),
("Sameer", "Massod"),("Masood","Abuhol"),("Fadi","Shihada");

select * from friendships;
/*
Query: Have user 1 be friends with users 2, 4, and 6
Query: Have user 2 be friends with users 1, 3, and 5
Query: Have user 3 be friends with users 2 and 5
Query: Have user 4 be friends with user 3
Query: Have user 5 be friends with users 1 and 6
Query: Have user 6 be friends with users 2 and 3
*/
insert into friendships (user_id, friend_id) values (1,2),(1,4),(1,6),
(2,1),(2,3),(2,5),
(3,2),(3,5),
(4,3),
(5,1),(5,6),
(6,2),(6,3);

/* Query: Display the relationships created as shown in the above image */
select users.first_name, users.last_name, friends.first_name as friend_first_name,
 friends.last_name as friend_last_name
from users
join friendships on users.id = friendships.user_id
left join users as friends on friends.id = friendships.friend_id;

/* NINJA Query: Return all users who are friends with the first user, 
and make sure their names are displayed in the results. */
select users.first_name, users.last_name, friends.first_name as friend_first_name, friends.last_name as friend_last_name
from users
join friendships on users.id = friendships.user_id
left join users as friends on friends.id = friendships.friend_id
where users.id = 1;

/* NINJA Query: Return the count of all friendships */
select users.first_name, count(users.first_name) as number_of_friends
from users
join friendships on users.id = friendships.user_id
left join users as friends on friends.id = friendships.friend_id group by users.first_name;

/* NINJA Query: Find out who has the most friends and return the count of their friends. */
select users.first_name, count(*) as number_of_friends
from users
join friendships on users.id = friendships.user_id
group by users.first_name
order by number_of_friends desc
limit 1;

/* NINJA Query: Return the friends of the third user in alphabetical order */
select friends.first_name, friends.last_name
from users
join friendships on users.id = friendships.user_id
join users as friends on friends.id = friendships.friend_id
where users.id = 3
order by friends.first_name;
