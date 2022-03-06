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

CREATE TABLE role_permission (
role_permission_id VARCHAR(20) NOT NULL,
role_id VARCHAR (40),
permission_id VARCHAR (40),
PRIMARY KEY (role_permission_id),
FOREIGN KEY (role_id) REFERENCES role(role_id),
FOREIGN KEY (permission_id) REFERENCES permission(permission_id)
);

CREATE TABLE user_role (
user_role_id VARCHAR(20) NOT NULL, 
user_id VARCHAR (40),
role_id VARCHAR (40),
PRIMARY KEY (user_role_id),
FOREIGN KEY (user_id) REFERENCES tus_user(user_id),
FOREIGN KEY (role_id) REFERENCES role(role_id)
);

CREATE TABLE user_module (
user_module_id VARCHAR(20) NOT NULL,
user_id VARCHAR (40),
module_id VARCHAR (40),
grade_id VARCHAR (40),
PRIMARY KEY (user_module_id),
FOREIGN KEY (user_id) REFERENCES tus_user(user_id),
FOREIGN KEY (module_id) REFERENCES module(module_id),
FOREIGN KEY (grade_id) REFERENCES grade(grade_id)
);

ALTER TABLE tus_user
ADD password VARCHAR(20);



