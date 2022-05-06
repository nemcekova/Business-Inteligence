USE covid19;

create table fact_covid(
	date_id INT,
	CONSTRAINT FK_date_covid_id FOREIGN KEY(date_id) REFERENCES dim_date(DateKey),
	country_id INT,
	CONSTRAINT FK_country_covid_id FOREIGN KEY(country_id) REFERENCES dim_country(id),
	tests_id INT,
	CONSTRAINT FK_tests_id FOREIGN KEY(tests_id) REFERENCES dim_tests(id),
	number_of_deaths INT NOT NULL,
	number_of_tests INT NOT NULL,
	positive_increase INT NOT NULL,
	new_vaccinations INT NOT NULL
);

create table fact_restrictions(
	date_id INT,
	CONSTRAINT FK_date_restrictions_id FOREIGN KEY(date_id) REFERENCES dim_date(DateKey),
	country_id INT,
	CONSTRAINT FK_country_restrictions_id FOREIGN KEY(country_id) REFERENCES dim_country(id),
	restriction_id INT,
	CONSTRAINT FK_restriction_id FOREIGN KEY(restriction_id) REFERENCES dim_restriction(id),
	borders_id INT,
	CONSTRAINT FK_borders_id FOREIGN KEY(borders_id) REFERENCES dim_borders(id),
	masks_id INT,
	CONSTRAINT FK_masks_id FOREIGN KEY(masks_id) REFERENCES dim_masks(id),
	closure_id INT,
	CONSTRAINT FK_closure_id FOREIGN KEY(closure_id) REFERENCES dim_closure(id)
);

create table fact_weather(
	date_id INT,
	CONSTRAINT FK_date_weather_id FOREIGN KEY(date_id) REFERENCES dim_date(DateKey),
	country_id INT,
	CONSTRAINT FK_country__weather_id FOREIGN KEY(country_id) REFERENCES dim_country(id),
	weather_id INT,
	CONSTRAINT FK_weather_id FOREIGN KEY(weather_id) REFERENCES dim_weather(id),
	temperature FLOAT NOT NULL,
	humidity INT
);