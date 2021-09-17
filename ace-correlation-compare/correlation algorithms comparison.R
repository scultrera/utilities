library(nlcor) # Some variables, x1 & y1 and others
library(acepack) #ace()

source("annotation_compass.R")


plot(x1, y1)

cor(x1, y1)
nlcor(x1, y1)

a = ace(x1, y1)
cor(a$tx, a$ty)


#-----------------------
#-- x2, y2
#-----------------------
plot(x2, y2)

cor(x2, y2)
nlcor(x2, y2)

a = ace(x2, y2)
cor(a$tx, a$ty)



#-----------------------
#-- x3, y3
#-----------------------
plot(x3, y3)
cor(x3, y3)
nlcor(x3, y3)
a = ace(x3, y3)
cor(a$tx, a$ty)



data(mtcars)
plot(mtcars$wt, mtcars$mpg)
cor(mtcars$wt, mtcars$mpg)
nlcor(mtcars$wt, mtcars$mpg)
a = ace(mtcars$wt, mtcars$mpg)
cor(a$tx, a$ty)


library(ggplot2)
library(gridExtra)
g = ggplot(mtcars, aes(x=wt, y=mpg)) + geom_point()
g = g + annotation_compass(label="Pearson Cor=-0.87\nMaximal (ACE) Cor=0.93", position = "SW")
g = g + ggtitle("MTCars Vehicle Weight x MPG Correlation")
g = g + ylab("MPG") + xlab("Weight")
g

mydata = data.frame(x1 = x1, y1 = y1)

g2 = ggplot(mydata, aes(x=x1, y=y1)) + geom_point()
g2 = g2 + annotation_compass(label="Pearson Cor=0.008\nMaximal (ACE) Cor=0.88", position = "SE")
g2 = g2 + ggtitle("Cyclical Variables")
g2

grid.arrange(g, g2, ncol=2)


