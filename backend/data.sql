INSERT INTO faculties (name, description) VALUES ('Faculty of Science', 'Dedicated to scientific research and innovation in various fields of science, including biology, physics, and chemistry.');
INSERT INTO faculties (name, description) VALUES ('Faculty of Arts', 'Fostering creativity and artistic expression through programs in literature, fine arts, and performing arts.');
INSERT INTO faculties (name, description) VALUES ('Faculty of Engineering', 'Leading the way in engineering solutions, technology, and cutting-edge research in mechanical, electrical, and civil engineering.');
INSERT INTO faculties (name, description) VALUES ('Faculty of Medicine', 'Committed to advancing healthcare and medical research to improve patient care and save lives.');
INSERT INTO faculties (name, description) VALUES ('Faculty of Business', 'Shaping future business leaders through top-notch education, entrepreneurship programs, and financial analysis.');



-- Departments for Faculty of Science
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Biology', 'Dr. Emily Smith', 'Promoting the study of living organisms and ecosystems.', 1);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Physics', 'Dr. James Anderson', 'Advancing research in the field of physics and its applications.', 1);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Chemistry', 'Dr. Sarah Johnson', 'Exploring chemical elements, compounds, and reactions.', 1);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Mathematics', 'Dr. Robert Davis', 'Fostering mathematical excellence and problem-solving.', 1);

-- Departments for Faculty of Arts
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Literature', 'Dr. Alice Wilson', 'Celebrating the world of literature and literary analysis.', 2);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of History', 'Dr. William Brown', 'Uncovering the past and preserving historical records.', 2);

-- Departments for Faculty of Engineering
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Mechanical Engineering', 'Prof. Michael Clark', 'Innovating in mechanical engineering and design.', 3);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Computer Science', 'Dr. Susan Lee', 'Advancing computer science research and technology.', 3);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Electrical Engineering', 'Prof. David Rogers', 'Pioneering electrical engineering solutions and innovations.', 3);

-- Departments for Faculty of Medicine
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Medicine', 'Dr. Jennifer Harris', 'Providing quality healthcare and medical research.', 4);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Nursing', 'Prof. John White', 'Training compassionate and skilled nurses.', 4);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Pharmacology', 'Dr. Patricia Martin', 'Advancing drug research and pharmaceutical science.', 4);

-- Departments for Faculty of Business
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Business Administration', 'Prof. Robert Johnson', 'Educating future business leaders and entrepreneurs.', 5);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Economics', 'Dr. Elizabeth Turner', 'Analyzing economic trends and policy.', 5);
INSERT INTO departments (name, hod, description, faculty_id) VALUES ('Department of Marketing', 'Prof. Sarah Lewis', 'Exploring marketing strategies and consumer behavior.', 5);


-- Courses for the Department of Biology
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Introduction to Biology', 'BIO101', 'Prof. Laura Anderson', 'Foundations of biological sciences.', 1),
    ('Genetics and Evolution', 'BIO201', 'Dr. Mark Smith', 'Exploring genetic principles and evolutionary biology.', 1);

INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Ecology and Environmental Science', 'BIO301', 'Prof. Sarah Walker', 'Study of ecosystems and environmental science.', 1),
    ('Human Anatomy and Physiology', 'BIO401', 'Dr. Emily Davis', 'In-depth examination of human anatomy and physiology.', 1);

-- Courses for the Department of Physics
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Classical Mechanics', 'PHY101', 'Prof. John Davis', 'Principles of classical physics.', 2),
    ('Quantum Physics', 'PHY201', 'Dr. Emily White', 'The world of quantum physics and quantum mechanics.', 2);

-- Courses for the Department of Chemistry
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Inorganic Chemistry', 'CHEM101', 'Prof. Robert Johnson', 'Study of inorganic compounds and reactions.', 3),
    ('Organic Chemistry', 'CHEM201', 'Dr. Sarah Miller', 'Exploring organic chemistry and organic compounds.', 3);

-- Courses for the Department of Mathematics
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Calculus I', 'MATH101', 'Prof. James Anderson', 'Fundamentals of calculus and mathematical analysis.', 4),
    ('Linear Algebra', 'MATH201', 'Dr. Susan Davis', 'Exploring linear algebra and its applications.', 4);

-- Courses for the Department of Literature
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Introduction to Literature', 'LIT101', 'Prof. Alice Wilson', 'An overview of literature from different periods.', 5),
    ('Shakespearean Studies', 'LIT201', 'Dr. William Brown', 'Exploring the works of William Shakespeare.', 5);

-- Courses for the Department of History
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('World History', 'HIST101', 'Prof. Laura Miller', 'A survey of world history from ancient times to the present.', 6),
    ('American History', 'HIST201', 'Dr. Michael Clark', 'Exploring the history of the United States.', 6);

-- Courses for the Department of Mechanical Engineering
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Mechanics of Materials', 'MECH101', 'Dr. Jennifer Harris', 'Stress analysis and mechanics of materials.', 7),
    ('Thermodynamics', 'MECH201', 'Prof. John White', 'Study of thermodynamic systems and principles.', 7);

-- Courses for the Department of Computer Science
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Introduction to Programming', 'COMP101', 'Dr. Patricia Martin', 'Basic programming concepts and principles.', 8),
    ('Database Management', 'COMP201', 'Prof. Robert Johnson', 'Exploring database systems and management.', 8);

-- Courses for the Department of Electrical Engineering
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Circuit Analysis', 'ELEC101', 'Dr. Elizabeth Turner', 'Fundamentals of electrical circuits and analysis.', 9),
    ('Digital Electronics', 'ELEC201', 'Prof. Sarah Lewis', 'Study of digital electronic systems and design.', 9);

-- Courses for the Department of Medicine
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Medical Ethics', 'MED101', 'Prof. Emily Smith', 'Ethical considerations in the field of medicine.', 10),
    ('Anatomy and Physiology', 'MED201', 'Dr. David Rogers', 'Study of human anatomy and physiological systems.', 10);

-- Courses for the Department of Nursing
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Nursing Fundamentals', 'NURS101', 'Dr. Susan Lee', 'Basic nursing principles and patient care.', 11),
    ('Community Health Nursing', 'NURS201', 'Prof. Laura Anderson', 'Community-based healthcare and nursing practice.', 11);

-- Courses for the Department of Pharmacology
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Pharmacology Principles', 'PHARM101', 'Prof. Mark Smith', 'Fundamental principles of pharmacology.', 12),
    ('Pharmaceutical Research', 'PHARM201', 'Dr. Sarah Johnson', 'Exploring drug research and development.', 12);

-- Courses for the Department of Business Administration
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Introduction to Business Management', 'BADM101', 'Dr. Jennifer Harris', 'Foundations of business management.', 13),
    ('Marketing Strategies', 'BADM201', 'Prof. John White', 'Exploring marketing strategies and tactics.', 13);

-- Courses for the Department of Economics
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Microeconomics', 'ECON101', 'Prof. Patricia Martin', 'Principles of microeconomics and economic analysis.', 14),
    ('Macroeconomics', 'ECON201', 'Dr. Robert Davis', 'Study of macroeconomics and economic systems.', 14);

-- Courses for the Department of Marketing
INSERT INTO courses (title, code, instructor, description, department_id)
VALUES
    ('Marketing Management', 'MKTG101', 'Prof. Sarah Lewis', 'Management of marketing activities and campaigns.', 15),
    ('Consumer Behavior Analysis', 'MKTG201', 'Dr. William Brown', 'Understanding consumer behavior and market research.', 15);


-- Students in the Department of Biology
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/BIOL/001', 'John', 'Smith', 'Male', 'john.smith@example.com', '123 Elm Street', '2000-01-15', 1),
    ('20/BIOL/002', 'Emma', 'Johnson', 'Female', 'emma.johnson@example.com', '456 Oak Avenue', '2001-03-20', 1);

-- Students in the Department of Physics
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/PHY/001', 'Olivia', 'Brown', 'Female', 'olivia.brown@example.com', '321 Pine Road', '2000-02-05', 2),
    ('20/PHY/002', 'William', 'Davis', 'Male', 'william.davis@example.com', '654 Birch Street', '2001-04-25', 2);

-- Students in the Department of Chemistry
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/CHEM/001', 'Liam', 'Taylor', 'Male', 'liam.taylor@example.com', '111 Oak Lane', '1999-12-10', 3),
    ('20/CHEM/002', 'Isabella', 'Moore', 'Female', 'isabella.moore@example.com', '444 Elm Street', '2001-02-18', 3);

-- Students in the Department of Mathematics
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/MATH/001', 'Sophia', 'Miller', 'Female', 'sophia.miller@example.com', '987 Cedar Avenue', '2002-08-15', 4),
    ('20/MATH/002', 'Liam', 'Wilson', 'Male', 'liam.wilson@example.com', '555 Maple Lane', '2003-01-10', 4);

-- Students in the Department of Literature
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/LIT/001', 'Mia', 'Harris', 'Female', 'mia.harris@example.com', '333 Pine Avenue', '2000-06-20', 5),
    ('20/LIT/002', 'Noah', 'Turner', 'Male', 'noah.turner@example.com', '222 Elm Road', '2001-10-05', 5);

-- Continue adding students for the other departments

INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/HIST/001', 'Ava', 'Smith', 'Female', 'ava.smith1@example.com', '123 Elm Street - History', '2000-01-15', 6),
    ('20/HIST/002', 'Liam', 'Johnson', 'Male', 'liam.johnson1@example.com', '456 Oak Avenue - History', '2001-03-20', 6);

-- Students in the Department of Mechanical Engineering (Department ID 7)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/MECH/001', 'Olivia', 'Brown', 'Female', 'olivia.brown1@example.com', '321 Pine Road - Mechanical Engineering', '2000-02-05', 7),
    ('20/MECH/002', 'William', 'Davis', 'Male', 'william.davis1@example.com', '654 Birch Street - Mechanical Engineering', '2001-04-25', 7);

-- Students in the Department of Computer Science (Department ID 8)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/COMP/001', 'Sophia', 'Miller', 'Female', 'sophia.miller1@example.com', '987 Cedar Avenue - Computer Science', '2002-08-15', 8),
    ('20/COMP/002', 'Liam', 'Wilson', 'Male', 'liam.wilson1@example.com', '555 Maple Lane - Computer Science', '2003-01-10', 8);

-- Students in the Department of Electrical Engineering (Department ID 9)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/ELEC/001', 'Mia', 'Harris', 'Female', 'mia.harris1@example.com', '333 Pine Avenue - Electrical Engineering', '2000-06-20', 9),
    ('20/ELEC/002', 'Noah', 'Turner', 'Male', 'noah.turner1@example.com', '222 Elm Road - Electrical Engineering', '2001-10-05', 9);

-- Students in the Department of Medicine (Department ID 10)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/MED/001', 'Oliver', 'Clark', 'Male', 'oliver.clark1@example.com', '444 Oak Street - Medicine', '2000-03-25', 10),
    ('20/MED/002', 'Charlotte', 'Roberts', 'Female', 'charlotte.roberts1@example.com', '777 Elm Avenue - Medicine', '2001-09-15', 10);

-- Students in the Department of Nursing (Department ID 11)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/NURS/001', 'Liam', 'White', 'Male', 'liam.white1@example.com', '555 Pine Road - Nursing', '2000-07-10', 11),
    ('20/NURS/002', 'Emma', 'Hall', 'Female', 'emma.hall1@example.com', '999 Cedar Lane - Nursing', '2001-12-05', 11);

-- Students in the Department of Pharmacology (Department ID 12)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/PHARM/001', 'Mason', 'Lee', 'Male', 'mason.lee1@example.com', '777 Birch Street - Pharmacology', '2000-04-20', 12),
    ('20/PHARM/002', 'Olivia', 'Davis', 'Female', 'olivia.davis1@example.com', '333 Elm Lane - Pharmacology', '2001-11-10', 12);

-- Students in the Department of Business Administration (Department ID 13)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/BADM/001', 'Sophia', 'Scott', 'Female', 'sophia.scott1@example.com', '123 Pine Avenue - Business Administration', '2000-08-15', 13),
    ('20/BADM/002', 'Liam', 'King', 'Male', 'liam.king1@example.com', '666 Oak Road - Business Administration', '2001-01-25', 13);

-- Students in the Department of Economics (Department ID 14)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/ECON/001', 'Mia', 'Turner', 'Female', 'mia.turner1@example.com', '444 Cedar Street - Economics', '2000-05-10', 14),
    ('20/ECON/002', 'Noah', 'Baker', 'Male', 'noah.baker1@example.com', '999 Elm Avenue - Economics', '2001-10-20', 14);

-- Students in the Department of Marketing (Department ID 15)
INSERT INTO students (matric_number, first_name, last_name, gender, email, address, dob, department_id)
VALUES
    ('20/MKT/001', 'Oliver', 'Adams', 'Male', 'oliver.adams1@example.com', '321 Pine Lane - Marketing', '2000-06-05', 15),
    ('20/MKT/002', 'Charlotte', 'Harris', 'Female', 'charlotte.harris1@example.com', '777 Cedar Road - Marketing', '2001-12-15', 15);



-- Enroll students in courses with grades
-- Replace 'student_id_here' and 'course_id_here' with actual student and course IDs

-- Enrollment for Student 1 in Course 1 with Grade A
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (1, 1, 'A');

-- Enrollment for Student 1 in Course 2 with Grade B
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (1, 2, 'B');

-- Enrollment for Student 2 in Course 1 with Grade C
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (2, 1, 'C');

-- Enrollment for Student 2 in Course 2 with Grade D
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (2, 2, 'D');

-- Enrollment for Student 3 in Course 3 with Grade A
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (3, 3, 'A');

-- Enrollment for Student 3 in Course 4 with Grade B
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (3, 4, 'B');

-- Continue adding enrollments for other students and courses with appropriate grades

