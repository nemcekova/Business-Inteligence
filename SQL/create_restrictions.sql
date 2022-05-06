use covid19;

create table restrictions(
	[id] INT NOT NULL IDENTITY(1,1) PRIMARY KEY
      ,[name] VARCHAR(50) NOT NULL
      ,[code] VARCHAR(5) NOT NULL
      ,[day] INT NOT NULL
      ,[month] INT NOT NULL
      ,[year] INT NOT NULL
      ,[date] datetime
      ,[stay_at_home] INT NOT NULL
      ,[closure_schools] INT NOT NULL
      ,[closure_workplace] INT NOT NULL
      ,[type_travel_controle] INT NOT NULL
      ,[public_events] INT NOT NULL 
      ,[masks] INT NOT NULL
);