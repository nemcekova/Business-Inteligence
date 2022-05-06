use covid19;

delete from [dbo].[fact_covid];
delete from [dbo].[fact_restrictions];
delete from [dbo].[fact_weather];
delete from [dbo].[restrictions];
delete from [dbo].[weather];
delete from covid;
delete from dim_borders;
delete from dim_closure;
delete from dim_country;
delete from [dbo].[dim_date];
delete from [dbo].[dim_masks];
delete from [dbo].[dim_restriction];
delete from [dbo].[dim_tests];
delete from [dbo].[dim_weather];
