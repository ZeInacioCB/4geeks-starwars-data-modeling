import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id= Column(Integer, primary_key=True)
    username = Column(String(200))
    firstname = Column(String(500))
    lastname = Column(String(500))
    email = Column(String(500))

class Followers(Base):
    __tablename__ = 'followers'
    follower_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

class Posts(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.post_id'))
    type = Column(String)
    url = Column(String, nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('posts.post_id'))
    text = Column(String(1000)) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagramInstagram.png')
