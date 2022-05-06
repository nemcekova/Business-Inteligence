use covid19;

create table covid(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	date datetime,
	name VARCHAR(50) NOT NULL,
	testing_policy INT NOT NULL,
	number_of_deaths INT NOT NULL,
	number_of_tests INT NOT NULL,
	positive_increase INT NOT NULL,
	new_vaccinations INT NOT NULL

);