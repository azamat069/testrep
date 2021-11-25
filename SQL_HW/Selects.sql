-- Создание employee

create table empolyee (
	id primary key serial,
	employee_name varchar(50) not null
);



select * from employees e;


insert into employees (id, employee_name)
values (default, 'Jason Fields');

--===================================================

--- Создание salary

create table salary (
	id serial primary key,
	monthly_salary int not null
);


select * from salary;

insert into salary (id, monthly_salary)
values (default, 2500);

--========================================================
 
-- Создание employee_salary

create table employee_salary (
	id serial primary key,
	employee_id int not null unique,
	salary_id int not null
);

select * from employee_salary;

insert into employee_salary (id, employee_id, salary_id)
values (default,80,15);

--======================================================

----Создание roles

create table roles (
	id serial primary key,
	role_name int not null unique
);

alter table roles 
alter column role_name type varchar (30)
using role_name::varchar(30);

select * from roles r 

insert into roles (id, role_name)
values (default, 'Senior Automation QA engineer')

--====================================================

-- Создание roles_employee

 create table roles_employee (
 	id serial primary key,
 	employee_id Int not null unique,
 	role_id Int not null,
	foreign key (employee_id)
		references employees(id),
	foreign key (role_id)
		references roles(id)
	);

select * from roles_employee re 

insert into roles_employee (id,employee_id,role_id)
values (default,10,18);
