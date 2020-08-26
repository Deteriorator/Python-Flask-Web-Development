#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    __init__.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.25   10:00
-------------------------------------------------------------------------------
   @Change:   2020.08.25
-------------------------------------------------------------------------------
"""
import logging
import os
import click

from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask

from blog.blueprints.admin import admin_bp
from blog.blueprints.auth import auth_bp
from blog.blueprints.blog import blog_bp
from blog.extensions import bootstrap, db, ckeditor, mail, moment, migrate
from blog.settings import config
from blog.models import Admin, Comment, Category, Post

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)

    register_commands(app)

    register_extensions(app)

    register_template_context(app)

    return app


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_commands(app):

    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True,
                  confirmation_prompt=True, help='The password used to login.')
    def init(username, password):
        """Building Bluelog, just for you."""

        click.echo('Initializing the database...')
        db.create_all()

        admin = Admin.query.first()
        if admin is not None:
            click.echo('The administrator already exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(
                username=username,
                blog_title='Bluelog',
                blog_sub_title="No, I'm the real thing.",
                name='Admin',
                about='Anything about you.'
            )
            admin.set_password(password)
            db.session.add(admin)

        category = Category.query.first()
        if category is None:
            click.echo('Creating the default category...')
            category = Category(name='Default')
            db.session.add(category)

        db.session.commit()
        click.echo('Done.')

    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    @click.option('--comment', default=500, help='Quantity of comments, default is 500.')
    def forge(category, post, comment):
        """Generates the fake categories, posts, and comments."""
        from blog.fakes import fake_admin, fake_categories, fake_posts, fake_comments
        db.drop_all()
        db.create_all()
        click.echo('Generating the administrator...')
        fake_admin()
        click.echo('Generating %d categories...' % category)
        fake_categories(category)
        click.echo('Generating %d posts...' % post)
        fake_posts(post)
        click.echo('Generating %d comments...' % comment)
        fake_comments(comment)
        click.echo('Done.')


def register_template_context(app):

    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        return dict(admin=admin, categories=categories)


if __name__ == '__main__':
    app = create_app()
    app.run()