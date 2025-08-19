CREATE DATABASE IF NOT EXISTS photos_db;

USE photos_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    image_url VARCHAR(255) NOT NULL,
    likes INT DEFAULT 0
);

-- Insert a default admin user (password: adminpass)
INSERT IGNORE INTO users (username, hashed_password, is_admin) VALUES
('admin', '$2b$12$K8/N1.1.2.3.4.5.6.7.8.9.0.1.2.3.4.5.6.7.8.9.0', TRUE); -- This is a placeholder hash, generate a real one!

-- Insert some sample photos
INSERT INTO photos (title, description, image_url, likes) VALUES
('Sunset over Mountains', 'A beautiful sunset.', 'https://placehold.co/600x400/FF0000/FFFFFF?text=Sunset', 5),
('Forest Stream', 'Peaceful stream in the woods.', 'https://placehold.co/600x400/00FF00/FFFFFF?text=Forest', 10);