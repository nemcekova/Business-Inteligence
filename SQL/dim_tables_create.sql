USE covid19;

create table dim_date(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	day INT NOT NULL,
	month INT NOT NULL,
	year INT NOT NULL,
	day_of_the_week VARCHAR(20)
);

create table dim_country(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	code VARCHAR(5) NOT NULL,
	continent VARCHAR(20) NOT NULL
);

create table dim_weather(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	description VARCHAR(50) 
);

create table dim_restriction(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	public_events INT NOT NULL,
	stay_at_home INT NOT NULL
);

create table dim_closure(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	closure_schools INT NOT NULL,
	closure_workplace INT NOT NULL
);

create table dim_masks(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	masks INT NOT NULL 
);

create table dim_death(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	number_of_deaths INT NOT NULL 
);

create table dim_borders(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	type_travel_controle INT NOT NULL 
);

create table dim_tests(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	testing_policy INT 
);

create table dim_vaccination(
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	new_vaccinations INT NOT NULL 

);
