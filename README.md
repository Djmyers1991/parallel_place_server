# Parallel Place: The Ultimate Book Club's Guide to this Novel

## Application Overview
Having taught literature and creative writing for ten years prior to beginning my career as web developer, I have stumbled across various exercises and prompts that engender fun and enlightening conversations in the classroom — or in book clubs. This full-stack content management application is the manifestation of all my experience as a writer, teacher, and reader. This application is meant to be a tool for educators to spark meaningful discussions and develop critical thinking skills in an engaging way. While this application centers currently on the novel I have written entitled This Parallel Place, the ultimate goal is for this application to be a template that any educator can use for any novel or short story. 

In this application's present iteration, teachers are able to create/edit/delete assignments as well as vocabulary cards. They are also able to view student submissions and leave comments. Various filters were instilled in able for teachers to easily toggle between claimed and unclaimed submissions and for students to toggle between reviewed and unreviewed submissions. Teachers will also be able to view their individual student's inspiration lists by selecting a student's name from the dopdown. Please note that the inspiration list is simply a list of novels the students believed to have inspired This Parallel Place. On the other side, students are able to create/edit/delete their submissions as well as notecards. Students will only see their own submissions. While students will be able to see all of the vocabulary words posted by either their teachers or themselves, they will not be able to see any of the notecards posted by other students. Students can create/edit/delete novels from their own inspiration list. To prevent cheating, students will not be able to see any of their peer's lists. For students and teachers alike, various built-in activities were built in to foster dynamic learning. With the help of the drag and drop function, students will be able to rank their favorite and least favorite characters in descending order. Not to add too much of a spoiler, but the landing page has a time "time traveling" button where users can go back in time and witness how the past has been changed. The overall purpose of our application is to allow students and instrucots alike to engage with the assingned novel in such a way as to develop critical thinking skills within the mind and rapport within the classroom — or book club living room.

## Technologies Used

 ![HTML5](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![React](https://img.shields.io/badge/react%20-%2320232a.svg?&style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Git](https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white) 
[![Django](https://img.shields.io/badge/Django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python%20-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) 
![Visual Studio Code](https://img.shields.io/badge/VSCode%20-%23007ACC.svg?&style=for-the-badge&logo=visual-studio-code&logoColor=white) 
[![Bulma](https://img.shields.io/badge/Bulma-%2300D1B2.svg?style=for-the-badge&logo=bulma&logoColor=white)](https://bulma.io/)


 
## Getting Started

### Server Side
1. Clone this repository for the server side:
```sh
git clone git@github.com:Djmyers1991/parallel_place_server.git
cd parallel_place_server
```
2. Initialize virtual environment:
```sh
pipenv shell
```
3. Install pipenv:
```sh
pipenv install
```
4. Seed database with initial fixtures:
```sh
./seed_database.sh
```
   
5. Run the Server:
```sh
python3 manage.py runserver
```


### Client Side
1. Clone this repository for the client side:
```sh
git clone git@github.com:Djmyers1991/parallel-place-client-side.git 
cd parallel-place-client-side
```
2. Install dependencies: 
```sh
npm install
```
3. Run the code 
```sh
npm start
```
3. Login credentials: (Teacher = Daniel, Student = Jonathan)
```txt
username: JonathanVanDuyne@aol.com
password: lemmon
```
```txt
username: DanielMyers@aol.com
password: lemmon
```

## ERD

https://dbdiagram.io/d/Parallel-Place-Final-Capstone-64f749fd02bd1c4a5e02cc50

## Wireframe

https://miro.com/app/board/uXjVMAhOHYo=/?share_link_id=268571184966




## Parallel Place Client Side Code
https://github.com/Djmyers1991/parallel-place-client-side
