CREATE TABLE tus_user (
user_id VARCHAR (40) NOT NULL,
first_name VARCHAR(20),
last_name VARCHAR(20),
email  VARCHAR(40),
PRIMARY KEY (user_id)
);


CREATE TABLE grade (
grade_id VARCHAR (40),
assessment_mark DOUBLE,
exam_mark DOUBLE,
final_mark DOUBLE,
PRIMARY KEY (grade_id)
);

CREATE TABLE module (
module_id VARCHAR (40),
module_name VARCHAR(40),
PRIMARY KEY (module_id)
);

CREATE TABLE role (
role_id VARCHAR (40),
role_type VARCHAR(20),
PRIMARY KEY (role_id)
);

CREATE TABLE permission (
permission_id VARCHAR (40),
url VARCHAR(40),
PRIMARY KEY (permission_id)
);


CREATE TABLE user_module (
user_module_id VARCHAR(20) NOT NULL,
user_id VARCHAR(40) NOT NULL, 
module_id VARCHAR(20) NOT NULL, 
grade_id VARCHAR(6) NOT NULL,
PRIMARY KEY (user_module_id)
);



