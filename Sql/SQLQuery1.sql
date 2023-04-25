-- loome db
cReatE database TARge22

-- db valimine
use TARge22

-- db kustutamine
drop dataBASe TARge22

--- tabeli loomine
create table Gender
(
Id int not null primary key,
Gender nvarchar(10) not null
)

--andmete sisestamine tabelisse
insert into Gender (Id, Gender)
values (1, 'Female')
insert into Gender (Id, Gender)
values (2, 'Male')
insert into Gender (Id, Gender)
values (3, 'Unknown')

--- vaatame tabeli sisu
select * from Gender

-- tabeli tegemine
create table Person
(
Id int not null primary key,
Name nvarchar(30),
Email nvarchar(30),
GenderId int
)

insert into Person (Id, Name, Email, GenderId)
values (1, 'Superman', 's@s.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (2, 'Wonderwoman', 'w@w.com', 1)
insert into Person (Id, Name, Email, GenderId)
values (3, 'Batman', 'bat@bat.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (4, 'Aquaman', 'a@a.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (5, 'Catwoman', 'c@c.com', 1)
insert into Person (Id, Name, Email, GenderId)
values (6, 'Antman', 'ant"ant.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (8, NULL, NULL, 2)

--kuidas saab tabeli sisu vaadata???
select * from Person

-- võõrvõtme õhenduse loomine kahe tabeli vahel
alter table Person add constraint tblPerson_GenderId_FK
foreign key (GenderId) references Gender(Id)

--kui sisestad uue rea andmeid ja ei ole sisestanud GenderId alla väärtust,
-- siis see automaatselt sisetab sellele reale väärtuse 3
alter table Person
add constraint DF_Persons_GenderId
default 3 for GenderId

insert into Person (Id, Name, Email)
values (11, 'asdasd', 'asd@asd.com')

select * from Person

--piirangu maha v]tmine
alter table Person
drop constraint DF_Persons_GenderId

-- lisame uue veeru juurde
alter table Person
add Age nvarchar(10)

--lisame nr piirangu vanuse sisestamisel
alter table Person
add constraint CK_Person_Age check (Age > 0 and Age < 155)

--andmete uuendamine
update Person
set Age = 50
where Id = 6

select * from Person

insert into Person (Id, Name, Email, GenderId, Age)
values (10, 'Ironmn', 'i@iron.com', 2, 45)

-- lisame veeru juurde
alter table Person
add City nvarchar(50)

--- k]ik, kes elavad Gothami linnas
select * from Person where City = 'Gotham'
-- k]ik, kes ei ela Gothamis
select * from Person where City != 'Gotham'
-- k]ik, kes ei ela Gothamis, teine variant
select * from Person where City <> 'Gotham'

--n'itab teatud vanusega inimesi
select * from Person where Age = 120 or Age = 50 or Age = 28
select * from Person where Age in (120, 50, 28)

-- n'itab teatud vanusevahemikus olevaid inimesi
select * from Person where Age between 40 and 120

--wildcardi kasutamine e n'itab k]ik g-t'hega linnad
select * from Person where City like 'n%' 
-- email, milles on @ m'rk 
select * from Person where Email like '%@%'

-- n'itab k]iki, kellel on emailis ees ja 
-- peale @-m'rki ainult [ks t'ht
select * from Person where Email like '_@_.com'

-- k]ik, kellel nimes ei ole esimene t'ht W, A ja C
select * from Person where Name like '[^WAC]%'

--- kes elavad Gothamis ja New Yorkis
select * from Person where (City = 'Gotham' or City = 'New York')

-- kes elavad Gothamis ja New Yorkis ning on 
-- vanemad, kui 27
select * from Person where (City = 'Gotham' or City = 'New York')
and Age >= 27

-- kuvab t'hestikulises j'rjekorras inimesi 
-- ja v]tab aluseks nime
select * from Person order by Name
-- vastupidine j'rjestus
select * from Person order by Name desc

--v]tab kolm esimest rida
select top 3 * from Person

--kolm esimest, aga tabeli j'rjestuses on Age ja siis Name
select top 3 Age, Name from Person

--kuvab esimesed 50% tabelist
select top 50 percent * from Person

-- v]tab neli esimest ja j'rjestab vanuse j'rgi
select top 4 * from Person order by Age desc

-- muudab Age muutuja intiks ja n'itab 
-- vanuselises j'rjestuses
select * from Person order by CAST(Age as int)

--kuvab k]ige nooremat isikut
select MIN(CAST(Age as int)) from Person
--kuvab k]ige vanemat isikut
select Max(CAST(Age as int)) from Person


-- n'eme konkreetsetes linnades olevate isikute koondvanust
select City, SUM(Age) as TotalAge from Person group by City

-- muudame koodiga andmet[[pi ja selle pikkust
alter table Person
alter column Name varchar(25)


-- kuvab esimeses reas v'lja toodud j'rjestuses ja kuvab Age-i
-- TotalAge-ks
-- j'rjestab Citys olevate nimede j'rgi ja siis GenderId j'rgi
select City, GenderId, SUM(Age) as TotalAge from Person
group by City, GenderId order by City

-- n'itab, et miu rida on selles tabelis
select COUNT(*) from Person

-- n'itab tulemust, et mitu inimest on GenderId v''rtusega 2
-- konkreetses linnas
-- arvutab vanuse kokku selles linnas
select GenderId, City, SUM(Age) as TotalAge, COUNT(Id) 
as [Total Person(s)] from Person
where GenderId = '2'
group by GenderId, City

-- n'itab 'ra, et mitu inimest on koondvanusena 
-- vanemad, kui 41 ja kui 
-- palju igas linnas elab
select GenderId, City, SUM(Age) as TotalAge, COUNT(Id) 
as [Total Person(s)] from Person
group by GenderId, City having SUM(Age) > 41



-- loome kaks tabelit
create table Department
(
Id int primary key,
DepartmentName nvarchar(50),
[Location] nvarchar(50),
DepartmentHead nvarchar(50)
)

create table Employees
(
Id int primary key,
Name nvarchar(50),
Gender nvarchar(50),
Salary nvarchar(50),
DepartmentId int
)

insert into Employees values 
(1, 'Tom', 'Male', 4000, 1),
(2, 'Pam', 'Female', 3000, 3),
(3, 'John', 'Male', 3500, 1),
(4, 'Sam', 'Male', 4500, 2),
(5, 'Todd', 'Male', 2800, 2),
(6, 'Ben', 'Male', 7000, 1),
(7, 'Sara', 'Female', 4800, 3),
(8, 'Valarie', 'Female', 5500, 1),
(9, 'James', 'Male', 6500, NULL),
(10, 'Russell', 'Male', 8800, NULL)

insert into Department values
(1, 'IT', 'London', 'Rick'),
(2, 'Payroll', 'Delhi', 'Ron'),
(3, 'HR', 'New York', 'Christie'),
(4, 'Other Department', 'Sydney', 'Cindrella')

--- 24.03.2023 2 tund

select Name, Gender, Salary, DepartmentName
from Employees
left join Department
on Employees.DepartmentId = Department.Id

select * from Employees

--arvutab k]ikide palgad kokku
--kasutame CAST-i kuna Salary on nvarchar andmet[[p
-- SUM arvutab k]ik kokku
select SUM(CAST(Salary as int)) from Employees
-- min palga saaja
select min(CAST(Salary as int)) from Employees
-- [he kuu palgafond linnade l]ikes
select City, SUM(CAST(Salary as int)) as TotalSalary 
from Employees
group by City

alter table Employees
add City nvarchar(30)

-- toome soolise erisuse p'ringusse
select City, Gender, SUM(CAST(Salary as int)) as [Total Salary] 
from Employees group by City, Gender

--j'rjestab linnade kaupa palgafondi
select City, Gender, SUM(CAST(Salary as int)) as [Total Salary] 
from Employees group by City, Gender order by City

---loeb 'ra, mitu inimest on nimekirjas e mitu rida on tabelis
select COUNT(*) from Employees

--saan teada, kui palju on t;;tajaid soo kaupa linnas
select Gender, City, SUM(CAST(Salary as int)) as [Total Salary],
COUNT (Id) as [Total Employee(s)]
from Employees
group by Gender, City

--kuvab ainult k]ik mehed linnade kaupa
select Gender, City, SUM(CAST(Salary as int)) as [Total Salary],
COUNT (Id) as [Total Employee(s)]
from Employees
where Gender = 'Male'
group by Gender, City

--kuvab ainult k]ik naised linnade kaupa
select Gender, City, SUM(CAST(Salary as int)) as [Total Salary],
COUNT (Id) as [Total Employee(s)]
from Employees
group by Gender, City
having Gender = 'Female'

--- annab errori
select * from Employees where SUM(CAST(Salary as int)) > 4000

select Gender, City, SUM(CAST(Salary as int)) as TotalSalary,
COUNT (Id) as TotalEmployees
from Employees group by Gender, City
having SUM(CAST(Salary as int)) > 4000

--- inner join
-- kuvab neid, kellel on DepartmentName all olemas v''rtus
select Name, Gender, Salary, DepartmentName
from Employees
inner join Department
on Employees.DepartmentId = Department.Id

-- left join
-- v]tab k]ik andmed Employee tabelist
select Name, Gender, Salary, DepartmentName
from Employees
left join Department  -- v]ib kasutada ka LEFT OUTER JOIN-i
on Employees.DepartmentId = Department.Id

--- rigth join
-- v]tab k]ik v''rtused paremast tabelist
select Name, Gender, Salary, DepartmentName
from Employees
right join Department  -- v]ib kasutada ka RIGHT OUTER JOIN-i
on Employees.DepartmentId = Department.Id

--- outer join
--- kuvab k]ikide tabelite v''rtused [hte p'ringusse
select Name, Gender, Salary, DepartmentName
from Employees
full join Department -- v]ib kasutada ka FULL OUTER JOIN-i
on Employees.DepartmentId = Department.Id

-- cross join
select Name, Gender, Salary, DepartmentName
from Employees
cross join Department 

--inner join
select Name, Gender, Salary, DepartmentName
from Employees
inner join Department
on Department.Id = Employees.DepartmentId

--- n'itab k]iki neid kellel on Employees tabelis DepartmentName null
select Name, Gender, Salary, DepartmentName
from Employees
left join Department
on Department.Id = Employees.DepartmentId
where Department.Id is null

--- n'itab k]iki neid kellel on Employees tabelis DepartmentName null
select Name, Gender, Salary, DepartmentName
from Employees
left join Department
on Department.Id = Employees.DepartmentId
where Employees.DepartmentId is null

--- full join
--- m]lema tabeli mitte-kattuvate v''rtustega read kuvab v'lja
select Name, Gender, Salary, DepartmentName
from Employees
full join Department
on Employees.DepartmentId = Department.Id
where Employees.DepartmentId is null
or Department.Id is null

---kuues tund

--- kasutame inner joini kahe tabeli ühendamiseks, kuvab kõik
--- töötajad, kellel on Department Id olemas väärtus
select Name, Gender, Salary, DepartmentName
from Employees
inner join Department
on Employees.DepartmentId = Department.Id

select * from Department
-- right join tagastab meile andmed mõlemast tabelist ja
-- mittekuuluvad andmed, mis antud juhul on Other Department
select Name, Gender, Salary, DepartmentName
from Employees
right join Department
on Employees.DepartmentId = Department.Id

-- tahan saada kõik andmed mõlemast tabelist
-- osakonna töötajad ja osakonnad, kus pole töötajaid

select Name, Gender, Salary, DepartmentName
from Employees
full join Department
on Employees.DepartmentId = Department.Id


-- teeme päring kahele tabelile, kus tahame näha neid
-- töötajaid, kelle osakonna all on väärtus null
-- kasutame selles päringus lühendeid

select Name, Gender, Salary, DepartmentName
from Employees E
left join Department D
on E.DepartmentId = D.Id
Where D.Id is Null

-- teeme p2ringu kahele tabelile ja
-- kuvame Department tabeli, kus osakonna alla pole 
-- määratud töötajaid

select Name, Gender, Salary, DepartmentName
from Employees e
right join Department d
on e.DepartmentId = d.Id
where e.DepartmentId is Null

select * from Employees
select * from Department

-- teeme p2ringu kahele tabelile, kuvame read, kus
-- ei ole klappimist
select Name, Gender, Salary, DepartmentName
from Employees e
full join Department d
on e.Id = d.Id
where e.DepartmentId is null
or d.Id is null

-- lisame tabelisse uue veeru nimege ManagerId
alter table Employees
add ManagerId int null

select * from Employees
-- kes kellele allub
select e.Name as Employee, m.Name as Manager
from Employees e
left join Employees m
on e.ManagerId = m.Id

-- kuvame inimesi, kellel on ylemus
select e.Name as Employee, M.name as Manager
from Employees e
inner Join Employees m
on e.ManagerId = m.Id

-- igayks on omavahel p6imutud yhenduses

select e.Name as Employee, m.Name as Manager
from Employees e
cross join Employees m
--- 6 tunni lõpp

--7 tund

-- kuidas saada Null väärtuse asemel No Manager
-- kasutades Isnull

select e.Name as Employee, isnull(m.name, 'No manager') as Manager
from Employees e
left join Employees m
on e.ManagerId = m.Id

-- kuidas saada NULL vaartuse asemel no Manager ja kasutada else case
Select e.Name as Employee, case when m.Name is null then 'No manager'
else m.Name end as Manager
from Employees e
left join Employees m
on e.ManagerID = m.Id

-- kuidas null väärtuse asemel kuvad 'No manager' ja kasutada coalesce
select e.Name as Employee, coalesce(m.Name, 'No manager') as Manager
from Employees e
left join Employees m
on e.ManagerId = m.Id

-- lisame 2 veergu
alter table Employees
add MiddleName nvarchar(25) null,
LastName nvarchar(25) null 

-- Soovime n2ha firstname infot, kui v2hemalt yhes nimeveerus on 
-- valja toodud yks nime liike

select * from Employees 
select * from Employees 
select Id, coalesce(Name, MiddleName, LastName) as FirstName
from Employees

-- loome 2 uut objekti IndianCustomers ja
create Table IndianCustomers
(
Id Int,
Name nvarchar(25) null,
Email nvarchar(25) null
)

create Table UKCustomers
(
Id Int,
Name nvarchar(25) null,
Email nvarchar(25) null
)
-- lisame andmed koodiga
insert into IndianCustomers values
(1,'Raj','R@R.com'),
(2,'Sam','S@S.com')

insert into UKCustomers values
(1,'Ben','B@B.com'),
(2,'Sam','S@S.com')

select * from IndianCustomers
select * From UKCustomers

-- kuva kahe tabeli andmeid korraga
select Id, Name, Email from IndianCustomers
union all
select Id, Name, Email from UKCustomers

-- Kuva kahe tabeli andmeid aga duplikaadid ühendame üheks
select Id, Name, Email from IndianCustomers
union
select Id, Name, Email from UKCustomers

-- Kuvame kahe tabeli andmed korraga kuid järjestame tähestikuselt Name veeruga
select Id, Name, Email from IndianCustomers
union all
select Id, Name, Email from UKCustomers
order by Name

-- loome esimese stored procedure, mis annab meile iga kord sellest objektist nime ja soo
create procedure spGetEmployees
as Begin
select Name, Gender from Employees
end

-- kui sp on salvestatud siis saame kasutada seda sp koodiga
exec spGetEmployees
-- teine variant pikemalt
execute spGetEmployees
-- kolmas variant
spGetEmployees

-- teeme sp kus igal käivitamisel tuleb anda parameeter ette
create procedure spGetEmployeesByGenderAndDepartment
@Gender nvarchar(50),
@DepartmentId int
as begin
select Name, Gender from Employees
where Gender = @Gender and DepartmentId = @DepartmentId
end

-- sp koos väärtustega ja kindlasti peab järjestus olema õige, muidu tuleb error
select * from Employees
exec spGetEmployeesByGenderAndDepartment 'Male', 1

-- kuidas vaadata sp koodi
sp_helptext spGetEmployeesByGenderAndDepartment

-- sp koos encryptioniga
create proc spGetEmployeesByGenderAndDepartment2
@Gender nvarchar(50),
@DepartmentId Int
with encryption
as begin
select Name, Gender from Employees
where Gender = @Gender and DepartmentId = @DepartmentId
end

-- sp kustutamine
drop proc spGetEmployeesByGenderAndDepartment2

--9 tund
-- out ja output parameetrid SP tegemisel
create procedure spGetEmployeesCountByGender
@Gender nvarchar(20),
@EmployeeCount int output
as begin
select @EmployeeCount =  count(Id)
from Employees
where Gender = @Gender
end

-- output annab koondtulemuse, saame, et on 3 naistöötajat 
declare @EmployeeTotal int
execute spGetEmployeesCountByGender 'Female', @EmployeeTotal output
print @EmployeeTotal

-- kontrollime, on jah 3
select * From Employees

-- kasutame if ja else loogikat, et kuvada andmeid, kas kedagi on DB-s olemas
-- kasutame out parameetrit
declare @EmployeeTotalCount int
execute spGetEmployeesCountByGender 'Female', @EmployeeTotalCount output
if (@EmployeeTotalCount is null)
print '@EmployeeTotalCount is null'
else
print '@EmployeeTotalCount is not null'

-- kasutame out parameetrit ja saame tulemuse, et mitu inimest vastab tingimustele
declare @EmployeeT int
execute spGetEmployeesCountByGender @EmployeeCount = @EmployeeT out,
@Gender = 'Male'
print @EmployeeT

-- vaatame sp sisu
sp_helptext spGetEmployeesCountByGender

-- sp sõltuvus teistest
sp_depends spGetEmployeesCountByGender

-- mida tähendab @ koodis
-- seda kasutatakse muutujate deklareerimisel
-- C# var muutuja

-- soovime teada saada töötajate arvu ja teeme sp selle jaoks
create procedure spGetTotalCountOfEmployees1
@TotalCount int output
as begin
select @TotalCount = count(Id) from Employees
end

-- saame teada töötajate arvu
declare @TotalEmployees int
execute spGetTotalCountOfEmployees1 @TotalEmployees output
select @TotalEmployees

-- paneme sulgudesse selle parameetri, mis meile on tähtis
-- ja tahame saada teada ja teeme selle esimesena
create procedure spGetTotalCountOfEmployees2
as begin
return (select count(Id) from Employees)
end

-- saame teada töötajate arvu
declare @TotalEmployees int
execute @TotalEmployees = spGetTotalCountOfEmployees2
select @TotalEmployees

-- sp kus saame teada, et mis Id-le vastab konkreetne isik
create procedure spGetNameById1
@Id int,
@Name nvarchar(20) output
as begin
select @Name = Name from Employees where Id = @Id
end

-- soovime teada saada, et mis id all keegi on, pannes vastavaid numbreid spGetNameById1 järele
declare @EmployeeName nvarchar(20)
execute spGetNameById1 6, @EmployeeName output
print 'Name of Employee = '+@EmployeeName

-- teine lahendus
create procedure spGetNameById2
@Id int
as begin
return (select Name from Employees where Id = @Id)
end

-- teeme declare mis annab tulemuse, et mis isik on konkreetse Id taga
declare @EmployeeName nvarchar(20)
execute @EmployeeName = spGetNameById2 1
print 'The name of Emploee = ' + @EmployeeName

-- 10 tund
-- mis ASCII kood vastab mis tähele, A puhul 65
select ascii('A')
-- iterereerib läbi kuni jõuab 255
declare @Number int
set @Number = 1
while (@Number <= 255)
begin
print char(@Number)
set @Number = @Number + 1
end

--otsime suured tähed
-- kõik väiksed tähed asuvad vahemikus 97 - 122
declare @Number int
set @Number = 65
while (@Number <= 90)
begin
print char(@Number)
set @Number = @Number + 1
end

-- kõik väiksed tähed asuvad vahemikus 97 - 122
declare @Number int
set @Number = 97
while (@Number <= 122)
begin
print char(@Number)
set @Number = @Number + 1
end

-- väikseid tähti aga niimoodi, et muudame suured väikseks
declare @Number int
set @Number = 65
while(@Number <= 90)
begin
print lower(char(@Number))
set @Number = @Number + 1
end

-- kasutame trim funktsiooni
-- eemaldame tühikud vasakult poolelt
select ltrim('           Hello')
select ('                Hello')
-- eemaldame tühikud paremalt
select rtrim('Hello          ')
-- kui tavaline trim ei tööta
select rtrim(ltrim('   Hello  '))
-- tavaline trim
select trim('            Hello          ')
-- teeb kogu teksti ulatuses suured tähed väikseks
select lower('AbbbaGHDSDKJdsjssjkAdjjf')
-- teeb kogu teksti ulatuses suureks
select upper('AbbbaGHDSDKJdsjssjkAdjjf')
-- kogu teksti kuvame tagurpidi
select reverse('Minu nimi on Siim')
-- teksti pikkus, arvestab kuni viimase tähemärgini
select len('Minu nimi on Siim d  d')
-- võtame loetelust kolm esimest tähte
select left('abcdef', 3)
-- võtame loetelust kolm viimast tähte
select right('abcdef', 3)
-- tahame alates @ hakkaks lugema märkide arvu
select charindex('@','sara@aaa.com')
-- tahame teada mis domeeni kasutatakse, hakkab lugema alates 6 märgist
-- ning loeb peale seda 7 märki
select substring('sara@aaa.com',6,7)
-- kuidas saada domain teada dünaamiliselt
select substring('john@bbb.com', (charindex('@','john@bbb.com')+1),
(len('john@bbb.com') - charindex('@','john@bbb.com')))
-- tahame teada midu domeeni meil olemas
select Email from Employees
select substring(Email, charindex('@', Email) + 1,
len(Email) - charindex('@', Email)) as EmailDomain,
count(Email) as Total
from Employees
group by substring(Email, charindex('@',Email)+1,
len(Email) - charindex('@',Email))
