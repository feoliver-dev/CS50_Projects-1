#    Nocturne World
#### Video Demo:  https://youtu.be/WLgr9Mp-VDc
#### Description:

### The beggining
It all started when I thought about doing the final project. At first, I wanted to use C language, cause I really liked it. But later, I noticed that I was just avoiding frontend, even during the course, I was just doing the necessary. And I have chosen not to keep with fear and not to contempt myself with the low level of skills that I had. That's when Nocturne World begun.

### The planning
My first thought after the idea of creating a website with Flask, was to think about everything that I wanted to do. First of all what type of site? A blog, so I could talk about something that I enjoy. That way, it would be very satisfatying to create the blog, and it was. I have chosen Goth as the main theme of the project, and for that reason, I made a long search so as not to talk nonsense. I spen long weeks reading, listening and also writting all the content that the website displays. After couple searches, I planned exactlly what were the main subjects related to the goth subculture. I also planned how I wanted the layout of the blog, so as to start creating the folders to programm. One of the hardest parts of this project, was choosing the amount of content that I would talk about, and control my time on searching. But I managed to keep focus on the main content(and not in deatils) that would satisfy the needs of each page created.

### app.py
##### I started by creating this folder, so as to set Flask during the coding process. I created routes to each part I had planned before. Which were: index, history, art, architecture, cinema, dance, literature, music, painting, sculpture, fashion and about. Each of them should return the template with the HTML content that I was creating for the blog, also redirect when necessary.

### templates
##### A folder that holds every single HTML file in this project.

### base.html
##### This HTML folder was written to create the layout extended to each of the templates. Which were the header(with the title and icon) and the navigation bar, with the menu. Also wrote it to be responsive.

### index.html
##### Is the actual homepage. I created a card-deck, wich is like a row of cards. Each of them buttons redirect the user to other page. The three of them correspond to each subject: history, art and fashion. It was hard to style this later, so as to be responsive and keep a good looking size of both cards and images.

### history.html
##### I created a page to keep a long text about goth through history. With one row of three columns, two of them with three images each, aside from the text, creating a border.


### art.html
##### This template creates a big row of 7 cards, which corresponds to the 7 arts. They'll redirect the user to the art they choose to lear more about. When in cellphones, it will display vertically. From this one, I created more 7 folders, to create a singular HTML template explaining about each of them all.

### architecture.html
##### I made a pattern(with a row) of images related to the buildings architecture that were an example of what the text in the column aside talked about.

### cinema.html
##### In this one, the images are from each movie I talk about in the last three paragraphs of the text. I also created a column so as both text and images were side to side.

### dance.html
##### This one is the smallest content from all arts talked about. Since I didn't found any deep information about goth or gothic dance, I tried to resume what I found and display couple links, to videos as an example too. A row with the images creating a pattern aside the text and links, to be more aesthetically pleasant.

### literature.html
##### I used a similar layout as in history page, but all the images are related to references made in the text.

### music.html
##### This is a huge page, since it's the base of the goth subculture, I put a lot of content on it. I intercalated both containers and rows(with columns), to distribute the genres introduction and the bands info. The columns also intercalate between the cover of the first album of the band, the text about them and a picture of them. I tried to follow the same structure in the text about the groups too.

### painting.html
##### Here is a row of columns again. The images also works as an example of painting from gothic art, artistic movement that's explained in the text.

### sculpture.html
##### The images here work, again, as an example of the gothic sculptures. The text displays many infos about this art that is not very known when gothic art is the subject.


### fashion.html
##### I created a row with three images. The first one is just a picture of a random example of goth style. The middle one is the text, talking about goth style and more specific aesthetics. The third one shows images of this gothic style that were specified.

### about.html
##### A small text about who and what's behind the blog. With a image of a known figure related to goth aesthetics.

### static
##### It's where is the style.css folder, to style every single template and their elements.

### style.css
##### The aesthetic choices were made thinking in a spcefic collor palette, so as to have a kind of darker, but not creepy or too strong vibe. I also tried to keep simples, with the font and collors of the texts. I tried to keep the pattern of the elements, changing collor so as not to be boring for the user to navigate. Sized the cards, images and containers size and more in here. And also the responsive aspects were written there. I tried to keep a minimalistic aspect when it was about the text, and the style os the elements of the template. That way, I could work more in the collors so it wouldn't be tedious, and so as to use collor tones that are related to goth aesthetic too.
