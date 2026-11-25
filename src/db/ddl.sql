CREATE TABLE IF NOT EXISTS employees (
	emp_id SERIAL PRIMARY KEY,
	emp_name VARCHAR(50) NOT NULL,
	emp_email VARCHAR(55) UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

INSERT INTO employees (
    emp_name, 
    emp_email
) values
    ('Matheus', 'matheus@email.com'),
	('Camila', 'camila@emial.com') 
ON CONFLICT (emp_email) DO NOTHING;
