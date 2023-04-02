CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  gender VARCHAR(10) NOT NULL,
  age INTEGER NOT NULL,
  location VARCHAR(255) NOT NULL,
  bio TEXT,
  profile_pic_url TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE likes (
  id SERIAL PRIMARY KEY,
  sender_id INTEGER REFERENCES users(id) NOT NULL,
  receiver_id INTEGER REFERENCES users(id) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  user1_id INTEGER REFERENCES users(id) NOT NULL,
  user2_id INTEGER REFERENCES users(id) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  sender_id INTEGER REFERENCES users(id) NOT NULL,
  receiver_id INTEGER REFERENCES users(id) NOT NULL,
  message TEXT NOT NULL,
  sent_at TIMESTAMP DEFAULT NOW()
);
